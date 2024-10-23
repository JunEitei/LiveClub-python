import os


def replace_in_file(file_path, old_string, new_string):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_data = file.read()

    new_data = file_data.replace(old_string, new_string)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_data)


def replace_in_folder(folder_path, old_string, new_string):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                replace_in_file(file_path, old_string, new_string)


folder_path = 'Posts'  # 将此处替换为你的文件夹路径
old_string = 'https://github.com/JunEitei/JunEitei.github.io/raw/main/music/'
new_string = 'https://dm-o.netlify.app/music/'

replace_in_folder(folder_path, old_string, new_string)