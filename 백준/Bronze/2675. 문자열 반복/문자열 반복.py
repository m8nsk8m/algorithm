
T = int(input())


for t in range(T): #테스트케이스
    cnt, word = input().split()
    cnt1 = int(cnt)
    word1 = list(str(word))
    result = []
    for i in word1:
        result += i*cnt1

    print(''.join(result))
