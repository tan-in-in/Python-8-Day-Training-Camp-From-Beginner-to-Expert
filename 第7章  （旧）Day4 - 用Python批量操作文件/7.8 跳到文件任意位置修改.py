# python操作文件的其他功能
# 1.seek 操作文件的光标移动到指定位置
f = open('7.8 测试.txt', 'w', encoding='utf-8')
for i in range(10):
    f.write(str(i) + '\n')
f.seek(3)
f.write('------')
print(f.tell())
f.close()

f = open('7.8 测试.txt', 'r', encoding='utf-8')
# 移动是按字节 英文2个字节 中文3个字节
f.seek(9)
# print(f.readline())

# 2.tell 返回光标当前位置
print(f.tell())
f.close()

# 3.flush 将文件从内存buffer里强制刷新到硬盘


