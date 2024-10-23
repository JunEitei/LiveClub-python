import os
from deep_translator import GoogleTranslator, exceptions

# 定义输入和输出文件夹路径
input_folder = 'Posts'  # 输入的 Markdown 文件夹
output_folder = 'Posts_de'  # 输出的 Markdown 文件夹，指定为德文

# 创建输出文件夹（如果不存在）
os.makedirs(output_folder, exist_ok=True)

# 遍历输入文件夹中的所有 Markdown 文件
for filename in os.listdir(input_folder):
    if filename.endswith('.md'):
        input_file_path = os.path.join(input_folder, filename)  # 输入文件路径
        output_file_path = os.path.join(output_folder, filename)  # 输出文件路径

        # 读取 Markdown 文件内容
        with open(input_file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()  # 逐行读取文件内容

        # 翻译内容并保留每一行末尾的空格
        translated_lines = []
        for line in content:
            # 去掉行末的空格，进行翻译，再加回空格
            trimmed_line = line.rstrip()  # 去掉行末空格

            try:
                translated_line = GoogleTranslator(source='auto', target='german').translate(trimmed_line)
                if translated_line is None:
                    translated_line = trimmed_line  # 如果翻译返回 None，则使用原始行

            except exceptions.NotValidPayload:  # 处理无效负载错误
                translated_line = trimmed_line  # 如果出现翻译错误，则使用原始行

            translated_lines.append(translated_line + ' ' * (len(line) - len(trimmed_line)))  # 加回原有的空格

        # 保存翻译后的内容到新文件
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.writelines(translated_lines)  # 写入翻译后的所有行

        print(f"翻译完成: {filename} -> {output_file_path}")

print("所有文件翻译完成！")