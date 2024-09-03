import pyaudio
import numpy as np
import RPi.GPIO as GPIO

# Set up GPIO
GPIO.setmode(GPIO.BCM)
motor_pin = 18  # Example pin for motor control
GPIO.setup(motor_pin, GPIO.OUT)

# PyAudio configuration
FRAMES_PER_BUFFER = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 44100
RATE = 16000
DEVICE_INDEX = 1  # Change this to the index of your USB microphone
p = pyaudio.PyAudio()

def record_audio(duration):
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=FRAMES_PER_BUFFER,
        input_device_index=DEVICE_INDEX
    )

    frames = []
    total_frames = int(RATE / FRAMES_PER_BUFFER * duration)
    for i in range(total_frames):
        data = stream.read(FRAMES_PER_BUFFER)
        frames.append(data)
        # Check for sound intensity and set motor pin to high if sound detected
        audio_data = np.frombuffer(data, dtype=np.int16)
        if np.max(audio_data) > threshold:
            GPIO.output(motor_pin, GPIO.HIGH)  # Turn motor on
        else:
            GPIO.output(motor_pin, GPIO.LOW)   # Turn motor off

    stream.stop_stream()
    stream.close()
    
    return np.frombuffer(b''.join(frames), dtype=np.int16)

def terminate():
    p.terminate()
    GPIO.cleanup()

# Define threshold for sound intensity (adjust as needed)
threshold = 10000

# Example usage: Record audio for 5 seconds
audio_data = record_audio(duration=15)

# Terminate PyAudio and clean up GPIO
terminate()
