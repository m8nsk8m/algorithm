
T = int(input())

for t in range(T):
    word = input().split()
    result = []
    for i in word:
        result.append(i[::-1])

    print(' '.join(result))

