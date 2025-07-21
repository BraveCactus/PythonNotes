import threading

def work1():
    """Простая функция имитирующая работу потока"""
    print(f"Выполняется работа!")

def work2(thread):
    """Простая функция имитирующая работу потока"""
    print(f"Поток {thread} выполняет работу")

if __name__ == "__main__":
    thread = threading.Thread(target = work1)
    thread.start()
    thread.join()

    thread = threading.Thread(target = work2, args=(1,))
    thread.start()
    thread.join()