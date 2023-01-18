
taeboking = input()

cut = taeboking.find('0')

left = taeboking[:cut].count('@')
right = taeboking[cut:].count('@')

print(f'{left} {right}')