import multiprocessing

def increment(proc, shared_value):
    shared_value.value += 1
    print(f"Процесс {proc}: добавил 1")

if __name__ == "__main__":
    counter = multiprocessing.Value("i", 0)
    processes = [multiprocessing.Process(target = increment, args = (_, counter,)) for _ in range(5)] 

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print(f"Итоговое значение counter: {counter.value}")
