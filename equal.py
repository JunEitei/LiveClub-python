#   Author: damao
#   2024-08-17

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定義螺旋的參數
a = 1  # 螺旋的初始半徑
b = 0.1  # 控制螺旋的擴展速度，值越大，螺旋擴展得越快

# 設置角度範圍
theta = np.linspace(0, 4 * np.pi, 1000)  # 從 0 到 4π，生成 1000 個數據點

# 計算 r 的值
r = a * np.exp(b * theta)  # r 隨著 theta 增大而指數增長

# 計算 x, y 和 z 坐標
x = r * np.cos(theta)  # x 坐標根據 r 和 theta 的餘弦值計算
y = r * np.sin(theta)  # y 坐標根據 r 和 theta 的正弦值計算
z = 3 * theta  # z 坐標直接使用 theta 的線性變換

# 畫圖
fig = plt.figure(figsize=(10, 8))  # 創建一個 10x8 英寸的圖形窗口
ax = fig.add_subplot(111, projection='3d')  # 添加一個 3D 坐標軸
ax.plot(x, y, z, label='等角螺線')  # 在 3D 坐標軸上繪製等角螺線
ax.set_title('立體等角螺線')  # 設置圖形的標題
ax.set_xlabel('X 軸')  # 設置 X 軸標籤
ax.set_ylabel('Y 軸')  # 設置 Y 軸標籤
ax.set_zlabel('Z 軸')  # 設置 Z 軸標籤
ax.grid(True)  # 顯示網格線以方便查看坐標
ax.legend()  # 顯示圖例

plt.show()  # 顯示繪製的螺旋圖形
