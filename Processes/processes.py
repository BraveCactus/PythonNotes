import multiprocessing

def work1():
    """Простая функция имитирующая работу процесса"""
    print("Выполняю работу!")

def work2(name):
    """Простая функция имитирующая работу процесса, принимающая параметр"""
    print(f"Привет, {name}!")

def work3(q):
    """Процесс работает с очередью"""
    q.put("Сообщение")
    print("Поместил сообщение в очередь")

def square(x):
    return x * x

if __name__ == "__main__":
    p = multiprocessing.Process(target = work1)
    p.start()
    p.join()

    p = multiprocessing.Process(target = work2, args = ("Аурелиано",))
    p.start()
    p.join()

    q = multiprocessing.Queue()
    p = multiprocessing.Process(target = work3, args=(q,))
    p.start()
    p.join()
    print(q.get())

    # С помощью Pool можно выполнять однотипные действия
    with multiprocessing.Pool(4) as pool:
        result = pool.map(square, [_ for _ in range(1, 5)])
    print(result)

