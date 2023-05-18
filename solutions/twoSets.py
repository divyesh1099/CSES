n = int(input())
total_sum = (n * (n+1))//2
if total_sum %2 != 0:
    print("NO")
else:
    print("YES")
    target_sum = total_sum //2
    a = set()
    b = set()
    for i in range(n, 0, -1):
        if i <= target_sum:
            target_sum -= i
            a.add(i)
        else:
            b.add(i)

    print(len(a))
    print(*a)
    print(len(b))
    print(*b)
