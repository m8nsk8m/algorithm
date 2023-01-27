a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
ab = A - B
ba = B - A
print(len(ab) + len(ba))