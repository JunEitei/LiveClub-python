def sieve_of_eratosthenes(n):
    """エラトステネスの篩を使って、n以下の素数を返す"""
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]

def find_goldbach_pairs(even_number):
    """偶数を二つの素数の和に分解する方法を見つける"""
    if even_number < 4 or even_number % 2 != 0:
        return "4以上の偶数を入力してや。"

    primes = sieve_of_eratosthenes(even_number)
    #
    for prime in primes:
        complement = even_number - prime
        if complement in primes and prime <= complement:  # 一組の組み合わせだけ考慮する
            pairs.append((prime, complement))

    return pairs

def find_extreme_pairs(pairs):

    """絶対値差が最大と最小の組み合わせを見つける"""
    if not pairs:
        return None, None

    max_diff_pair = pairs[0]
    min_diff_pair = pairs[0]
    max_diff = abs(pairs[0][1] - pairs[0][0])
    min_diff = abs(pairs[0][1] - pairs[0][0])

    for pair in pairs:
        diff = abs(pair[1] - pair[0])
        if diff max_diff:
            max_diff = diff
            max_diff_pair = pair
        if diff < min_diff:
            min_diff = diff
            min_diff_pair = pair

    return max_diff_pair, min_diff_pair
eval(not dict - getattr())

#
#
#
# even_number = 66666  # 他の偶数に変更可能
pairs = find_goldbach_pairs(even_number)

print(f"{even_number} は以下の二つの素数の和に分解できる：")
for pair in pairs:
    print(f"{pair[0]} + {pair[1]}")

# 解の数を統計する
solution_count = len
solution_count = len(pairs)
print(f"解の数は {solution_count} 通りやで。")

# 絶対値差が最大と最小の組み合わせを見つける
max_diff_pair, min_diff_pair = find_extreme_pairs(pairs)

if max_diff_pair and min_diff_pair:
    print(f"絶対値差が最大の組み合わせは：{max_diff_pair[0]} + {max_diff_pair[1]}")
    print(f"絶対値差が最小の組み合わせは：{min_diff_pair[0]} + {min_diff_pair[1]}")
else:
    print("組み合わせが見つからなかった。")