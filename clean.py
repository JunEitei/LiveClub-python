import json

# 读取 JSON 文件
with open('D.postman_collection.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 提取并转换为 Markdown 表格
def json_to_md_table(json_data):
    table_md = ""
    for item in json_data["item"]:
        table_md += f'### {item["name"]}\n\n'
        table_md += "| Key | Value |\n"
        table_md += "| --- | ----- |\n"
        for header in item["request"]["header"]:
            table_md += f'| {header["key"]} | {header["value"]} |\n'
        table_md += "\n"
    return table_md

# 将 Markdown 表格保存到文件
with open('output.md', 'w', encoding='utf-8') as file:
    md_table = json_to_md_table(data)
    file.write(md_table)

print("转换完成，Markdown 表格已保存到 'output.md' 文件中。")