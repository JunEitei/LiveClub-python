def modify_text(text):
    # 分割文本为行
    lines = text.splitlines()
    # 在每一行前面添加 >，并在末尾增加两个空格
    modified_lines = [f'· {line}  ' for line in lines]
    # 将修改后的行重新连接为文本
    modified_text = '\n'.join(modified_lines)
    return modified_text




# 示例文本
text = """4 = 2 + 2
6 = 3 + 3
8 = 3 + 5
10 = 5 + 5
12 = 5 + 7
14 = 7 + 7
16 = 3 + 13 や 5 + 11
18 = 5 + 13 や 7 + 11
20 = 3 + 17 や 7 + 13
22 = 3 + 19 や 5 + 17 や 11 + 11
24 = 5 + 19 や 7 + 17 や 11 + 13
26 = 3 + 23 や 7 + 19 や 13 + 13
28 = 5 + 23 や 11 + 17
30 = 7 + 23 や 11 + 19 や 13 + 17
32 = 3 + 29 や 13 + 19
34 = 3 + 31 や 5 + 29 や 11 + 23 や 17 + 17
36 = 5 + 31 や 7 + 29 や 13 + 23 や 17 + 19
38 = 7 + 31 や 19 + 19
40 = 3 + 37 や 11 + 29 や 17 + 23
42 = 5 + 37 や 11 + 31 や 13 + 29 や 19 + 23
44 = 3 + 41 や 7 + 37 や 13 + 31 や 17 + 27 や 23 + 21
46 = 5 + 41 や 19 + 27 や 23 + 23
48 = 5 + 43 や 11 + 37 や 17 + 31
50 = 3 + 47 や 7 + 43 や 13 + 37 や 19 + 31
52 = 5 + 47 や 11 + 41 や 23 + 29
54 = 7 + 47 や 13 + 41 や 23 + 31 や 27 + 27
56 = 3 + 53 や 13 + 43 や 19 + 37
58 = 5 + 53 や 11 + 47 や 17 + 41 や 29 + 29
60 = 7 + 53 や 13 + 47 や 19 + 41 や 23 + 37 や 29 + 31
62 = 3 + 59 や 29 + 33
64 = 3 + 61 や 7 + 57 や 31 + 33
66 = 5 + 61 や 31 + 35
68 = 7 + 61 や 17 + 51 や 31 + 37
70 = 23 + 47 や 37 + 33
72 = 17 + 55 や 37 + 35
74 = 3 + 71 や 7 + 67 や 17 + 57 や 37 + 37
76 = 3 + 73 や 13 + 63 や 31 + 45
78 = 11 + 67 や 37 + 41
80 = 3 + 77 や 13 + 67 や 19 + 61 や 29 + 51 や 37 + 43
82 = 11 + 71 や 41 + 41
84 = 5 + 79 や 23 + 61 や 41 + 43
86 = 7 + 79 や 29 + 57 や 43 + 43
88 = 19 + 69 や 23 + 65 や 41 + 47
90 = 17 + 73 や 31 + 59 や 43 + 47
92 = 5 + 87 や 11 + 81 や 41 + 51 や 47 + 45
94 = 47 + 47
96 = 11 + 85 や 23 + 73 や 41 + 55 や 47 + 49
98 = 19 + 79 や 29 + 69 や 47 + 51
100 = 3 + 97 や 11 + 89 や 17 + 83 や 29 + 71 や 41 + 59 や 47 + 53
102 = 19 + 83 や 23 + 79 や 29 + 73 や 41 + 61 や 47 + 55"""

# 调用函数
modified_text = modify_text(text)
print(modified_text)