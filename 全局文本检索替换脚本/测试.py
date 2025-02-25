import sys

print(sys.argv)
old_str = sys.argv[1]
new_str = sys.argv[2]
filename = sys.argv[3]

# 1.将文件内容读入内存中
f = open(filename, 'r+', encoding='utf-8')
data = f.read()

# 2.修改内存中的内容
old_str_count = data.count(old_str)
new_data = data.replace(old_str, new_str)

# 3.清空原文件
f.seek(0)
f.truncate()

# 4.写入新内容
f.write(new_data)
f.close()
print(f'成功替换字符"{old_str}" to "{new_str}", 共{old_str_count}处...')

