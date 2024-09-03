import pyaudio

pa = pyaudio.PyAudio()

# Get the index of the default input device
default_device_index = pa.get_default_input_device_info()['index']

# Get the number of available audio devices
num_devices = pa.get_device_count()

print("Available audio devices:")
for i in range(num_devices):
    device_info = pa.get_device_info_by_index(i)
    print(f"Device {i}: {device_info['name']}")
    print(f"  Max Input Channels: {device_info['maxInputChannels']}")
    print(f"  Default Sample Rate: {device_info['defaultSampleRate']}")
    print(f"  Host API: {device_info['hostApi']}")  # Optional, depending on your needs
    print("")

pa.terminate()

