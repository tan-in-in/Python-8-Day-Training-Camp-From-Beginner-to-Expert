f = open('7.10 测试.txt', 'r+', encoding='utf-8')

# 1.将文件加载到内存
data = f.read()
new_data = data.replace('修改', '的修改')

# 2.清空文件
f.seek(0)
f.truncate()

# 3.把新内容写回硬盘
f.write(new_data)
f.close()
