from sympy import isprime  # sympyライブラリからisprime関数をインポートする。この関数は数が素数かどうかを判定する。

def find_goldbach_pairs(even_num):
    # 入力された数が偶数か、4以上かをチェックする。
    if even_num % 2 != 0 or even_num < 4:
        print("4以上の偶数を入力してな。")  # もし違ったら、メッセージを表示する。
        return [], 0  # 空のリストとカウントを返す。

    pairs = []  # 条件に合う素数のペアを保存するためのリスト。
    for p in range(2, even_num):  # 2から指定された偶数まで繰り返す。
        if isprime(p):  # pが素数かどうかをチェックする。
            complement = even_num - p  # pと合計して偶数になる補数を計算する。
            if complement >= p and isprime(complement):  # 補数がp以上で、補数も素数であるかを確認する。
                pairs.append((p, complement))  # この素数ペアをリストに追加する。
    return pairs, len(pairs)  # 見つかった素数のペアとその数を返す。

# ユーザーに偶数を入力させる。
even_number = int(input("偶数を入力してな: "))  # ユーザーに偶数を入力させるメッセージを表示する。
goldbach_pairs, count = find_goldbach_pairs(even_number)  # 関数を呼び出して素数ペアを探す。

# 素数ペアが見つかった場合。
if goldbach_pairs:
    print(f"{even_number}のゴールドバッハのペアは：")  # 結果を表示するメッセージ。
    for pair in goldbach_pairs:  # 見つかったペアを繰り返す。
        print(pair)  # 各素数ペアを表示する。
    print(f"見つかったペアの数: {count}")  # ペアの数を表示する。
else:
    print(f"{even_number}にはペアが見つかりませんでした。")  # ペアが見つからなかった場合のメッセージ。

