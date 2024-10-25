import os

# 要處理的目標文件夾路徑
folder_path = 'M'

# 要替換的舊字符串和新字符串
old_string = '%E6%A1%83.mp3'
new_string = '%E6%A1%83.m4a'

# 遍歷文件夾中的所有 .md 文件
for filename in os.listdir(folder_path):
    if filename.endswith(".md"):
        file_path = os.path.join(folder_path, filename)

        # 打開文件並讀取內容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 檢查文件內容是否包含要替換的字符串
        if old_string in content:
            # 進行替換
            new_content = content.replace(old_string, new_string)

            # 將替換後的內容寫回文件
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)

            print(f'Updated: {file_path}')

print("內容替換完成！")