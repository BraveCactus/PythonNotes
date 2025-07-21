from typing import Callable
import time
from functools import wraps

"""Базовые декораторы"""

# Пример простого декоратора
def deco(func):
    def wrapper():
        print("Hello")
        func()
    return wrapper  

# Декоратор для подсчета времени выполнения функции
def time_deco(func: Callable):
    def wrapper():
        start = time.time()
        func()
        finish = time.time()
        print(f"Время выполнения: {finish - start}")
    return wrapper

# Универсальный декоратор для функции с любым количеством параметров
def param_time_deco(func: Callable):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        finish = time.time()
        print(f"Время выполнения: {finish - start}")
    return wrapper

# Декоратор с параметром
def uni_deco(limit: int):
    def wrapper(func: Callable):
        def inner(*args, **kwargs):
            nonlocal limit
            if limit == 0:
                print("Нельзы вызвать функцию")
                return             
            res = func(*args, **kwargs)    
            limit -= 1
            print(f"Осталось вызовов: {limit}")
            return res       
        return inner
    return wrapper

"""Допустим нам надо сохданять docstring или название функции после применения декоратора"""

# Декоратор с параметром
def new_uni_deco(limit: int):
    def wrapper(func: Callable):
        @wraps(func)
        def inner(*args, **kwargs):
            nonlocal limit
            if limit == 0:
                print("Нельзы вызвать функцию")
                return             
            res = func(*args, **kwargs)    
            limit -= 1
            print(f"Осталось вызовов: {limit}")
            return res       
        return inner
    return wrapper

@new_uni_deco(2)
def func(sleep_sec: int):
    """Какой-то docstring"""
    time.sleep(sleep_sec)
    return 123

if __name__ == "__main__":    
    print(func.__annotations__)


