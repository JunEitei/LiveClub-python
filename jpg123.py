import os

# 设置目标文件夹路径
folder_path = os.path.expanduser('~/Downloads/g')  # 替换为你的文件夹路径

# 获取文件夹中所有文件列表
files = os.listdir(folder_path)

# 只保留文件，去除目录
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

# 对文件进行排序（根据文件名或其他条件）
files.sort()

# 遍历文件并重命名2
for index, file in enumerate(files, start=1):
    # 获取文件扩展名
    ext = file.split('.')[-1]

    # 构造新的文件名
    new_name = f"{index}.jpg"

    # 获取文件的完整路径
    old_file_path = os.path.join(folder_path, file)
    new_file_path = os.path.join(folder_path, new_name)

    # 重命名文件
    os.rename(old_file_path, new_file_path)

    print(f"Renamed '{file}' to '{new_name}'")