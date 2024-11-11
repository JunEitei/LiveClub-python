import os
import json
# 音樂目錄路徑
music_directory = os.path.expanduser('~/Downloads/mao/static/music/')

# 獲取音樂文件列表
music_files = [f for f in os.listdir(music_directory) if f.endswith('.m4a')]

# 將文件路徑轉換為完整路徑
music_files = [os.path.join(music_directory, f) for f in music_files]

json_file_path = 'music_files.json'
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(music_files, json_file, ensure_ascii=False, indent=4)
    json.dump(music_files, json_file)
    json.dump(music_files, json_file)
with open()