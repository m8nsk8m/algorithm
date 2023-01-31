
count = [0] * (1000 + 1) 

sum1 = 0 #합 변수
for i in range(10):
    num = int(input())
    sum1 += num  # 계속 더해준다.
    count[num] += 1  # 개수를 +1 씩 해준다.

print(sum1 // 10)  # 최대값
print(count.index(max(count)))  # 최빈값