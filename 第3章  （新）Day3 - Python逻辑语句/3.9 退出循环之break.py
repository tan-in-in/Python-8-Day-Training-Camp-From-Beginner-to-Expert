# 循环退出机制
# break continue 强制退出
# break:退出整个循环
# continue:退出当次循环
# print('break')
# for i in range(10):
#     if i == 6:
#         break
#     print(i, end='')
#
# print()
# print('continue')
# for i in range(10):
#     if i == 6:
#         continue
#     print(i, end='')

# 1.打印半径为1-100的圆的面积 pi * r ** 2
# 2.半径为1-100范围内找到第一个面积大于1000的半径值
import math
for r in range(1, 100):
    # 计算圆的面积
    area = math.pi * r ** 2
    if area > 1000:
        print(f'半径为{r}的圆的面积:{round(area, 2)}')
        break
