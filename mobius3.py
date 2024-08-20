#   Author: damao
#   2024-08-17

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建参数
u = np.linspace(0, 2 * np.pi, 100)  # u参数从0到2π, 分成100个点
v = np.linspace(0, 2 * np.pi, 100)  # v参数从0到2π, 分成100个点
u, v = np.meshgrid(u, v)  # 使用网格生成器创建参数空间

# 克莱因瓶的参数方程
R = 4  # 半径参数，控制克莱因瓶的大小
x = (R + np.cos(u / 2) * np.sin(v) - np.sin(u / 2) * np.sin(2 * v)) * np.cos(u)
y = (R + np.cos(u / 2) * np.sin(v) - np.sin(u / 2) * np.sin(2 * v)) * np.sin(u)
z = np.sin(u / 2) * np.sin(v) + np.cos(u / 2) * np.sin(2 * v)

# 绘制克莱因瓶
fig = plt.figure()  # 创建一个新的图形窗口
ax = fig.add_subplot(111, projection='3d')  # 添加一个3D子图
ax.plot_surface(x, y, z, cmap='viridis')  # 使用‘viridis’颜色映射绘制克莱因瓶表面

# 设置图形的标签
ax.set_xlabel('X')  # 设置X轴标签
ax.set_ylabel('Y')  # 设置Y轴标签
ax.set_zlabel('Z')  # 设置Z轴标签

plt.show()  # 显示绘制的图形
