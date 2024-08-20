#   Author: damao
#   2024-08-17

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建参数
theta = np.linspace(0, 2 * np.pi, 10)  # 环形参数，生成从0到2π的角度数组，共10个点
w = np.linspace(-0.5, 0.5, 30)  # 宽度参数，生成从-0.5到0.5的数组，共30个点
theta, w = np.meshgrid(theta, w)  # 生成网格坐标，用于计算莫比乌斯带上的点

# 莫比乌斯带的参数方程
R = 1  # 半径，控制莫比乌斯带的整体大小
x = (R + w * np.cos(theta / 2)) * np.cos(theta)  # 计算x坐标
y = (R + w * np.cos(theta / 2)) * np.sin(theta)  # 计算y坐标
z = w * np.sin(theta / 2)  # 计算z坐标

# 绘制莫比乌斯带
fig = plt.figure()  # 创建一个新的图形窗口
ax = fig.add_subplot(111, projection='3d')  # 添加一个3D子图
ax.plot_surface(x, y, z, cmap='viridis')  # 绘制莫比乌斯带的表面，并使用'viridis'颜色映射

# 设置图形的标签
ax.set_xlabel('X')  # 设置X轴标签
ax.set_ylabel('Y')  # 设置Y轴标签
ax.set_zlabel('Z')  # 设置Z轴标签

plt.show()  # 显示绘制的图形
