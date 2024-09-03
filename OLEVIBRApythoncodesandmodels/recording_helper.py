import pyaudio
import scipy.signal
import numpy as np

def upsample_audio(audio, target_length=16000):
    original_length = len(audio)
    # Upsample the audio using linear interpolation
    upsampled_audio = scipy.signal.resample(audio, target_length)
    return upsampled_audio

def record_audio(stream, chunk=512):
    # Record audio data from the microphone
    audio_data = stream.read(chunk)
    return audio_data

if __name__ == "__main__":
    # Set parameters for audio recording
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    CHUNK = 512

    # Initialize PyAudio
    audio = pyaudio.PyAudio()
    DEVICE_INDEX = 1

    # Open audio stream
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK,
                        input_device_index=DEVICE_INDEX)

    print("Recording...")

    frames = []
    seconds = 1
    for i in range(0, int(RATE / CHUNK * seconds)):
        data = stream.read(CHUNK)
        frames.append(data)



    stream.stop_stream()
    stream.close()

    recorded_audio = np.frombuffer(b''.join(frames), dtype=np.int16)
    print("Recording stopped")
    print("Length of recorded audio:", len(recorded_audio))

    # Terminate PyAudio
    audio.terminate()

