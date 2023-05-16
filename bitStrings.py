import math
n = int(input())
my_sum = 0
if n >1:
    my_sum += 2
for i in range(1, n):
    my_sum += math.perm(n, i)
print(my_sum)