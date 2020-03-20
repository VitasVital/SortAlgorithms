import datetime
# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i, что является индексом в arr[]. n - размер кучи
def heapify(arr, n, i):
    largest = i # Initialize largest as root
    l = 2 * i + 1   # left = 2*i + 1
    r = 2 * i + 2   # right = 2*i + 2

  # Проверяем существует ли левый дочерний элемент больший, чем корень
    if l < n and arr[i] < arr[l]:
        largest = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i] # свап

        # Применяем heapify к корню.
        heapify(arr, n, largest)

# Основная функция для сортировки массива заданного размера
def heapSort(arr):
    n = len(arr)

    # Построение max-heap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] # свап
        heapify(arr, i, 0)

# random_list_of_nums = [120, 45, 68, 250, 176]
# random_list_of_text=["skibi","qwe","ythf","pokb"]
# random_list_of_date=[datetime.date(1999, 12, 22), datetime.date(2020, 1, 12), datetime.date(2003, 6, 16)]
#
# class Heap_sort:
#     def heapify(arr, n, i):
#         largest = i
#         l = 2 * i + 1
#         r = 2 * i + 2
#         if l < n and arr[i] < arr[l]:
#             largest = l
#         if r < n and arr[largest] < arr[r]:
#             largest = r
#         if largest != i:
#             arr[i], arr[largest] = arr[largest], arr[i]
#             heapify(arr, n, largest)
#     def heap_sort(self, array):
#         n = len(array)
#         for i in range(n, -1, -1):
#             heapify(array, n, i)
#         for i in range(n - 1, 0, -1):
#             array[i], array[0] = array[0], array[i]
#             heapify(array, i, 0)
#
# v=Heap_sort()
# v.heap_sort(random_list_of_nums)
# print(random_list_of_nums)
#
# v.heap_sort(random_list_of_text)
# print(random_list_of_text)
#
# v.heap_sort(random_list_of_date)
# print(random_list_of_date)