import io
from pydub import AudioSegment

sound_queue = []

def play_audio(audio):
    sr = 16000
    s = io.BytesIO(audio)
    channels = 1
    sample_width = 2

    audio = AudioSegment.from_raw(s, sample_width=sample_width, frame_rate=sr, channels=channels)
    sound = pygame.mixer.Sound(io.BytesIO(audio.raw_data))
    sound_queue.append(sound)
    sound.play()

    # Wait for the audio to finish playing
    duration_ms = sound.get_length() * 1000  # Convert seconds to milliseconds
    pygame.time.wait(int(duration_ms))
