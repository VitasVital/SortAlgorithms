import random
import string

def build_rand_string(size, lenght):
    l=[]
    for i in range(lenght):
        l.append(''.join(random.choice(string.ascii_letters) for _ in range(size)))
    return l

rand_string_5000_100=build_rand_string(50,100)
l=rand_string_5000_100[25:75]
l.sort()
rand_string_5000_100[25:75]=l

rand_string_5000_10000=build_rand_string(50,10000)
l=rand_string_5000_10000[25:75]
l.sort()
rand_string_5000_10000[25:75]=l

# rand_string_5000_1000000=build_rand_string(50,1000000)
# l=rand_string_5000_1000000[25:75]
# l.sort()
# rand_string_5000_1000000[25:75]=l