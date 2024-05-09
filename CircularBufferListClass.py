# Реализация класса с использованием списка
# + Простота реализации
# - При удалении старых элементов необходим сдвиг всех оставшихся
#   элементов сложностью O(n)
# - Вставка также может потребовать O(n) операций
class CircularBufferList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.size = 0
        self.head = 0
        self.tail = 0

    # Добавление эелемента
    def enqueue(self, item):
        if self.size == self.capacity:
            # Буфер полон, удаляем самый старый элемент
            self.dequeue()
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    # Извлечение элемента
    def dequeue(self):
        if self.size == 0:
            raise IndexError("Buffer is empty")
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item


