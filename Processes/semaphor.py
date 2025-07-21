import multiprocessing
import time

def worker(sem, id):
    with sem:
        print(f"Процесс {id} начал работу")
        time.sleep(2)
        print(f"Процесс {id} завершил работу")

if __name__ == "__main__":
    sem = multiprocessing.Semaphore(2)  # Не более 2 процессов одновременно
    processes = [multiprocessing.Process(target=worker, args=(sem, i)) 
                for i in range(4)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()