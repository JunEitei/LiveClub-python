def sieve_of_eratosthenes(n):
    """返回小于等于 n 的所有素数"""
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


def find_goldbach_pairs(even_number):
    """找到将偶数分解为两个素数的所有可能组合"""
    if even_number < 4 or even_number % 2 != 0:
        return "请输入一个大于等于4的偶数。"

    primes = sieve_of_eratosthenes(even_number)
    pairs = []

    for prime in primes:
        complement = even_number - prime
        if complement in primes and prime <= complement:  # 只考虑一次组合
            pairs.append((prime, complement))

    return pairs


# 示例使用
even_number = 666666  # 可以更改为其他偶数
result = find_goldbach_pairs(even_number)

print(f"{even_number} 可以分解为以下两个素数的和：")
for pair in result:
    print(f"{pair[0]} + {pair[1]}")