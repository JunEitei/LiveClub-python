import os


def replace_audio_tag_in_md_files(folder_path):
    # 遍历指定文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):  # 检查文件扩展名
                file_path = os.path.join(root, file)
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 替换内容
                new_content = content.replace('>{{< ऑडियो', '>{{< audio')

                # 仅在内容发生变化时写入文件
                if content != new_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f'Replaced in: {file_path}')
                    print(f'Repla')


# 指定要处理的文件夹路径
folder_path = 'Posts'  # 替换为你的文件夹路径
replace_audio_tag_in_md_files(folder_path)
