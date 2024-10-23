import os


def replace_language_code(folder_path):
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 只处理以 .md 结尾的文件
        if filename.endswith('.md'):
            file_path = os.path.join(folder_path, filename)

            # 读取文件内容
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # 替换 languageCode: 为 anguagCode:
            new_content = content.replace('languagCode:', 'languageCode =')

            # 将修改后的内容写回文件
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)

            print(f"Updated {filename}")


# 指定要处理的文件夹路径
folder_path = 'Posts1'
replace_language_code(folder_path)