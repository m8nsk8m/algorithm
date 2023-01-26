num = int(input()) # 손님수
seat = map(int,input().split()) #손님이 원하는 좌석
pc = [0]*101  #1~100 컴퓨터
result = 0 

for i in seat:
    if(pc[i]==0):  # 손님이 원하는 자리가 비어있으면
        pc[i] += 1  #자리에 앉히기  
    else:
        result += 1 #이미 있으면 거절당한 손님으로 

print(result)

