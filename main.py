import random

import firstTask
import secondTask
import thirdTask

if __name__ == '__main__':
    # Try first task
    print("Задание 1:")
    firstTask.TryAllOfMethodsIsEven()
    print()

    # Try second task
    print("Задание 2:")
    secondTask.TryAllFifoClasses()
    print()

    # Try third task
    print("Задание 3:")
    arr = [random.randint(1, 1000) for _ in range(10)]
    print(f"Исходный массив:\n{arr}")
    print(f"Отсортированный массив:\n{thirdTask.merge_sort(arr)}")

