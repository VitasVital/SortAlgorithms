import datetime
def radixsort(A):
    length = len(str(max(A)))
    rang = 10
    for i in range(length):
        B = [[] for k in range(rang)] #список длины range, состоящий из пустых списков
        for x in A:
            figure = x // 10**i % 10
            B[figure].append(x)
        A = []
        for k in range(rang):
            A = A + B[k]
    return A

# random_list_of_nums = [120, 45, 68, 250, 176]
# random_list_of_text=["skibi","qwe","ythf","pokb"]
# random_list_of_date=[datetime.date(1999, 12, 22), datetime.date(2020, 1, 12), datetime.date(2003, 6, 16)]
#
# class Radix_sort:
#     def radix_sort(self, array):
#         length = len(str(max(array)))
#         rang = 10
#         for i in range(length):
#             B = [[] for k in range(rang)]  # список длины range, состоящий из пустых списков
#             for x in array:
#                 figure = x // 10 ** i % 10
#                 B[figure].append(x)
#             array = []
#             for k in range(rang):
#                 array = array + B[k]
#         return array
#
# v=Radix_sort()
# random_list_of_nums = v.radix_sort(random_list_of_nums)
# print(random_list_of_nums)