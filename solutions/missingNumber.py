#1083
n = int(input())
input_array = input()
array = list(map(int, input_array.split()))
totalSum = (n * (n + 1)) // 2
currentSum = sum(array)
print(totalSum - currentSum)