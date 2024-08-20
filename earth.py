#   Author: damao
#   2024-08-17

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建经度和纬度数据
phi = np.linspace(0, np.pi, 30)  # 纬度范围：0 到 π
theta = np.linspace(0, 2 * np.pi, 30)  # 经度范围：0 到 2π

# 创建球面网格，将经度和纬度组合成一个 2D 网格
phi, theta = np.meshgrid(phi, theta)

# 定义球的半径
r = 1  # 球的半径为 1

# 计算球面坐标
x = r * np.sin(phi) * np.cos(theta)
y = r * np.sin(phi) * np.sin(theta)
z = r * np.cos(phi)

# 创建图形
fig = plt.figure(figsize=(8, 8))  # 创建一个 8x8 英寸的图形窗口
ax = fig.add_subplot(111, projection='3d')  # 添加一个 3D 坐标轴

# 绘制球面
# 使用 plot_surface 方法在 3D 坐标轴上绘制球面
# cmap 指定颜色映射，edgecolor 指定边界线颜色，alpha 控制透明度
surf = ax.plot_surface(x, y, z, facecolors=plt.cm.viridis((phi - phi.min()) / (phi.max() - phi.min())),
                       edgecolor='k', alpha=0.8)

# 绘制经度线
# 遍历每个经度，绘制对应的经度线
for t in theta[0, :]:
    ax.plot(r * np.sin(phi[:, 0]) * np.cos(t),
            r * np.sin(phi[:, 0]) * np.sin(t),
            r * np.cos(phi[:, 0]), color='k', linewidth=0.5)

# 绘制纬度线
# 遍历每个纬度，绘制对应的纬度线
for p in phi[:, 0]:
    ax.plot(r * np.sin(p) * np.cos(theta[0, :]),
            r * np.sin(p) * np.sin(theta[0, :]),
            r * np.cos(p), color='k', linewidth=0.5)

# 设置图形标题和坐标轴标签
ax.set_xlabel('X 轴')  # 设置 X 轴标签
ax.set_ylabel('Y 轴')  # 设置 Y 轴标签
ax.set_zlabel('Z 轴')  # 设置 Z 轴标签


# 显示图形
plt.show()  # 显示地球仪图形
