w = []
k = []

for i in range(10):
    w.append(int(input()))
for i in range(10):
    k.append(int(input()))

 # 내림차순 정렬   
w.sort(reverse=True)
k.sort(reverse=True)

# 3등까지의 합
print(sum(w[:3]), sum(k[:3]))