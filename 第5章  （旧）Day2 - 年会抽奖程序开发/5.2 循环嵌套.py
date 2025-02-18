# 打印房间号
# 例:L2-202 第二层202房间
for i in range(1, 6):
    print(f'----------{i}层----------')
    for j in range(1, 9):
        print(f'L{i}-{i}0{j}室')
