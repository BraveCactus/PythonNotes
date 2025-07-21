import multiprocessing

"""
Как работает Lock?
Если процесс захватывает (acquire()) блокировку, другие процессы не могут войти в защищённый участок кода, пока она не будет освобождена (release()).

Гарантирует, что только один процесс изменяет общий ресурс (например, переменную в multiprocessing.Value).
"""

def work(proc, lock, shared_value):
    with lock:
        shared_value.value += 1
        print(f"Процесс {proc}: завладел shared_value")
        print(f"Процесс {proc}: увеличил shared_value")

if __name__ == "__main__":
    shared_value = multiprocessing.Value("i", 0)
    lock = multiprocessing.Lock()

    processes = [multiprocessing.Process(target = work, args = (i, lock, shared_value,)) for i in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()

    print(f"Итоговое значение shared_value: {shared_value.value}")