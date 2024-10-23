import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import colorsys
import simpleaudio as sa
import threading

# 基本设定
A4_frequency = 440.0  # A4 音符的频率为 440Hz
C5_color = np.array([1, 0, 0])  # C5 对应的颜色为红色 (RGB 归一化值)

# 十二平均律的半音间隔比率，计算音符频率时使用
semitone_ratio = 2 ** (1 / 12)

# 定义八度内的音符，从 A4 到 G5
notes = [
    "A", "Bb", "B", "C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab"
]
# 计算对应音符的频率
frequencies = [A4_frequency * (semitone_ratio ** i) for i in range(len(notes))]


# 定义一个函数，用于将频率转换为颜色值
def frequency_to_color(frequency, base_frequency, base_color):
    """
    将音符的频率转换为颜色值。

    参数:
    - frequency: 当前音符的频率
    - base_frequency: 基准频率（例如 C5 的频率）
    - base_color: 基准颜色（例如 C5 的颜色）

    返回:
    - 转换后的颜色 (RGB格式)
    """
    ratio = frequency / base_frequency  # 计算当前频率相对于基准频率的比率
    hue = (np.log2(ratio) % 1)  # 将频率比率映射到色相 (Hue) 值，范围为 0 到 1
    # 使用 colorsys 库将 HSV 模型的颜色转换为 RGB 模型
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)  # 其中饱和度 (S) 和亮度 (V) 均设置为 1
    return np.array([r, g, b])


# 计算所有音符的颜色
base_frequency = frequencies[3]  # 基准频率（C5 的频率）
base_color = C5_color  # 基准颜色（C5 的颜色）

# 对所有音符计算其颜色值
colors = [frequency_to_color(f, base_frequency, base_color) for f in frequencies]
# 确保 C5 的颜色为红色
colors[3] = C5_color


# 将 RGB 颜色值转换为 HEX 颜色代码
def rgb_to_hex(rgb):
    """
    将 RGB 颜色转换为 HEX 颜色代码。

    参数:
    - rgb: RGB 颜色 (归一化值)

    返回:
    - HEX 颜色值
    """
    # 将 RGB 颜色的三个分量转换为两位十六进制数，并连接为字符串
    return '#' + ''.join(f'{int(c * 255):02X}' for c in rgb)


# 将所有音符的 RGB 颜色值转换为 HEX 颜色代码
hex_colors = [rgb_to_hex(color) for color in colors]

# 创建用于绘制色轮的图形
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'aspect': 'equal'})

# 初始化一些控制旋转的参数
rotation = 0  # 色轮的初始旋转角度
start_x = None  # 记录鼠标按下时的 x 坐标
start_y = None  # 记录鼠标按下时的 y 坐标
last_angle = None  # 记录上一次的旋转角度


# 绘制色轮的函数
def draw_color_wheel(rotation):
    ax.clear()  # 清除之前的绘图
    # 使旋转角度在 0 到 360 度之间循环
    angle_shift = rotation % 360

    # 循环绘制每个音符对应的扇区和文字
    for i, (note, color, hex_color, frequency) in enumerate(zip(notes, colors, hex_colors, frequencies)):
        # 创建并绘制一个扇区，表示一个音符的颜色
        wedge = patches.Wedge(
            center=(0, 0), r=1,  # 扇区的圆心和半径
            theta1=angle_shift + (360 / len(notes)) * i,  # 扇区的起始角度
            theta2=angle_shift + (360 / len(notes)) * (i + 1),  # 扇区的结束角度
            facecolor=color,  # 扇区的填充颜色
            edgecolor='none'  # 无边框
        )
        ax.add_patch(wedge)  # 将扇区添加到图形中

        # 计算并绘制音符名称和对应的 HEX 颜色代码
        angle_rad = np.deg2rad(angle_shift + (360 / len(notes)) * (i + 0.5))
        x = 0.6 * np.cos(angle_rad)  # 文字的 x 坐标
        y = 0.6 * np.sin(angle_rad)  # 文字的 y 坐标
        # 在扇区内添加音符名称
        ax.text(x, y, note, ha='center', va='center', fontsize=10, color='black')
        # 在扇区内添加 HEX 颜色代码
        ax.text(x, y - 0.1, hex_color, ha='center', va='center', fontsize=8, color='black')

    # 绘制指针指向下方，指示当前选中的音符
    pointer_length = 0.2  # 指针的长度
    pointer_width = 0.05  # 指针的宽度
    pointer = patches.FancyArrow(
        0, -pointer_length, 0, pointer_length,
        width=pointer_width, color='white', alpha=0.7  # 指针的颜色和透明度
    )
    ax.add_patch(pointer)  # 将指针添加到图形中

    # 设置图形的显示范围，确保所有内容都在可视范围内
    ax.set_xlim(-1.5, 1.5)  # 设置 x 轴的显示范围
    ax.set_ylim(-1.5, 1.5)  # 设置 y 轴的显示范围
    ax.axis('off')  # 关闭坐标轴显示
    plt.title("Color Wheel of Notes with HEX Values (One Octave)")  # 设置图形标题


# 获取点(x,y)相对于原点的角度
def get_angle(x, y):
    return np.degrees(np.arctan2(y, x))  # 使用反正切函数计算角度并转换为度数


# 播放一个频率对应的音符
def play_tone(frequency):
    sample_rate = 44100  # 采样率，表示每秒样本数量
    duration = 1.0  # 音符持续时间（秒）
    t = np.linspace(0, duration, int(sample_rate * duration), False)  # 时间点
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # 生成正弦波音符
    wave = (wave * 32767).astype(np.int16)  # 转换为 16 位 PCM 数据
    play_obj = sa.play_buffer(wave, 1, 2, sample_rate)  # 播放音频
    play_obj.wait_done()  # 等待音频播放完成


# 启动一个线程来播放音符
def play_tone_thread(frequency):
    # 创建并启动一个线程，用于后台播放音符
    thread = threading.Thread(target=play_tone, args=(frequency,))
    thread.start()  # 启动线程


# 鼠标按下事件处理函数
def on_press(event):
    global start_x, start_y, last_angle
    if event.inaxes == ax:  # 确保鼠标点击在图形内
        start_x = event.xdata  # 记录按下时的 x 坐标
        start_y = event.ydata  # 记录按下时的 y 坐标
        last_angle = get_angle(event.xdata - 0.5, event.ydata - 0.5)  # 计算按下点的角度
        # 检查鼠标是否点击在某个音符的扇区内
        click_angle = np.degrees(np.arctan2(event.ydata, event.xdata)) % 360
        for i, frequency in enumerate(frequencies):
            wedge_angle_start = (rotation + (360 / len(notes)) * i) % 360
            wedge_angle_end = (rotation + (360 / len(notes)) * (i + 1)) % 360
            if wedge_angle_start <= click_angle < wedge_angle_end:
                play_tone_thread(frequency)  # 点击后在后台线程中播放对应音符
                break


# 鼠标拖动事件处理函数
def on_motion(event):
    global rotation, start_x, start_y, last_angle
    if event.inaxes == ax and start_x is not None and start_y is not None:
        current_angle = get_angle(event.xdata - 0.5, event.ydata - 0.5)  # 计算当前点的角度
        rotation += current_angle - last_angle  # 更新旋转角度
        last_angle = current_angle  # 更新上一次角度
        draw_color_wheel(rotation)  # 根据新的旋转角度重绘色轮
        plt.draw()  # 更新绘图


# 鼠标释放事件处理函数
def on_release(event):
    global start_x, start_y
    start_x = None  # 清除鼠标按下的 x 坐标记录
    start_y = None  # 清除鼠标按下的 y 坐标记录


# 连接鼠标事件到处理函数
fig.canvas.mpl_connect('button_press_event', on_press)  # 连接鼠标按下事件
fig.canvas.mpl_connect('motion_notify_event', on_motion)  # 连接鼠标拖动事件
fig.canvas.mpl_connect('button_release_event', on_release)  # 连接鼠标释放事件

# 绘制初始色轮并显示
draw_color_wheel(rotation)
plt.show()
