T = int(input())

for t in range(T):
    change = int(input())
    numbers = [25, 10, 5, 1]
    result = [] 
    for i in numbers:
        result.append(change // i) # 입력받은 돈에서 큰 화폐를 기준으로 나누고.
        change = change % i  # 나눈 값은 출력하고 나머지 값은 다시 남은돈으로 계산
    print(*result) # 언패킹