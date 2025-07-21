import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def work(self):
        print(f"Работа потока {self.name} началась")
        time.sleep(self.delay)
        print(f"Работа потока {self.name} закончилась")


if __name__ == "__main__":
    thr1 = MyThread("thr1", 2)
    thr2 = MyThread("thr2", 3)    

    thr1.start()
    thr2.start()

    thr1.work()
    thr2.work()

    thr1.join()
    thr2.join()

