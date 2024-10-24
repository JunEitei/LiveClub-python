import os

# 定义目标文件夹路径
music_folder = 'Music'  # 请将此处替换为你的音乐文件夹路径
output_file = 'README.md'

# 定义音频文件扩展名
audio_extensions = ('.mp3', '.wav', '.flac', '.aac', '.ogg', '.m4a')

# 创建README.md文件并写入标题
with open(output_file, 'w', encoding='utf-8') as file:
    file.write('# 音楽ファイルのディレクトリ\n\n')

    # 遍历文件夹
    for root, dirs, files in os.walk(music_folder):
        # 生成文件夹路径
        folder_name = os.path.relpath(root, music_folder)
        if folder_name == '.':
            folder_name = ''  # 根目录不需要显示

        # 写入文件夹名
        file.write(f'## {folder_name}\n\n' if folder_name else '## ルート\n\n')

        # 写入音频文件
        for filename in files:
            if filename.lower().endswith(audio_extensions):
                # 获取文件路径
                file_path = os.path.join(folder_name, filename) if folder_name else filename
                # 添加文件名到README
                file.write(f'- [{filename}]({file_path})\n')

        # 添加换行
        file.write('\n')

print(f"{output_file}が作成されました！")