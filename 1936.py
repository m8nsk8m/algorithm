
## 인풋 32  가위 1 바위 2 보 3  이긴사람 A
a = list(map(int,input().split()))

if a[0] == 2:
    if a[1] == 1:
        print('A')
    else:
        print('B')
if a[0] == 1:
    if a[1] == 3:
        print('A')
    else:
        print('B')
if a[0] == 3:
    if a[1] == 2:
        print('A')
    else:
        print('B')
