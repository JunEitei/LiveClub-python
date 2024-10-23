import os

def add_language_suffix(folder_path, suffix):
    # 遍历指定文件夹
    for filename in os.listdir(folder_path):
        # 检查文件是否以.md结尾
        if filename.endswith('.md'):
            # 构造新的文件名
            new_filename = filename.replace('.md', f'{suffix}.md')
            # 获取完整的文件路径
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)
            # 重命名文件
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {old_file_path} -> {new_file_path}')

# 指定文件夹路径和后缀
folder_path = 'Posts'  # 替换为你的文件夹路径
suffix = '.ja'  # 要添加的后缀

# 调用函数
add_language_suffix(folder_path, suffix)