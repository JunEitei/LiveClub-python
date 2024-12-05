import json

# 读取 JSON 文件
with open('D.postman_collection.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 繁體中文翻譯對照表
translation_dict = {
    "host": "主機",
    "Accept": "接受",
    "User-Agent": "用戶代理",
    "Content-Type": "內容類型",
    "Sec-Fetch-Dest": "安全取取目的地",
    "Sec-Fetch-Mode": "安全取取模式",
    "Sec-Fetch-Site": "安全取取站點"
}


# 提取并转换为 Markdown 表格
def json_to_md_table(json_data):
    table_md = ""
    for item in json_data["item"]:
        table_md += f'### {item["name"]}\n\n'
        table_md += "| Key | Value |\n"
        table_md += "| --- | ----- |\n"
        for header in item["request"]["header"]:
            # 如果字段在翻譯對照表中，則替換為繁體中文
            key_translated = translation_dict.get(header["key"], header["key"])
            table_md += f'| {key_translated} | {header["value"]} |\n'
        table_md += "\n"
    return table_md


# 将 Markdown 表格保存到文件
with open('output.md', 'w', encoding='utf-8') as file:
    md_table = json_to_md_table(data)
    file.write(md_table)

print("转换完成，Markdown 表格已保存到 'output.md' 文件中。")
