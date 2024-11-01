def is_prime(num):
    """判断一个数字是否为素数"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def goldbach_conjecture(limit):
    """输出100以下的偶数分解成两个素数的结果"""
    primes = [i for i in range(limit) if is_prime(i)]
    results = {}

    for even in range(4, limit + 1, 2):
        pairs = []
        for p in primes:
            if p > even // 2:  # 只考虑不重复的组合
                break
            if (even - p) in primes:
                pairs.append(f"{p} + {even - p}")
        results[even] = " や ".join(pairs)

    for even, pairs in results.items():
        print(f"> {even} = {pairs}")

# 调用函数，输出结果
goldbach_conjecture(100)