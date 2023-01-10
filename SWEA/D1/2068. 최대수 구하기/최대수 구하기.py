
T = int(input())

for ele in range(1, T + 1):
    
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(ele, max(numbers)))
