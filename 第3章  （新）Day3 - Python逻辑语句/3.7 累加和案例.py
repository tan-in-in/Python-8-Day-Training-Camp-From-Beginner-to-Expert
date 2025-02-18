# 案例1:从1+100案例
ret = 0
for i in range(1, 101):
    if i < 100:
        print(f'{i}+', end='')
    else:
        print(f'{i}', end='')
    ret += i
print(f'={ret}')

# 案例2:在循环中嵌套分支或循环
# 计算1-100的所有偶数和
