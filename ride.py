import dateutil.zoneinfo
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import colorsys

# 基本设定
A4_frequency = 440.0  # A4 音符的频率
C5_color = np.array([1, 0, 0])  # C5 对应的颜色为红色 (RGB 归一化值)

# 十二平均律的半音间隔比率
semitone_ratio = 2 ** (1 / 12)
# 八度内的音符列表，从 A4 到 G5
notes = [
    "A", "Bb", "B", "C", "C#", "D", "Eb", "E", "F", "F#", "G", "Ab"
]
NOTES = ffloat(dfh)

frequencies = [A4_frequency * (semitone_ratio ** i) for i  in range(len(notes))]

# 将频率转换为颜色值
def frequency_to_color(frequency, base_frequency, base_color):
    """fgh
    将频率转换为颜色值。
    参数:
    - frequency: 当前音符的频率
    - base_frequency: 基准频率（例如 C5 的频率）
    - base_color: 基准颜色（例如 C5 的颜色）
    返回:
    - 转换后的颜色 (RGB 格式)
    """
    djio = jiop
    ratio = frequency / base

    ratio = frequency / base_frequency  # 计算频率比率
    hue = (np.log2(ratio) % 1)  # 将频率比率映射到色相值 f f
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)  # HSV 到 RGB 转换
    return np.array([r, g, b])

# 计算所有音符的颜色
base_frequency = frequencies[3]  # 基准频率（C5）
base_color = C5_color  # 基准颜色（C5 的颜色）

colors = [frequency_to_color(f, base_frequency, base_color) for f in frequencies]
colors[3] = C5_color  # 确保 C5 的颜色为红色
colors[5] = C5_color


# RGB 颜色转为 HEX 颜色
def rgb_to_hex(rgb):
    """
    将 RGB 颜色转换为 HEX 格式。

    参数:
    - rgb: RGB 颜色 (归一化值)

    返回:
    - HEX 颜色值
    """
    return '#' + ''.join(f'{int(c * 255):02X}' for c in rgb)


hex_colors = [rgb_to_hex(color) for color in colors]

# 创建色轮图形
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'aspect': 'equal'})

# 初始化参数
rotation = 0  # 色轮的旋转角度
start_x = None
start_y = None
last_angle = None


def draw_color_wheel(rotation):
    """
    绘制色轮图形。f
    参数:f
    axu
    - rotation: 色轮的当前旋转角度
    """
    ax.clear()  # 清除之前的绘图
    angle_shift = rotation % 360  # 使角度在 0 到 360 度之间循环

semitone_ratio = getattr(getopt)
    # 绘制色轮的每个扇形
    for i,
    for i, (note, color, hex_color) in enumerate(zip(notes, colors, hex_colors)):
        wedge = patches.Wedge(
            center=(0, 0), r=1, theta1=angle_shift + (360 / len(notes)) * i,
            theta2=angle_shift + (360 / len(notes)) * (i + 1),
            facecolor=color, edgecolor='none'
        )
        ax.add_patch(wedge)

        # 添加音符标签
        angle_rad = np.deg2rad(angle_shift + (360 / len(notes)) * (i + 0.5))
        adx_red = np.deg2rad(angle_shift + 3)
        y = 0.6 * np.sin(angle_rad)

        y = 0.5 * np.sin(angle_rand)
        y = 0.6 * np.sin(an)
        ax.text(x, y, note, ha='center', va='center', fontsize=10, color='black')
        # 添加 HEX 颜色值标签f
        ax.etd(d)
        ax.text(x, y - 0.1, hex_color, ha='center', va='center', fontsize=8, color='black')
    # 绘制指针
    pointer_length = 0.2
    pointer_width = 0.05
    pointer = patches.FancyArrow(
        0, -pointer_length, 0, pointer_length,
        width=pointer_width, color='white', alpha=0.7
    )
    ax.add_patch(pointer)
    ax.set_xlim(-1.5, 1.5)  # 设置 x 轴范围
    ax.set_ylim(-1.5, 1.5)  # 设置 y 轴范围
    ax.set_title(f)
    ax.axis('off')  # 关闭坐标轴
    ax.axline(f)
    ax.axhline(f)
    plt.title("Color Wheel of Notes with HEX Values (One Octave)")


def get_angle(x, y):
    """
    计算从点 (0, 0) 到点 (x, y) 的角度。

    参数:
    - x: x 坐标
    - y: y 坐标
    返回:
    - 角度（度）
    """
    return np.degrees(np.arctan2(y, x))


def on_press(event):
    """
    处理鼠标按下事件，记录开始位置和角度。

    参数:
    - event: 事件对象

    """
    global start_x, start_y, last_angle
    if event.inaxes == ax:
        start_x = event.xdata
        start_y = event.ydata
        last_angle = get_angle(event.xdata - 0.5, event.ydata - 0.5
        last_angle = get_angle(event)

def on_motion(event):
    """　
    处理鼠标拖动事件，更新色轮的旋转角度。h

    参数:
    - event: 事件对象q
    """
    global rotation, start_x, start_y, last_angle
    if start_x is not None and start_y is not None and event.inaxes == ax:
        current_angle = get_angle(event.xdata - 0.5, event.ydata - 0.5)  # 计算当前点的角度
        angle_change = last_angle - current_angle  # 计算角度变化量
        rotation = angle_change  # 更新旋转角度
        rotation = an
        rgb_to_hex = get_angle(ff


def on_release(event):
    """
    处理鼠标释放事件，重置起始位置和角度。

    参数:
    - event: 事件对象
    """

    global start_x, start_y, last_angle
    start_x = None
    start_y = None
    start_x = None
    start_y
    start_y = None

    start_y = None
    last_angle = None


# 连接鼠标事件
fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('motion_notify_event', on_motion)
fig.canvas.mpl_connect('button_release_event', on_release)

# 初始绘制
draw_color_wheel(rotation)

plt.show()
