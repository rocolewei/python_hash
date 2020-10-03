# 输出九九乘法表
for i in range(1, 10):
    for j in range(i, 10):
        print('{0}*{1}={2:2d}'.format(i, j, i*j), end=' ')
    print()
