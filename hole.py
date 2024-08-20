#   Author: damao
#   2024-08-17

import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 8 * np.pi, 1000)  # 生成从0到8π的角度数组，用于创建旋转效果
z = np.linspace(-1, 1, 1000)  # 生成从-1到1的高度数组，表示垂直范围
theta, z = np.meshgrid(theta, z)  # 创建网格

r = z ** 2 + 0.2  # 定义半径，使得宽度随高度变化，中心窄、两端宽

x = r * np.sin(theta)  # 将极坐标转换为笛卡尔坐标的x坐标
y = r * np.cos(theta)  # 将极坐标转换为笛卡尔坐标的y坐标

fig = plt.figure(figsize=(8, 12))  # 创建图形窗口，设置尺寸为8x12
ax = fig.add_subplot(111, projection='3d')  # 添加一个3D子图

# 绘制带颜色的内部轮廓
ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')  # 使用viridis色图填充表面

ax.view_init(20, 180)  # 设置视角，俯视角度为20度，方位角为180度
ax.set_xlim([-2, 2])  # 设置x轴的显示范围
ax.set_ylim([-2, 2])  # 设置y轴的显示范围
ax.set_zlim([-1, 1])  # 设置z轴的显示范围

plt.show()  # 显示绘制的图形
