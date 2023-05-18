#1094
n = int(input())
input_array = list(map(int, input().split()))
answer = 0
for i in range(1, n):
    if input_array[i] < input_array[i-1]:
        answer += input_array[i-1] - input_array[i]
        input_array[i]=input_array[i-1]

print(answer)