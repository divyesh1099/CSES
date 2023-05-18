#1070
n = int(input())
evens = list(i for i in range(1, n+1, 2))
odds = list(i for i in range(2, n+1, 2))
answer = evens + odds
for i in range(1,len(answer)):
    if abs(answer[i] - answer[i-1]) == 1 or n==2:
        answer = "NO SOLUTION"
        break
if len(answer) == n-1:
    answer = "NO SOLUTION"
if n == 4:
    answer = [2, 4, 1, 3]
print(" ".join(list(map(str, answer)))) if answer != "NO SOLUTION" else print("NO SOLUTION")