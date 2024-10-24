import os
from deep_translator import GoogleTranslator, exceptions

# 定义输入和输出文件夹路径
input_folder = 'Posts'  # 输入的 Markdown 文件夹
output_folder = 'Posts_vi'  # 输出的 Markdown 文件夹，指定为葡萄牙文

# 创建输出文件夹（如果不存在）
os.makedirs(output_folder, exist_ok=True)

# 遍历输入文件夹中的所有 Markdown 文件
for filename in os.listdir(input_folder):
    if filename.endswith('.md'):
        input_file_path = os.path.join(input_folder, filename)  # 输入文件路径

        # 修改输出文件名，将后缀从 .jp.md 改为 .pt.md
        output_file_name = filename.replace('.ja.md', '.vi.md')  # 替换后缀名
        output_file_path = os.path.join(output_folder, output_file_name)  # 输出文件路径

        # 读取 Markdown 文件内容
        with open(input_file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()  # 逐行读取文件内容

        # 提取前四行
        front_matter = content[:4]  # 保留前四行
        translated_lines = []

        # 翻译剩余的内容
        for line in content[4:]:  # 从第五行开始翻译
            trimmed_line = line.rstrip()  # 去掉行末空格

            # 记录原行的换行符和尾部空格
            newline_character = '\n' if line.endswith('\n') else ''
            trailing_spaces = len(line) - len(trimmed_line)  # 计算尾部空格数量
            try:
                translated_line = GoogleTranslator(source='auto', target='vietnamese').translate(trimmed_line)
                if translated_line is None:
                    translated_line = trimmed_line  # 如果翻译返回 None，则使用原始行

            except exceptions.NotValidPayload:  # 处理无效负载错误
                translated_line = trimmed_line  # 如果出现翻译错误，则使用原始行

            # 添加回原有的空格和换行符
            translated_lines.append(translated_line + ' ' * trailing_spaces + newline_character)

        # 将翻译后的内容合并
        final_content = front_matter + translated_lines

        # 更新 title 行
        for i, line in enumerate(final_content):
            if line.startswith('title ='):
                # 提取原有的标题并更新
                original_title = line.split('"')[1]  # 提取引号内的原始标题
                new_title = GoogleTranslator(source='auto', target='vietnamese').translate(original_title)  # 翻译标题
                final_content[i] = f'title = "{new_title}"\n'  # 替换为新的标题

        # 保存翻译后的内容到新文件
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.writelines(final_content)  # 写入翻译后的所有行

        print(f"翻译完成: {filename} -> {output_file_path}")

print("所有文件翻译完成！")