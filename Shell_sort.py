import datetime
def shell(seq):
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq):
            while i >= inc and seq[i - inc] > el:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)

# random_list_of_nums = [120, 45, 68, 250, 176]
# random_list_of_text=["skibi","qwe","ythf","pokb"]
# random_list_of_date=[datetime.date(1999, 12, 22), datetime.date(2020, 1, 12), datetime.date(2003, 6, 16)]
#
# class Shell_sort:
#     def shell_sort(self, array):
#         inc = len(array) // 2
#         while inc:
#             for i, el in enumerate(array):
#                 while i >= inc and array[i - inc] > el:
#                     array[i] = array[i - inc]
#                     i -= inc
#                 array[i] = el
#             inc = 1 if inc == 2 else int(inc * 5.0 / 11)
#
# v=Shell_sort()
# v.shell_sort(random_list_of_nums)
# print(random_list_of_nums)
#
# v.shell_sort(random_list_of_text)
# print(random_list_of_text)
#
# v.shell_sort(random_list_of_date)
# print(random_list_of_date)