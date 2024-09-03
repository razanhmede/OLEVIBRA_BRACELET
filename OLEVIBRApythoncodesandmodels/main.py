import numpy as np
import h5py
import tensorflow as tf
from tensorflow import keras
from recording_helper import record_audio
from tfhelper import preprocess_audiobuffer
import time
from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from luma.core.render import canvas
import pyaudio
import scipy.signal  # Import the scipy module for resampling

commands = ['stop' ,'up' ,'go', 'down' ,'no' ,'left' ,'right' ,'yes']
loaded_model = keras.models.load_model('/home/pi/Desktop/OLEVIBRA/my_model.h5')
loaded_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

def get_device():
    # Define your I2C interface and device here
    serial = i2c(port=1, address=0x3C)  # Adjust the address based on your OLED display
    return sh1106(serial)

def start():
    device = get_device()
    with canvas(device) as draw:
        draw.text((10, 10), "WELCOME TO OLEVIBRA!", fill="white")

    time.sleep(10)
    
def record_audio(stream, chunk=512):
    # Record audio data from the microphone
    audio= stream.read(chunk)
    return audio

def predict_mic():
    audio = record_audio(stream,chunk=512)
    spec = preprocess_audiobuffer(audio)
    prediction = loaded_model.predict(spec)
    label_pred = np.argmax(prediction, axis=1)
    label_index = label_pred[0]
    print("Predicted label index:", label_index)
    command = commands[label_index]
    print("Predicted command:", command)
    command = commands[label_index]
    print("Predicted label:", command)
    return command

if __name__ == "__main__":
    from Oledprintcom import printOLED 
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 512
    
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    
    while True:
        start()
        command = predict_mic()
        printOLED(command)
