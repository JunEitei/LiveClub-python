#   Author: damao
#   2024-08-17

import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 8 * np.pi, 1000)  # 生成从0到8π的角度数组，用于创建旋转效果
z = np.linspace(-1, 1, 1000)  # 生成从-1到1的高度数组，表示垂直范围
r = z ** 2 + 0.2  # 定义半径，使得宽度随高度变化，中心窄、两端宽

x = r * np.sin(theta)  # 将极坐标转换为笛卡尔坐标的x坐标
y = r * np.cos(theta)  # 将极坐标转换为笛卡尔坐标的y坐标

fig = plt.figure(figsize=(6, 10))  # 创建图形窗口，设置尺寸为6x10
ax = fig.add_subplot(111, projection='3d')  # 添加一个3D子图
ax.plot(x, y, z, color='blue')  # 绘制龙卷风的3D线条图，颜色为蓝色

ax.view_init(20, 180)  # 设置视角，俯视角度为20度，方位角为180度
ax.set_xlim([-1, 1])  # 设置x轴的显示范围
ax.set_ylim([-1, 1])  # 设置y轴的显示范围
ax.set_zlim([-1, 1])  # 设置z轴的显示范围

ax.axis('off')  # 移除坐标轴，使图像更加干净

plt.show()  # 显示绘制的图形

