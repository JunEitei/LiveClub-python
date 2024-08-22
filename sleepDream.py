import threading
import time


def sleep_sort(n, stop_event):
    # 檢查是否需要停止，如果沒有停止則繼續休眠
    if not stop_event.is_set():
        time.sleep(n / 1000)
        if not stop_event.is_set():  # 在打印之前再次檢查停止標誌
            print(n, end=' ')


def insertion_sort(arr, stop_event):
    for i in range(1, len(arr)):
        if stop_event.is_set():  # 如果排序已完成，停止其他排序
            return
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    stop_event.set()  # 排序完成，設置停止標誌
    print("\n插入排序後的列表:", arr)


def bubble_sort(arr, stop_event):
    n = len(arr)
    for i in range(n):
        if stop_event.is_set():  # 如果排序已完成，停止其他排序
            return
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    stop_event.set()  # 排序完成，設置停止標誌
    print("\n冒泡排序後的列表:", arr)


if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9]
    stop_event = threading.Event()  # 創建一個停止事件

    threads = [
        threading.Thread(target=sleep_sort, args=(numbers[0], stop_event)),
        threading.Thread(target=sleep_sort, args=(numbers[1], stop_event)),
        threading.Thread(target=sleep_sort, args=(numbers[2], stop_event)),
        threading.Thread(target=sleep_sort, args=(numbers[3], stop_event)),
        threading.Thread(target=sleep_sort, args=(numbers[4], stop_event)),
        threading.Thread(target=insertion_sort, args=(numbers.copy(), stop_event)),  # 插入排序線程
        threading.Thread(target=bubble_sort, args=(numbers.copy(), stop_event)),  # 冒泡排序線程
    ]

    # 啟動所有線程
    for t in threads:
        t.start()

    # 等待所有線程完成
    for t in threads:
        t.join()

    print("\n所有線程已完成。")
