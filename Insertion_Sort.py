import datetime
def insertion(data):
	for i in range(len(data)):
		j = i - 1
		key = data[i]
		while data[j] > key and j >= 0:
			data[j + 1] = data[j]
			j -= 1
		data[j + 1] = key
	return data

# random_list_of_nums = [120, 45, 68, 250, 176]
# random_list_of_text=["skibi","qwe","ythf","pokb"]
# random_list_of_date=[datetime.date(1999, 12, 22), datetime.date(2020, 1, 12), datetime.date(2003, 6, 16)]
#
# insertion(random_list_of_nums)
# print(random_list_of_nums)
#
# insertion(random_list_of_text)
# print(random_list_of_text)
#
# insertion(random_list_of_date)
# print(random_list_of_date)