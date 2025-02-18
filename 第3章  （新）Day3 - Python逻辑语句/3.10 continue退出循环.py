# continue 退出当前循环迭代
for i in range(10):
    if i == 6:
        # break
        continue
    # 0 1 2 3 4 5 7 8 9
    print(i, end=' ')
