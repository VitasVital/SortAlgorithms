import Python_Sort
import Merge_Sort
import Comb_Sort
import Heap_Sort
import Quick_Sort
import Radix_Sort
import Shell_sort
import timeit
from Tests.Time_test_rand_string_50000 import Array_rand_string_50000

f1=Array_rand_string_50000.rand_string_50000_100
f2=f1.copy()
f3=f1.copy()
f4=f1.copy()
f5=f1.copy()
f6=f1.copy()
f7=f1.copy()

print("Random array\n",f1,"\n")
t=timeit.Timer(lambda : Python_Sort.python_sort(f1))
print("Python sort ",t.timeit(number = 1))
print(f1,"\n")

t=timeit.Timer(lambda : Merge_Sort.merge_sort(f2))
print("Merge sort",t.timeit(number = 1))
print(f2,"\n")

t=timeit.Timer(lambda : Comb_Sort.comb(f3))
print("Comb sort ",t.timeit(number = 1))
print(f3,"\n")

t=timeit.Timer(lambda : Heap_Sort.heapSort(f4))
print("Heap sort ",t.timeit(number = 1))
print(f4,"\n")

t=timeit.Timer(lambda : Quick_Sort.quick_sort(f5))
print("Quick sort ",t.timeit(number = 1))
print(f5,"\n")

# t=timeit.Timer(lambda : Radix_Sort.radixsort(f6))
# print("Radix sort ",t.timeit(number = 1))
# print(f6, "\n")

t=timeit.Timer(lambda : Shell_sort.shell(f7))
print("Shell sort ",t.timeit(number = 1))
print(f7, "\n")