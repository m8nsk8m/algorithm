
T = int(input())

for ele in range(1, T + 1):

    numbers = list(map(int, input().split()))
    avg = sum(numbers)/len(numbers)
    avg = round(avg)
    print(f'#{ele} {avg}')