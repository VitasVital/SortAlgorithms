import datetime

def partition(nums, low, high):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

# random_list_of_nums = [120, 45, 68, 250, 176]
# random_list_of_text=["skibi","qwe","ythf","pokb"]
# random_list_of_date=[datetime.date(1999, 12, 22), datetime.date(2020, 1, 12), datetime.date(2003, 6, 16)]
#
# class Quick_sort:
#     def partition(self, nums, low, high):
#         pivot = nums[(low + high) // 2]
#         i = low - 1
#         j = high + 1
#         while True:
#             i += 1
#             while nums[i] < pivot:
#                 i += 1
#             j -= 1
#             while nums[j] > pivot:
#                 j -= 1
#             if i >= j:
#                 return j
#             nums[i], nums[j] = nums[j], nums[i]
#
#     def quick_sort(self, array):
#         def _quick_sort(items, low, high):
#             if low < high:
#                 split_index = partition(items, low, high)
#                 _quick_sort(items, low, split_index)
#                 _quick_sort(items, split_index + 1, high)
#         _quick_sort(array, 0, len(array) - 1)
#
# v=Quick_sort()
# v.quick_sort(random_list_of_nums)
# print(random_list_of_nums)
#
# v.quick_sort(random_list_of_text)
# print(random_list_of_text)
#
# v.quick_sort(random_list_of_date)
# print(random_list_of_date)