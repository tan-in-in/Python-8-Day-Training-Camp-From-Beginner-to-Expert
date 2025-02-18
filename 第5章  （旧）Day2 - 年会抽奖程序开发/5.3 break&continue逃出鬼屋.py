# 打印楼层的小程序:遇到第三层 不打印任何房间号 其他楼层都打印
# 到404房间后直接进入第五层
# 打印房间号
# 例:L2-202 第二层202房间
for i in range(1, 6):
    if i == 3:
        # continue:跳过当前循环
        # break:结束当前整个循环
        continue
    print(f'----------{i}层----------')
    for j in range(1, 9):
        print(f'L{i}-{i}0{j}室')
        if i == 4 and j == 4:
            print('遇到鬼屋404房间,over 了....')
            break

