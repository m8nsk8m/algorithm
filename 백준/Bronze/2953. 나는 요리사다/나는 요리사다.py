index = 0
result = 0
for i in range(5):
    sum = 0
    a = map(int, input().split())
    a = list(a)
    for j in range(4):
        sum += a[j]
    if result < sum:
        result = sum
        index = i+1

print(index, result)