



a = [int(input()) for i in range(3)]


if sum(a) == 180: #세각의 합이 180이고
    if a[0] == a[1] == a[2]: # 세각의 크기가 모두 60이면, 
        print('Equilateral')
    elif a[0] == a[1] or a[1] == a[2] or a[0] == a[2]: # 두각이 같은경우
        print('Isosceles')
    else: # 같은각이 없는 경우
        print('Scalene')
    
else: # 세각의 합이 180이 아닌경우
    print('Error')
