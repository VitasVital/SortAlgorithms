from random import randint
import random
import string

# rand_numbs_09_100 = [randint(0, 9) for i in range(100)]
# rand_numbs_09_10000 = [randint(0, 9) for i in range(10000)]
# rand_numbs_09_1000000 = [randint(0, 9) for i in range(1000000)]
#
# rand_integer_50_100 = [randint(-25, 25) for i in range(100)]
# rand_integer_50_10000 = [randint(-25, 25) for i in range(10000)]
# rand_integer_50_1000000 = [randint(-25, 25) for i in range(1000000)]
#
# rand_integer_500_100 = [randint(-250, 250) for i in range(100)]
# rand_integer_500_10000 = [randint(-250, 250) for i in range(10000)]
# rand_integer_500_1000000 = [randint(-250, 250) for i in range(1000000)]
#
# rand_integer_5000_100 = [randint(-2500, 2500) for i in range(100)]
# rand_integer_5000_10000 = [randint(-2500, 2500) for i in range(10000)]
# rand_integer_5000_1000000 = [randint(-2500, 2500) for i in range(1000000)]
#
# rand_integer_50000_100 = [randint(-25000, 25000) for i in range(100)]
# rand_integer_50000_10000 = [randint(-25000, 25000) for i in range(10000)]
# rand_integer_50000_1000000 = [randint(-25000, 25000) for i in range(1000000)]
#
# rand_integer_500000_100 = [randint(-250000, 250000) for i in range(100)]
# rand_integer_500000_10000 = [randint(-250000, 250000) for i in range(10000)]
# rand_integer_500000_1000000 = [randint(-250000, 250000) for i in range(1000000)]

def build_rand_string(size, lenght):
    l=[]
    for i in range(lenght):
        l.append(''.join(random.choice(string.ascii_letters) for _ in range(size)))
    return l

rand_string_50_100=build_rand_string(50,100)
rand_string_50_10000=build_rand_string(50,10000)
rand_string_50_1000000=build_rand_string(50,1000000)

rand_string_500_100=build_rand_string(500,100)
rand_string_500_10000=build_rand_string(500,10000)
rand_string_500_1000000=build_rand_string(500,1000000)

rand_string_5000_100=build_rand_string(5000,100)
rand_string_5000_10000=build_rand_string(5000,10000)
rand_string_5000_1000000=build_rand_string(5000,1000000)

rand_string_50000_100=build_rand_string(50000,100)
rand_string_50000_10000=build_rand_string(50000,10000)
rand_string_50000_1000000=build_rand_string(50000,1000000)

rand_string_500000_100=build_rand_string(500000,100)
rand_string_500000_10000=build_rand_string(500000,10000)
rand_string_500000_1000000=build_rand_string(500000,1000000)