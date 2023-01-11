
# input값 없음/?

for i in range(5):         #0000011111
    for j in range(5):     #0123401234
        if i == j:
            print('#', end=' ')
        else:
            print('+', end=' ')
# 이렇게 코드 짜고 print()위치가 항상 어렵다 ㅜㅜ 

    print() # 루프 한번돌때 (문자5개) 마다 개행되어야 하기때문에
            # print 위치는 j 밑임
            # i 밑에 하면 상단의 for 문까지 돌려야함

## + + + + 
#+ # + + + 
#+ + # + +
#+ + + # +
#+ + + + #