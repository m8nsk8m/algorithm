
list = []
for i in range(10):
    n = int(input())  
    list.append(n % 42)  # 입력받은 값을 42로 나눈 나머지를 추가...?
list = set(list) # 집합 자료형으로 (중복제거)
print(len(list))