import math
print(dir(math))

from math import sqrt
print(sqrt(16))


#user defined function
def print_sum(fir , sec=4):
    print(fir + sec)

print_sum(1 , 2)
print_sum(1)