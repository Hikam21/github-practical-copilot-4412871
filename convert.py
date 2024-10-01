import os

# Create a function that reads audio files in the mp3 format from
# the 'audio' directory and list them
def list_files():
    audio_files = [f for f in os.listdir('audio') if f.endswith('.mp3')]
    return audio_files

print(list_files())