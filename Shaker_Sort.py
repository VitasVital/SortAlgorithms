import datetime
def shaker(data):
	up = range(len(data) - 1)
	while True:
		for indices in (up, reversed(up)):
			swapped = False
			for i in indices:
				if data[i] > data[i+1]:
					data[i], data[i+1] =  data[i+1], data[i]
					swapped = True
			if not swapped:
				return data

# random_list_of_nums = [120, 45, 68, 250, 176]
# random_list_of_text=["skibi","qwe","ythf","pokb"]
# random_list_of_date=[datetime.date(1999, 12, 22), datetime.date(2020, 1, 12), datetime.date(2003, 6, 16)]
#
# shaker(random_list_of_nums)
# print(random_list_of_nums)
#
# shaker(random_list_of_text)
# print(random_list_of_text)
#
# shaker(random_list_of_date)
# print(random_list_of_date)