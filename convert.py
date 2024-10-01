import os
import yaml
import eyed3

def get_audio_files():
    audio_files = []
    for file in os.listdir('audio'):
        if file.endswith('.mp3'):
            audio_file = eyed3.load(os.path.join('audio', file))
            comments = ''
            if audio_file.tag.comments:
                for comment in audio_file.tag.comments:
                    comments += comment.text + '\n'
            audio_files.append({
                'title': audio_file.tag.title,
                'comments': comments
            })
    
    # Print the results in YAML format
    print(yaml.dump(audio_files, default_flow_style=False))

get_audio_files()