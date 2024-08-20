#   Author: damao
#   2024-08-17

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.spatial import ConvexHull


# 函数 normalize：将输入的向量归一化，使其长度为 1
def normalize(vectors):
    """将向量归一化为单位向量"""
    norms = np.linalg.norm(vectors, axis=1)  # 计算每个向量的范数（长度）
    return vectors / norms[:, np.newaxis]  # 将每个向量除以其范数，得到单位向量


# 函数 subdivide_faces：将三角形面细分为更小的三角形面
def subdivide_faces(vertices, faces, depth=1):
    """细分面"""
    for _ in range(depth):  # 根据给定的深度重复细分过程
        new_faces = []  # 用于存储新的细分面
        midpoint_cache = {}  # 缓存中点，避免重复计算
        for tri in faces:  # 遍历每一个面（三角形）
            midpoints = []  # 用于存储三条边的中点
            for i in range(3):  # 每个三角形有三条边
                edge = tuple(sorted([tri[i], tri[(i + 1) % 3]]))  # 取当前边的两个顶点，排序后作为字典键
                if edge not in midpoint_cache:  # 如果这个边的中点未计算过
                    midpoint = (vertices[edge[0]] + vertices[edge[1]]) / 2  # 计算中点的坐标
                    midpoint_cache[edge] = len(vertices)  # 将中点加入缓存并记录它在顶点列表中的索引
                    vertices = np.vstack([vertices, midpoint])  # 将中点加入顶点列表
                midpoints.append(midpoint_cache[edge])  # 将中点的索引加入中点列表
            # 使用原顶点和中点创建新的细分面
            new_faces.extend([
                [tri[0], midpoints[0], midpoints[2]],  # 创建新的三角形面
                [tri[1], midpoints[1], midpoints[0]],  # 创建新的三角形面
                [tri[2], midpoints[2], midpoints[1]],  # 创建新的三角形面
                midpoints  # 中间的三角形面
            ])
        faces = np.array(new_faces)  # 更新 faces 列表为新细分的面
    return vertices, faces  # 返回更新后的顶点列表和面列表


# 定义正二十面体的顶点，使用黄金比例 phi 计算
phi = (1 + np.sqrt(5)) / 2  # 黄金比例
vertices = np.array([  # 正二十面体的 12 个顶点坐标
    [-1, phi, 0],
    [1, phi, 0],
    [-1, -phi, 0],
    [1, -phi, 0],
    [0, -1, phi],
    [0, 1, phi],
    [0, -1, -phi],
    [0, 1, -phi],
    [phi, 0, -1],
    [phi, 0, 1],
    [-phi, 0, -1],
    [-phi, 0, 1]
])
vertices = normalize(vertices)  # 将顶点归一化，使其位于单位球的表面上

# 使用 scipy.spatial.ConvexHull 函数计算截角二十面体的面
hull = ConvexHull(vertices)  # 计算包围这些顶点的凸包（Convex Hull）
faces = hull.simplices  # 获取凸包的每个面（由顶点索引组成的三角形面）

# 对截角二十面体进行细分，以获得更平滑的球体近似
vertices, faces = subdivide_faces(vertices, faces, depth=3)  # 细分两次
vertices = normalize(vertices)  # 再次将细分后的顶点归一化到单位球的表面

# 绘制球体
fig = plt.figure()  # 创建一个新的绘图窗口
ax = fig.add_subplot(111, projection='3d')  # 添加 3D 子图

# 绘制每个多边形面
for face in faces:  # 遍历每个细分后的面
    poly = Poly3DCollection([vertices[face]], color='cyan', alpha=0.5, edgecolor='r')  # 创建多边形集合，颜色为青色，边缘为红色
    ax.add_collection3d(poly)  # 将多边形添加到 3D 图中

# 设置坐标轴范围，以确保图形居中显示且比例正确
ax.set_xlim([-1, 1])  # 设置 x 轴范围
ax.set_ylim([-1, 1])  # 设置 y 轴范围
ax.set_zlim([-1, 1])  # 设置 z 轴范围
ax.set_box_aspect([1, 1, 1])  # 保持 x, y, z 三个方向的比例相同

plt.show()  # 显示绘制的图形
