import threading
import queue
import time

def producer(q):
    for i in range(5):
        # time.sleep(0.5)
        q.put(i)
        print(f"Producer поместил элемент {i} в очередь")
    q.put(None)

def consumer(q):
    while True:
        item = q.get()
        if item == None:
            print(f"Consumer встретил None в очереди")
            break        
        print(f"Consumer обработал элемент {item} из очереди")
        # time.sleep(0.5)

if __name__ == "__main__":
    q = queue.Queue()
    producer = threading.Thread(target=producer, args=(q,))
    consumer = threading.Thread(target=consumer, args=(q,))

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
