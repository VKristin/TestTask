'''
Вопрос №1

На языке Python написать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному
по функциональности, но отличен по своей сути. Объяснить плюсы и минусы обеих реализаций.
'''

# Запуск методов
def TryAllOfMethodsIsEven():
    # Even
    print(f"Example IsEven(6) = {IsEven(6)}")
    print(f"Bit IsEven(6) = {IsEvenBit(6)}")
    # Odd
    print(f"Example IsEven(7) = {IsEven(6)}")
    print(f"Bit IsEven(7) = {IsEvenBit(6)}")

# Код из примера
# + Код простой и понятный
# - Может быть затратной из-за деления
def IsEven(value):
    return value % 2 == 0

# Собственная реализация
# + Побитовые операции быстрее
# - Код сложнее для понимания
def IsEvenBit(value):
    return value & 1 == 0