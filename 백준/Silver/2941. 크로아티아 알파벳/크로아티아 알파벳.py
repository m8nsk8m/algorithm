alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

a = input()

for i in alpha:
    a = a.replace(i, '1') # replace 의 특징을 잘 알고 있기  찾아서 바꿔주는..
    
print(len(a))
