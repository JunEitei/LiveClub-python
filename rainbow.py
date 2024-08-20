#   Author: damao
#   2024-08-17

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.spatial import ConvexHull
import random


def normalize(vectors):
    """将向量归一化为单位向量
    参数:
        vectors (numpy.ndarray): 需要归一化的向量数组，形状为 (n, 3)。
    返回:
        numpy.ndarray: 归一化后的向量数组，形状与输入相同。
    """
    norms = np.linalg.norm(vectors, axis=1)  # 计算每个向量的范数（长度）
    return vectors / norms[:, np.newaxis]  # 将向量除以其范数，得到单位向量


def subdivide_faces(vertices, faces, depth=1):
    """细分面，以便获得更平滑的模型
    参数:
        vertices (numpy.ndarray): 顶点坐标数组，形状为 (n, 3)。
        faces (numpy.ndarray): 面的索引数组，每个面由三个顶点索引构成。
        depth (int): 细分的深度，表示每个面被细分的次数。
    返回:
        tuple: 细分后的顶点和面，形状与输入相同。
    """
    for _ in range(depth):
        new_faces = []  # 存储细分后的新面
        midpoint_cache = {}  # 缓存中点的字典，以避免重复计算

        for tri in faces:
            midpoints = []  # 存储当前三角形各边的中点
            for i in range(3):
                edge = tuple(sorted([tri[i], tri[(i + 1) % 3]]))  # 当前边的两个顶点
                if edge not in midpoint_cache:
                    # 计算边的中点，并将其添加到顶点列表中
                    midpoint = (vertices[edge[0]] + vertices[edge[1]]) / 2
                    midpoint_cache[edge] = len(vertices)
                    vertices = np.vstack([vertices, midpoint])
                midpoints.append(midpoint_cache[edge])
            # 创建细分后的四个新面，并将其添加到新面列表中
            new_faces.extend([
                [tri[0], midpoints[0], midpoints[2]],
                [tri[1], midpoints[1], midpoints[0]],
                [tri[2], midpoints[2], midpoints[1]],
                midpoints
            ])
        faces = np.array(new_faces)  # 更新面列表
    return vertices, faces


def merge_to_hexagons(vertices, faces):
    """将能够合并成六边形的面合并成六边形
    参数:
        vertices (numpy.ndarray): 顶点坐标数组，形状为 (n, 3)。
        faces (numpy.ndarray): 面的索引数组，每个面由三个顶点索引构成。
    返回:
        tuple: 合并后的顶点和面，形状与输入相同。
    """
    new_faces = []  # 存储合并后的面
    used_faces = set()  # 记录已经处理过的面

    for i, face in enumerate(faces):
        if i in used_faces:
            continue  # 如果该面已经处理过，则跳过

        # 查找与当前三角形共享两条边的面
        adj_faces = []
        for j, other_face in enumerate(faces):
            if j != i and len(set(face) & set(other_face)) == 2:
                adj_faces.append(j)

        if len(adj_faces) >= 2:
            # 如果找到至少两个相邻面，则将它们与当前面合并成六边形
            hexagon = list(set(face) | set(faces[adj_faces[0]]) | set(faces[adj_faces[1]]))
            new_faces.append(hexagon)
            used_faces.update([i, adj_faces[0], adj_faces[1]])  # 更新已处理面集合
        else:
            # 否则保留当前三角形
            new_faces.append(face)

    return vertices, new_faces


# 正二十面体顶点
phi = (1 + np.sqrt(5)) / 2  # 黄金比例，用于计算顶点位置
vertices = np.array([
    [-1, phi, 0],  # 顶点1
    [1, phi, 0],  # 顶点2
    [-1, -phi, 0],  # 顶点3
    [1, -phi, 0],  # 顶点4
    [0, -1, phi],  # 顶点5
    [0, 1, phi],  # 顶点6
    [0, -1, -phi],  # 顶点7
    [0, 1, -phi],  # 顶点8
    [phi, 0, -1],  # 顶点9
    [phi, 0, 1],  # 顶点10
    [-phi, 0, -1],  # 顶点11
    [-phi, 0, 1]  # 顶点12
])
vertices = normalize(vertices)  # 归一化以使顶点在单位球上

# 创建截角二十面体
hull = ConvexHull(vertices)  # 计算顶点的凸包
faces = hull.simplices  # 获取凸包的面

# 细分面以获得更平滑的球体近似
vertices, faces = subdivide_faces(vertices, faces, depth=3)  # 细分面
vertices = normalize(vertices)  # 再次归一化，以确保新顶点在单位球上

# 绘制球体
fig = plt.figure()  # 创建绘图对象
ax = fig.add_subplot(111, projection='3d')  # 创建3D坐标轴

# 为每个面分配一个随机颜色
colors = [plt.cm.jet(random.random()) for _ in faces]

# 绘制多边形
for face, color in zip(faces, colors):
    poly = Poly3DCollection([vertices[face]], color=color, alpha=0.8, edgecolor='k')
    ax.add_collection3d(poly)  # 将多边形添加到3D图形中

# 设置坐标轴范围和比例
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_box_aspect([1, 1, 1])  # 保持坐标轴比例

plt.show()  # 显示图形
