import os

# 文件保存路径
folder_path = os.path.expanduser('~/Downloads/g')  # 替换为你的文件夹路径

# 确保目录存在
os.makedirs(folder_path, exist_ok=True)

# 生成 35 个文件
for i in range(1, 36):
    # 格式化文件名，确保 X 只有一个零前导零（1到9会补充0）
    file_name = f"2008-02-{str(i).zfill(2)}.fuu.md"  # 使用zfill填充小于10的数字
    file_path = os.path.join(folder_path, file_name)

    # 格式化内容
    content = f"""+++
date = 2008-02-{str(i).zfill(2)}T13:54:53Z
[params]
picture = "/photos/fuu/{i}.jpg"
+++
"""

    # 写入文件
    with open(file_path, 'w') as f:
        f.write(content)

    print(f"文件 {file_name} 已生成")