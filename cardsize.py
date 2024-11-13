import os
from collections import defaultdict


def get_folder_size(folder_path):
    """计算指定文件夹的总大小"""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # 排除符号链接
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size


def get_total_size_of_folders(parent_folder):
    """获取 parent_folder 中 content 和 static/music, static/photos, static/videos 各文件夹的大小并累加"""
    total_sizes = defaultdict(int)  # 使用 defaultdict 来存储文件夹名和对应的大小
    # 扫描 content 目录
    content_folder = os.path.expanduser(os.path.join(parent_folder, "content"))
    if os.path.exists(content_folder):
        for dirpath, dirnames, filenames in os.walk(content_folder):
            folder_size = get_folder_size(dirpath)
            folder_name = os.path.basename(dirpath)  # 获取文件夹名
            total_sizes[folder_name] += folder_size  # 累加大小

    # 扫描 static/music, static/photos, static/videos 目录
    static_folder = os.path.expanduser(os.path.join(parent_folder, "static"))
    subfolders = ['music', 'photos', 'videos']

    for subfolder in subfolders:
        folder_path = os.path.join(static_folder, subfolder)
        if os.path.exists(folder_path):
            for dirpath, dirnames, filenames in os.walk(folder_path):
                folder_size = get_folder_size(dirpath)
                folder_name = os.path.basename(dirpath)  # 获取文件夹名
                total_sizes[folder_name] += folder_size  # 累加大小

    # 将每个文件夹的大小从字节转换为MB
    total_sizes_in_mb = {folder: size / (1024 * 1024) for folder, size in total_sizes.items()}
    return total_sizes_in_mb


# 示例用法
parent_folder = "~/Downloads/mao/"
folder_sizes = get_total_size_of_folders(os.path.expanduser(parent_folder))

# 打印每个符合条件的文件夹及其大小
for folder, size in folder_sizes.items():
    # 排除包含 content, music, photos, videos 的文件夹
    if any(exclude in folder for exclude in ['content', 'music', 'photos', 'videos']):
        continue
    print(f"Folder: {folder} - Total Size: {size:.2f} MB")