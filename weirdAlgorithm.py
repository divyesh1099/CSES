n = int(input())
answer = str(n) + ' '
while n!= 1:
    if n%2 ==0:
        n = n//2
        answer += str(n) + ' '
    else:
        n = n*3 + 1
        answer += str(n) + ' '
print(answer)