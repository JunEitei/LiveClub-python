import os
from collections import defaultdict


def get_folder_size(folder_path):
    """指定したフォルダの総サイズを計算する"""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # シンボリックリンクは無視する
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size


def get_total_size_of_folders(parent_folder):
    # フォルダ名と対応するサイズを保存するために
    total_sizes = defaultdict(int)
    # content フォルダをスキャン
    content_folder = os.path.expanduser(os.path.join(parent_folder, "content"))
    if os.path.exists(content_folder):
        for dirpath, dirnames, filenames in os.walk(content_folder):
            folder_size = get_folder_size(dirpath)
            folder_name = os.path.basename(dirpath)  # フォルダ名を取得
            total_sizes[folder_name] += folder_size  # サイズを累積する

    # static/music, static/photos, static/videos フォルダをスキャン
    static_folder = os.path.expanduser(os.path.join(parent_folder, "static"))
    subfolders = ['music', 'photos', 'videos']

    for subfolder in subfolders:
        folder_path = os.path.join(static_folder, subfolder)
        if os.path.exists(folder_path):
            for dirpath, dirnames, filenames in os.walk(folder_path):
                folder_size = get_folder_size(dirpath)
                folder_name = os.path.basename(dirpath)  # フォルダ名を取得
                total_sizes[folder_name] += folder_size  # サイズを累積する

    # 各フォルダのサイズをバイトからMBに変換する
    total_sizes_in_mb = {folder: size / (1024 * 1024) for folder, size in total_sizes.items()}
    return total_sizes_in_mb


# サンプルの使い方
parent_folder = "~/Downloads/mao/"
folder_sizes = get_total_size_of_folders(os.path.expanduser(parent_folder))

# 条件に合った各フォルダのサイズを表示
for folder, size in folder_sizes.items():
    # content, music, photos, videos を含むフォルダは表示しない
    if any(exclude in folder for exclude in ['content', 'music', 'photos', 'videos']):
        continue
    print(f"Folder: {folder} - Total Size: {size:.2f} MB")