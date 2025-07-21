import threading

shared_counter = 0
lock = threading.Lock()

def increment(number):
    global shared_counter
    print(f"Поток {number} выполняет работу")
    for _ in range(100):
        with lock:
            shared_counter += 1

if __name__ == "__main__":
    threads = []
    for _ in range(5):
        thr = threading.Thread(target = increment, args = (_,))
        threads.append(thr)
        thr.start()

    for thr in threads:
        thr.join()

    print(f"Итоговое значение счетчика: {shared_counter}")