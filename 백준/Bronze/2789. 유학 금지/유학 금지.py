word = input() 

for i in 'CAMBRIDGE': # 문자열 형태로만 for문 돌려도 한줄씩 출력된다  
    word = word.replace(i,'') # word 자기자신에 할당해주어야 한다 그래야지
     # 비교후 공백으로 바뀐값을 치환함

print(word)