import threading  # 引入 threading 模組來支持多線程
import time  # 引入 time 模組來使用 sleep 函數


def sleep_sort(n):
    # 讓線程休眠 n 毫秒（將 n 除以 1000 以轉換為秒）
    time.sleep(n / 1000)
    # 休眠結束後輸出該數字
    print(n, end=' ')


if __name__ == "__main__":
    # 定義待排序數組
    numbers = [1, 3, 5, 7, 9]
    # 為數組中的每個數字創建一個線程
    threads = [threading.Thread(target=sleep_sort, args=(n,)) for n in numbers]
    # 在創建線程的同時啟動線程並等待線程完成
    [t.start() or t.join() for t in threads]