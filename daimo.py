import os

def rename_files(directory):
    # 展开 ~ 为完整路径
    directory = os.path.expanduser(directory)
    # 遍历指定目录中的所有文件
    for filename in os.listdir(directory):
        # 检查文件是否以 .ja.md 结尾
        if filename.endswith(".ja.md"):
            # 构造旧文件路径
            old_file = os.path.join(directory, filename)
            # 构造新文件路径
            new_file = os.path.join(directory, filename.replace(".ja.md", ".daimo.md"))
            # 重命名文件
            os.rename(old_file, new_file)
            print(f'Renamed: {old_file} to {new_file}')

# 指定要重命名文件的目录
directory = "~/Downloads/mao/content/Posts/"

rename_files(directory)
