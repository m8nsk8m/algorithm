arr = [[0] * 100 for _ in range(100)]
cnt = 0
for i in range(4):
    x, y, x_, y_ = map(int, input().split())
    for j in range(x, x_):
        for k in range(y, y_):
            if arr[k][j] == 0:
                arr[k][j] = 1
                cnt += 1
print(cnt)