import matplotlib.pyplot as plt
import numpy as np

def is_prime(n):
    """檢查一個數字是否為質數"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def goldbach_conjecture(n):
    """返回哥德巴赫分拆數的所有組合"""
    primes = [p for p in range(2, n) if is_prime(p)]
    pairs = [(p, n - p) for p in primes if (n - p) in primes]
    return pairs

def plot_goldbach_pairs(max_n):
    """繪製哥德巴赫分拆數的圖譜"""
    x = []
    y1 = []
    y2 = []

    for n in range(4, max_n + 1, 2):  # 哥德巴赫猜想僅適用於偶數
        pairs = goldbach_conjecture(n)
        for p1, p2 in pairs:
            x.append(n)
            y1.append(p1)
            y2.append(p2)

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y1, color='blue', alpha=0.6, label='Prime 1')
    plt.scatter(x, y2, color='red', alpha=0.6, label='Prime 2')
    plt.title("Goldbach's Conjecture Prime Pairs")
    plt.xlabel("Even Number (n)")
    plt.ylabel("Prime Numbers (p1 and p2)")
    plt.xticks(np.arange(4, max_n + 1, step=50))
    plt.yticks(np.arange(0, max(y2) + 1, step=1000000))
    plt.grid()
    plt.legend()
    plt.show()

# 設定最大偶數範圍，然後繪製圖譜
max_n = 1010
plot_goldbach_pairs(max_n)