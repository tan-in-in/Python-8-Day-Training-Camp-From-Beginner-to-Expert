"""
python操作文件流程
找到文件 双击打开
读或修改
保存 关闭
"""
filename = '7.5 测试.txt'
# 写操作
f = open(filename, mode='w', encoding='utf-8')  # 打开文件
f.write('我是野生人\n')  # 写操作
f.write('我是野生人\n')  # 写操作
f.write('我是野生人\n')  # 写操作
f.write('我是野生人\n')  # 写操作
# f.read()  # 读操作
f.close()

# 读操作
f = open(filename, mode='r', encoding='utf-8')
# print(f.read())
print(f.readline())
f.close()

# 追加操作
f = open(filename, mode='a', encoding='utf-8')
f.write('1')
f.close()
