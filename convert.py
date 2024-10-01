import os
import yaml
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

def get_audio_files():
    audio_files = []
    for file in os.listdir('audio'):
        if file.endswith('.mp3'):
            file_path = os.path.join('audio', file)
            audio = MP3(file_path, ID3=EasyID3)
            comments = '\n'.join(audio.get('comment', []))
            audio_files.append({
                'title': audio.get('title', [''])[0],
                'comments': comments
            })
    return audio_files

print(yaml.dump(get_audio_files(), sort_keys=False))