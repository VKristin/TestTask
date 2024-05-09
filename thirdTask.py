'''
Вопрос №3

На языке Python предложить алгоритм, который быстрее всего (по процессорным тикам)
отсортирует данный ей массив чисел. Массив может быть любого размера со
случайным порядком чисел (в том числе и отсортированным). Объяснить,
почему вы считаете, что функция соответствует заданным критериям.
'''

# Сортировка слиянием
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Рекурсивно разбиваем массив на две половины
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Рекурсивно сортируем каждую половину
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Объединяем отсортированные половины
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0

    # Сливаем элементы из обеих половин
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # Добавляем оставшиеся элементы, если они есть
    result.extend(left[left_idx:])
    result.extend(right[right_idx:])

    return result

'''
Пояснение:
- Временная сложность сортировки слиянием во всех случаях O(n log n)
- Работает с любым набором данных (отсортированным, неотсортированным) одинаково хорошо
- Алгоритм прост для понимания
'''