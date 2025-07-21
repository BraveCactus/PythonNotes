import multiprocessing
import time

TOTALTIME = 4

currentTime = 0

def work(proc: int, queue_get, queue_send):
    """
    Имитирует работу процесса, получает и передает сообщения другим процессам
    params:
        proc: номер процесса
        queue_get: очередь для приема сообщений
        queue_send: очередь для отправки сообщений
    """
    global currentTime
    print(f"Процесс {proc}: currentTime = {currentTime}")
    while True:
        if not queue_get.empty():
            get_message = queue_get.get()
            print(f"Процесс {proc} получил сообщение '{get_message}'")
            time.sleep(0.5)
            currentTime += 1
            send_message = f"Привет от процесса {proc}"
            queue_send.put(send_message)
            print(f"Процесс {proc} отправил сообщение")
            print(f"Процесс {proc}: currentTime = {currentTime}")
            if(currentTime >= TOTALTIME):
                print(f"Процесс {proc}: currentTime = {currentTime}, поэтому завершается")
                break       


if __name__ == "__main__":
    queue1 = multiprocessing.Queue()
    queue2 = multiprocessing.Queue()
    queue3 = multiprocessing.Queue()

    processes =[
        multiprocessing.Process(target = work, args=(1, queue1, queue2)),
        multiprocessing.Process(target = work, args=(2, queue2, queue3)),
        multiprocessing.Process(target = work, args=(3, queue3, queue1))
    ]

    initial_message = "Start!"
    queue1.put(initial_message)

    for p in processes:
        p.start()

    for p in processes:
        p.join()    
    
    print(f"Все процессы завершились")
    
 
