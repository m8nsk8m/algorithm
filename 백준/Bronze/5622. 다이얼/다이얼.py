alphalist = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input() # 문자열로 받아서
time = 0 # 구해야 하는것은 걸리는 시간이기 때문에 변수를 설정해 준다.

for i in alphalist:# alphalist 에서 요소를 꺼내서
    for a in i: # 요소를 한글자씩 분리
        for w in word: # 입력받은 알파벳을 분리
            if a == w: # 두 글자가 같으면
                time += alphalist.index(i) + 3

print(time)