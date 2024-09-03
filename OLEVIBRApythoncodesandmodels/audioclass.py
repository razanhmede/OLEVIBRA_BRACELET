import tensorflow as tf
import numpy as np
import librosa
import RPi.GPIO as GPIO
import time
import pyaudio
model = tf.keras.models.load_model('/home/pi/Desktop/OLEVIBRA/Model1.h5')
red_pin = 17
yellow_pin = 22
blue_pin = 27
white_pin=10
GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(yellow_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)
GPIO.setup(white_pin, GPIO.OUT)
def classify_audio(audio_data):
  
    audio_data = audio_data.reshape(1, -1)
    predictions = model.predict(audio_data)
    return np.argmax(predictions)


def control_led(prediction):
    #siren
    if prediction == 8:
        # Class 0 prediction, turn on red LED
        GPIO.output(red_pin, GPIO.HIGH)
        GPIO.output(yellow_pin, GPIO.LOW)
        GPIO.output(blue_pin, GPIO.LOW)
        GPIO.output(white_pin, GPIO.LOW)
    elif prediction == 6:
        #gunshot
        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(yellow_pin, GPIO.HIGH)
        GPIO.output(blue_pin, GPIO.LOW)
        GPIO.output(white_pin, GPIO.LOW)
    elif prediction == 1:
        #carhorn
        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(yellow_pin, GPIO.LOW)
        GPIO.output(blue_pin, GPIO.HIGH)
        GPIO.output(white_pin, GPIO.LOW)
    elif prediction == 3:
        #Dogbark
        GPIO.output(red_pin, GPIO.LOW)
        GPIO.output(yellow_pin, GPIO.LOW)
        GPIO.output(blue_pin, GPIO.LOW)
        GPIO.output(white_pin, GPIO.HIGH)

# Function to continuously record audio from USB microphone
def record_audio(stream, CHUNK):
    while True:
        data = stream.read(CHUNK)
        audio_data = np.frombuffer(data, dtype=np.int16)
        prediction = classify_audio(audio_data)
        control_led(prediction)

# Setup USB microphone stream
CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Record and classify audio
try:
    print("Recording started...")
    record_audio(stream, CHUNK)
except KeyboardInterrupt:
    print("Recording stopped by user.")
finally:
    # Turn off all LEDs
    GPIO.output(red_pin, GPIO.LOW)
    GPIO.output(yellow_pin, GPIO.LOW)
    GPIO.output(blue_pin, GPIO.LOW)
    GPIO.output(white_pin, GPIO.LOW)

    # Cleanup GPIO and stream
    GPIO.cleanup()
    stream.stop_stream()
    stream.close()
    p.terminate()
