import pyaudio
import numpy as np
import RPi.GPIO as GPIO

def calculate_rms(audio_data):
    # Convert raw audio data to numpy array
    audio_np = np.frombuffer(audio_data, dtype=np.int16)
    # Ensure non-negative values before squaring
    audio_np = np.abs(audio_np)
    # Calculate RMS amplitude
    rms = np.sqrt(np.mean(np.square(audio_np)))
    return rms

def record_audio(stream, chunk=512):
    # Record audio data from the microphone
    audio_data = stream.read(chunk)
    return audio_data

def map_intensity(audio_intensity):
    min_audio_intensity = 0
    max_audio_intensity = 255  # Maximum intensity for 8-bit audio
    min_motor_intensity = 0
    max_motor_intensity = 100  # Maximum PWM duty cycle

    return min_motor_intensity + (audio_intensity - min_audio_intensity) * (max_motor_intensity - min_motor_intensity) / (max_audio_intensity - min_audio_intensity)
    
if __name__ == "__main__":
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 512


    GPIO.setmode(GPIO.BCM)
    motor_pin = 18
    GPIO.setup(motor_pin, GPIO.OUT)


    audio = pyaudio.PyAudio()
    DEVICE_INDEX = 1  
    
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK,
                        input_device_index=DEVICE_INDEX)
                        

    print("Recording...")

    try:
        
        motor_pwm = GPIO.PWM(motor_pin, 100)  
        motor_pwm.start(0) 

        while True:
            # Record audio
            audio_data = record_audio(stream, CHUNK)
          
            rms = calculate_rms(audio_data)
         
            if not np.isnan(rms):
                
                motor_intensity = map_intensity(rms)
                
                motor_pwm.ChangeDutyCycle(motor_intensity)
                print(f"RMS Amplitude: {rms:.2f}, Motor Intensity: {motor_intensity:.2f}")
            else:
                print("Invalid RMS Amplitude")
    except KeyboardInterrupt:
        GPIO.cleanup()
        
        motor_pwm.stop()
        GPIO.cleanup()
        stream.stop_stream()
        stream.close()
        audio.terminate()

