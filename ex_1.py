import pyaudio
import numpy as np
import requests

# Initialize PyAudio
pa = pyaudio.PyAudio()

# Define the callback function

def callback(in_data, frame_count, time_info, flag):
    audio_data = np.fromstring(in_data, dtype=np.float32)
    # Process audio data here
    return (in_data, pyaudio.paContinue)

# Open the audio stream
stream = pa.open(format=pyaudio.paFloat32,
                  channels=1,
                  rate=44100,
                  output=True,
                  input=True,
                  stream_callback=callback)

# Start the stream
stream.start_stream()
