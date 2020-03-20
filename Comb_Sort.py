import datetime
import timeit
def comb(data):
	gap = len(data)
	swaps = True
	while gap > 1 or swaps:
		gap = max(1, int(gap / 1.25))  # minimum gap is 1
		swaps = False
		for i in range(len(data) - gap):
			j = i + gap
			if data[i] > data[j]:
				data[i], data[j] = data[j], data[i]
				swaps = True
	return data

# random_list_of_nums = [120, 45, 68, 250, 176]
# random_list_of_text=["skibi","qwe","ythf","pokb"]
# random_list_of_date=[datetime.date(1999, 12, 22), datetime.date(2020, 1, 12), datetime.date(2003, 6, 16)]
#
# class Comb_sort:
# 	def comb_sort(self, array):
# 		gap = len(array)
# 		swaps = True
# 		while gap > 1 or swaps:
# 			gap = max(1, int(gap / 1.25))  # minimum gap is 1
# 			swaps = False
# 			for i in range(len(array) - gap):
# 				j = i + gap
# 				if array[i] > array[j]:
# 					array[i], array[j] = array[j], array[i]
# 					swaps = True
# 		return array

# v=Comb_sort()
# v.comb_sort(random_list_of_nums)
# print(random_list_of_nums)
#
# v.comb_sort(random_list_of_text)
# print(random_list_of_text)
#
# v.comb_sort(random_list_of_date)
# print(random_list_of_date)