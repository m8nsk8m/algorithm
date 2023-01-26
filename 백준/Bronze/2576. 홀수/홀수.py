min = 100   # 주어지는 자연수가 100보다 작기 때문에..
sum = 0  # 합 변수

for i in range(7): # 자연수 1개 하나씩 입력 받기
    num = int(input())
    if num % 2 == 1:  # 홀수 일경우
        sum += num  # sum 변수에 차례대로 더하기
        if num < min:  # 100이하의 자연수일경우 
                min = num #min 이라는 변수에 할당한다 다음 반복때는 이전 자연수와 비교하여 더작은 자연수를 할당시킨다 최종적으로 젤 작은 수만 남는다.

    
if sum == 0: # 홀수가 없을 경우 
    print(-1)

else:
    print(sum)
    print(min)