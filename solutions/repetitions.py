#1069
s = input()
s = s[::]
count = 1
maxCount = 1
index = 1
stack = [s[0]]
while index < len(s):
    if stack[-1] != s[index]:
        stack.append(s[index])
        count = 1
    else:
        count += 1
        maxCount = max(count, maxCount)
    index += 1
print(maxCount)