import os

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # Skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

def get_total_size_of_damao_folders(parent_folder):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(parent_folder):
        # Check if 'damao' is in the directory path
        if 'damao' in dirpath:
            total_size += get_folder_size(dirpath)
    # Convert total size from bytes to megabytes
    total_size_mb = total_size / (1024 * 1024)
    return total_size_mb

# Example usage
parent_folder = "~/Downloads/mao/"
total_size_mb = get_total_size_of_damao_folders(os.path.expanduser(parent_folder))
print(f'Total size of all "damao" folders: {total_size_mb:.2f} MB')