
N = int(input())


result = []
for n in range(N):
    result.append(int(input())) 

numbers = sorted(result)  
for n in range(len(result)): 
    print(numbers[n])  

