import numpy as np
import matplotlib.pyplot as plt
from sympy import primerange

# 生成素数
max_n = 1000
primes = list(primerange(2, max_n))

# 准备数据
even_numbers = np.arange(4, max_n + 1, 2)
goldbach_pairs = []

for n in even_numbers:
    pairs = [(p, n - p) for p in primes if p <= n // 2 and (n - p) in primes]
    goldbach_pairs.append(pairs)

# 设置图形
plt.figure(figsize=(12, 8))

# 绘制哥德巴赫彩虹
colors = plt.cm.rainbow(np.linspace(0, 1, len(even_numbers)))

for i, n in enumerate(even_numbers):
    for p1, p2 in goldbach_pairs[i]:
        plt.plot([n, n], [p1, p2], color=colors[i], alpha=0.6)

# 添加标签和标题
plt.title('哥德巴赫彩虹: 偶数及其素数和的组合')
plt.xlabel('偶数 n')
plt.ylabel('素数')
plt.xticks(even_numbers, rotation=90)
plt.grid(True)

# 显示图形
plt.tight_layout()
plt.show()