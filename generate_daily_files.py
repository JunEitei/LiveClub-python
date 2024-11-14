import os

# 文件保存路径
folder_path = os.path.expanduser('~/Downloads/g')  # 替换为你的文件夹路径

# 确保目录存在
os.makedirs(folder_path, exist_ok=True)

# 初始日期
month = 2
day = 1

# 生成 35 个文件
for i in range(1, 36):
    # 如果月份是2月且日期超过29号，则切换到3月，并重置日期
    if month == 2 and day > 29:
        month = 3
        day = 1

    # 格式化月份和日期，确保它们有两个数字（例如，01, 02, ..., 09, 10, ..., 31）
    formatted_month = str(month).zfill(2)
    formatted_day = str(day).zfill(2)

    # 格式化文件名
    file_name = f"2007-{formatted_month}-{formatted_day}.mitsuko.md"
    file_path = os.path.join(folder_path, file_name)

    # 格式化内容
    content = f"""+++
date = 2007-{formatted_month}-{formatted_day}T13:54:53Z
[params]
picture = "/photos/mitsuko/{i}.jpg"
+++
"""
    # 写入文件
    with open(file_path, 'w') as f:
        f.write(content)

    print(f"文件 {file_name} 已生成")

    # 增加日期
    day += 1