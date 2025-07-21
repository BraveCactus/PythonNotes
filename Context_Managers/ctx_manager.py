from contextlib import contextmanager



class Resourse:
    def __init__(self):
        self.opened = False

    def open(self, *args):
        print(f"Resours was open with args {args}")
        self.opened = True

    def close(self):
        print("Resourse was closed")
        self.opened = False

    def action(self):
        print("Doing smth")

    def __del__(self):
        if self.opened:
            print("Memoty leak detected! The Resourse was not close!")

"""Первый способ создания контекстного менеджера (через декоратор)"""
@contextmanager
def open_resourse(*args):
    resourse = None
    try:
        resourse = Resourse()
        resourse.open(*args)
        yield resourse
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        if resourse.opened:
            resourse.close()

"""Второй способ создания контекстного менеджера (через класс)"""
class ResourseWorker:
    def __init__(self, *args):
        self.args = args
        self.resourse = None
    
    def __enter__(self):
        self.resourse = Resourse()
        self.resourse.open(*self.args)
        return self.resourse
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.resourse.opened:
            self.resourse.close()


if __name__ == "__main__":
    with ResourseWorker(1, 2, 4) as res:
        res.action()
        # raise ValueError("wefg")