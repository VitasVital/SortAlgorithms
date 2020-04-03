import datetime
def bubble(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                buff = array[j]
                array[j] = array[j+1]
                array[j+1] = buff

# random_list_of_nums = [120, 45, 68, 250, 176]
# random_list_of_text=["skibi","qwe","ythf","pokb"]
# random_list_of_date=[datetime.date(1999, 12, 22), datetime.date(2020, 1, 12), datetime.date(2003, 6, 16)]
#
# bubble(random_list_of_nums)
# print(random_list_of_nums)
#
# bubble(random_list_of_text)
# print(random_list_of_text)
#
# bubble(random_list_of_date)
# print(random_list_of_date)