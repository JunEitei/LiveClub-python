#   Author: damao
#   2024-08-17

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from scipy.spatial import ConvexHull


def fibonacci_sphere(samples=1000):
    """生成球面上的点，使用Fibonacci格子"""
    # 黄金比例 (Phi)
    phi = (1 + np.sqrt(5)) / 2
    indices = np.arange(0, samples, dtype=float) + 0.5  # 生成从0到samples的索引
    theta = 2 * np.pi * indices / phi  # 计算角度theta
    z = 1 - (indices / (samples - 1)) * 2  # z坐标从1到-1
    radius = np.sqrt(1 - z * z)  # 半径基于z计算
    x = radius * np.cos(theta)  # 计算x坐标
    y = radius * np.sin(theta)  # 计算y坐标
    return np.vstack((x, y, z)).T  # 返回点的坐标 (x, y, z) 的数组


def hexagon_faces(center, radius):
    """生成以center为中心、给定半径的六边形的6个面"""
    angles = np.linspace(0, 2 * np.pi, 7)  # 生成从0到2π的角度，分为7个点（包括起始和结束点）
    hexagon = np.vstack([np.cos(angles), np.sin(angles), np.zeros_like(angles)]).T  # 创建六边形的顶点
    hexagon *= radius  # 将顶点扩展到指定的半径
    hexagon += center  # 将顶点平移到指定的中心
    return hexagon[:-1]  # 去掉重复的最后一个点，返回六边形的6个顶点


def generate_hexagonal_mesh_sphere(radius, hexagon_radius, num_points):
    """生成球体的六边形网格"""
    points = fibonacci_sphere(samples=num_points) * radius  # 生成球面上的点并按半径缩放
    hex_faces = []  # 初始化六边形面的列表

    for p in points:  # 对每个球面上的点
        hex_faces.append(hexagon_faces(p, hexagon_radius))  # 在该点生成六边形面并加入列表

    return np.array(hex_faces)  # 返回六边形面列表


def plot_hexagonal_mesh_sphere(hex_faces):
    """绘制六边形网格的球体"""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')  # 创建3D绘图

    # 创建一个面列表用于绘图
    poly3d = Poly3DCollection([face for face in hex_faces], facecolors='cyan', linewidths=0.1, edgecolors='r',
                              alpha=.25)  # 使用面颜色填充
    ax.add_collection3d(poly3d)  # 将多边形集合添加到3D坐标轴中

    # 绘制边缘
    edges = []  # 初始化边缘的列表
    for face in hex_faces:  # 对每个六边形面
        for i in range(len(face)):  # 对每个顶点
            edge = [face[i], face[(i + 1) % len(face)]]  # 连接当前顶点与下一个顶点形成边
            edges.append(edge)  # 将边加入列表

    edge_collection = Line3DCollection(edges, colors='black', linewidths=0.5)  # 创建边缘集合
    ax.add_collection3d(edge_collection)  # 将边缘集合添加到3D坐标轴中

    ax.set_xlabel('X')  # 设置X轴标签
    ax.set_ylabel('Y')  # 设置Y轴标签
    ax.set_zlabel('Z')  # 设置Z轴标签
    plt.show()  # 显示图形


# 参数设置
sphere_radius = 10  # 球体半径
hexagon_radius = 1  # 六边形半径
num_points = 1000  # 生成点的数量

# 生成并绘制六边形网格的球体
hex_faces = generate_hexagonal_mesh_sphere(sphere_radius, hexagon_radius, num_points)  # 生成六边形面
num_hexagons = len(hex_faces)  # 计算六边形的数量
print(f"Number of hexagons: {num_hexagons}")  # 输出六边形数量
plot_hexagonal_mesh_sphere(hex_faces)  # 绘制球体
