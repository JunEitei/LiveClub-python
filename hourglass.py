#   Author: damao
#   2024-08-17

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定義龍捲風的參數
theta = np.linspace(0, 2 * np.pi, 20)  # 生成从0到2π的角度数组，用于生成圆形横截面
z = np.linspace(-5, 5, 20)  # 生成从-5到5的高度数组，代表沙漏的垂直方向
theta, Z = np.meshgrid(theta, z * z * z)  # 将角度和高度组合成网格，用于生成3D曲面
# Z使用立方函数，使得z的分布更加集中在中心区域，创建更加平滑的形状

# 定義半徑隨 z 的變化，頂部和底部寬，中部窄
R = Z + np.exp(-Z ** 2)  # 计算半径，结合Z和指数衰减函数，使得沙漏的形状有顶部和底部宽，中间窄的特性
# Z作为基础半径，exp(-Z^2)项用于在Z接近0时产生一个较小的附加半径，从而使得中部变窄


# 計算 x 和 y 坐標
X = R * np.cos(theta)  # 通过极坐标转换计算x坐标
Y = R * np.sin(theta)  # 通过极坐标转换计算y坐标

# 畫圖
fig = plt.figure(figsize=(10, 8))  # 创建图形窗口，设置尺寸
ax = fig.add_subplot(111, projection='3d')  # 添加3D子图

# 生成3D曲面图，使用'viridis'颜色映射，边缘颜色设为'none'以使得曲面平滑
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# 設置圖形標題和坐標軸標籤
ax.set_xlabel('X 軸')  # 设置X轴标签
ax.set_ylabel('Y 軸')  # 设置Y轴标签
ax.set_zlabel('Z 軸')  # 设置Z轴标签

plt.show()  # 显示图形
