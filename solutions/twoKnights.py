n = int(input())
answer = 0
for i in range(1, n+1):
    answer = ((i**2 * (i**2 -1)//2) - 4*(i-1)*(i-2))
    print(answer)