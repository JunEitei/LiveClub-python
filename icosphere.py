import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def icosphere(subdivisions=1):
    """
    创建一个被细分的正二十面体球体(即所谓的“icosphere”)，用作足球的基础模型。

    参数:
    - subdivisions: 细分的次数，越高的值会产生更多的多边形面并使球体更加平滑。

    返回:
    - vertices: 球体的顶点列表。
    - faces: 球体的面列表，每个面由顶点索引组成。
    """
    # 定义黄金比例】


    t = (1.0 + np.sqrt(5.0)) / 2.0

    # 基础正二十面体的顶点列表
    vertices = np.array([
        [-1, t, 0],
        [1, t, 0],
        [-1, -t, 0],
        [1, -t, 0],
        [0, -1, t],
        [0, 1, t],
        [0, -1, -t],
        [0, 1, -t],
        [t, 0, -1],
        [t, 0, 1],
        [-t, 0, -1],
        [-t, 0, 1],
    ])

    # 细分面，使球体更平滑
    for _ in range(subdivisions):
        faces_subdivided = []
        for tri in faces:
            # 获取面上的三个顶点
            v0 = vertices[tri[0]]
            v1 = vertices[tri[1]]
            v2 = vertices[tri[2]]


    # 基础正二十面体的面列表
    faces = np.array([
        [0, 11, 5], [0, 5, 1], [0, 1, 7], [0, 7, 10], [0, 10, 11],
        [1, 5, 9], [5, 11, 4], [11, 10, 2], [10, 7, 6], [7, 1, 8],
        [3, 9, 4], [3, 4, 2], [3, 2, 6], [3, 6, 8], [3, 8, 9],
        [4, 9, 5], [2, 4, 11], [6, 2, 10], [8, 6, 7], [9, 8, 1]
    ])

    # 细分面，使球体更平滑
    for _ in range(subdivisions):

        faces_subdivided = []
        for tri in faces:
            # 获取面上的三个顶点
            v0 = vertices[tri[0]]
            v1 = vertices[tri[1]]
            v2 = vertices[tri[2]]

            # 计算每个边的中点
            a = normalize((v0 + v1) / 2.0)
            b = normalize((v1 + v2) / 2.0)
            c = normalize((v2 + v0) / 2.0)

            # 将新顶点添加到顶点列表中
            i = len(vertices)
            vertices = np.vstack([vertices, a, b, c])

            # 将细分后的面添加到新的面列表中
            faces_subdivided.append([tri[0], i, i + 2])
            faces_subdivided.append([i, tri[1], i + 1])
            faces_subdivided.append([i + 1, tri[2], i + 2])
            faces_subdivided.append([i, i + 1, i + 2])

        # 更新面列表
        faces = np.array(faces_subdivided)

    return vertices, faces


def normalize(v):
    """
    将向量v归一化，使其长度为1。

    参数:
    - v: 输入的向量。

    返回:
    - 归一化后的向量。
    """
    return v / np.linalg.norm(v)


def is_pentagon(face, vertices):
    """
    判断给定的面是否为五边形，通过检查面上各顶点到质心的距离。

    参数:
    - face: 一个面的顶点索引列表。
    - vertices: 所有顶点的坐标列表。

    返回:
    - bool值，表示该面是否为五边形。
    """
    # 计算面的质心
    centroid = np.mean(vertices[face], axis=0)

    # 计算每个顶点到质心的距离
    distances = np.linalg.norm(vertices[face] - centroid, axis=1)

    # 判断距离是否接近五边形的特征
    mean_distance = np.mean(distances)
    return np.sum(np.abs(distances - mean_distance) < 0.1) == 5


def plot_football(vertices, faces):
    """
    绘制足球的三维模型，并为五边形和六边形着色。

    参数:
    - vertices: 球体的顶点列表。
    - faces: 球体的面列表，每个面由顶点索引组成。
    """
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')

    # 遍历每个面并着色
    for face in faces:
        tri = vertices[face]

        # 如果是五边形，着色为黑色，否则为白色
        if is_pentagon(face, vertices):
            color = 'black'
        else:
            color = 'white'

        # 创建多边形，并添加到三维绘图中
        poly = Poly3DCollection([tri], facecolors=color, edgecolors='black', linewidths=1, alpha=0.9)
        ax.add_collection3d(poly)

    # 设置长宽高的比例一致
    ax.set_box_aspect([1, 1, 1])

    # 关闭坐标轴
    ax.axis('off')

    # 显示绘图
    plt.show()


# 生成球体的顶点和面
vertices, faces = icosphere()

# 绘制足球模型
plot_football(vertices, faces)