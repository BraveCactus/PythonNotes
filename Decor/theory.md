# ****Декораторы в Python****
## **Опр:** 
Декораторы (decorators) в Python — это специальные функции, которые позволяют модифицировать поведение других функций или классов без изменения их исходного кода. Декораторы "оборачивают" целевую функцию, добавляя к ней дополнительную функциональность.

## **Особенности:** 

1) Принцип DRY (Don't Repeat Yourself) - позволяют избежать дублирования кода

2) Модификация поведения - могут изменять работу функций/классов

3) Композиция - несколько декораторов можно применять к одной функции

4) Гибкость - могут принимать параметры

## **Синтаксис декораторов**
### **Базовый синтаксис:**

@decorator
def function():
    pass

### **Эквивалентно:**

def function():
    pass
function = decorator(function)

## **Зачем нужны декораторы?**

1) Логирование - запись информации о вызовах функций

2) Замер времени выполнения

3) Кеширование (мемоизация)

4) Контроль доступа (аутентификация/авторизация)

5) Валидация входных/выходных данных

6) Транзакции (например, в базах данных)

7) Повторные попытки выполнения (retry механизм)