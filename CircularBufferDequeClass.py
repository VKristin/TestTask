from collections import deque

# Реализация класса с использованием двусторонней очереди
# + Двусторонняя очередь оптимизирована для быстрой вставки и удаления (O(1))
# - Логика управления буфером сложнее

class CircularBufferDeque:
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)

    # Добавление элемента
    def enqueue(self, item):
        self.buffer.append(item)

    # Извлечение элемента
    def dequeue(self):
        if len(self.buffer) == 0:
            raise IndexError("Buffer is empty")
        return self.buffer.popleft()