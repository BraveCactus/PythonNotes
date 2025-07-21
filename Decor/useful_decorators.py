from functools import lru_cache
import time
from contextlib import contextmanager

# Декоратор кэширует вычисления (считает значение один рах и запоминает)
@lru_cache
def long_calc():
    time.sleep(3)
    return 42

# Контексный менеджер
@contextmanager
def ctx_manager():
    print("hello")
    yield
    print("end")

if __name__ == "__main__":
    print(long_calc())
    print(long_calc())
    print(long_calc())

    with ctx_manager() as man:
        print("123")
