import os
import yaml
from mutagen.mp3 import MP3

def format_duration(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = int(seconds % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def get_audio_files():
    audio_files = []
    audio_files_path = os.path.join(os.getcwd(), 'audio')
    
    if not os.path.exists(audio_files_path):
        print(f"Directory not found: {audio_files_path}")
        return audio_files

    for file in os.listdir(audio_files_path):
        if file.endswith('.mp3'):
            try:
                audio_file = MP3(os.path.join(audio_files_path, file))
                duration = format_duration(audio_file.info.length)
                comments = audio_file.tags.getall('COMM') if audio_file.tags else []
                audio_files.append({
                    'title': audio_file.tags.get('TIT2', 'Unknown Title'),
                    'comments': comments,
                    'filename': os.path.join('/audio', file),
                    'duration': duration
                })
            except Exception as e:
                print(f"Error processing file {file}: {e}")
    return audio_files

def convert_to_yaml():
    data = get_audio_files()
    yaml_data = yaml.dump(data, sort_keys=False)
    return yaml_data

print(convert_to_yaml())