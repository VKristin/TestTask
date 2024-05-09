import CircularBufferListClass as ListFifo
import CircularBufferDequeClass as DequeFifo
'''
Вопрос №2

На языке Python написать минимум по 2 класса реализовывающих циклический буфер FIFO.
Объяснить плюсы и минусы каждой реализации.

Оценивается:
- Полнота и качество реализации
- Оформление кода
- Наличие сравнения и пояснения по быстродействию
'''

def RunListFifo():
    print("Run list FIFO")
    buffer = ListFifo.CircularBufferList(5)
    buffer.enqueue(1)
    buffer.enqueue(2)
    buffer.enqueue(3)
    buffer.enqueue(4)
    buffer.enqueue(5)
    print(f"Dequeue from list FIFO = {buffer.dequeue()}")

def RunDequeFifo():
    print("Run deque FIFO")
    buffer = DequeFifo.CircularBufferDeque(5)
    buffer.enqueue(1)
    buffer.enqueue(2)
    buffer.enqueue(3)
    buffer.enqueue(4)
    buffer.enqueue(5)
    print(f"Dequeue from deque FIFO = {buffer.dequeue()}")

def TryAllFifoClasses():
    RunListFifo()
    RunDequeFifo()