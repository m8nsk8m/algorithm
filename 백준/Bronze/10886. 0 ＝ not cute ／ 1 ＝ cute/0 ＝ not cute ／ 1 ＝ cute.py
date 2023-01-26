N = int(input())

cnt = 0
cntx = 0
for n in range(N):

    a = int(input())
    if a == 1:
        cnt += 1
    elif a == 0:
        cntx += 1

if cnt > cntx:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')
    
        