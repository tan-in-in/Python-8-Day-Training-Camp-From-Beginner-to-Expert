# 转移符号：\
# 功能：将某些普通符号给予特殊功能 将一些特殊功能的符号普通化

# \n 换行
s = 'i am yuan \nmy age is 19'
print(s)

s2 = "let's Go!"
# s3 = 'let's Go!'  # SyntaxError: unterminated string literal (detected at line 9) SyntaxError：未终止的字符串文字（在第 9 行检测到）
# \' 表示'
s3 = 'let\'s Go!'
print(s2)
print(s3)

# C:\Users\TAN\Desktop\Python8天训练营课件
# \\ 表示 \
print('C:\\Users\\TAN\\Desktop\\Python8天训练营课件')
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
