# 1.确定在文件里 存储文本结构
# f = open('7.12 文本信息.txt', 'w', encoding='utf-8')
#
# # 2.把账号数据读到内存 为了方便调用 用字典数据类型
# accounts = {
#     'tan': ['tan', '123', '1'],
#     'jin': ['jin', '1234', '0'],
#     'lin': ['lin', '12345', '1'],
# }
# f.write(str(accounts))
# f.close()
#

# 3.循环 要求用户输入账号信息
accounts = {}
f = open('7.12 文本信息.txt', 'r', encoding='utf-8')
data = f.read()
new_data = ''
for i in data:
    if i in '\'[]{} ':
        continue
    if i == ':':
        i = ','
    new_data += i
for i in range(0, len(new_data.split(','))//4):
    accounts[new_data.split(',')[i*4]] = new_data.split(',')[i*4+1:i*4+4]
# 循环判断
count = 0
while count < 3:
    user = input('Username:').strip()
    if user not in accounts:
        print('该用户未注册...')
        continue
    passwd = input('Password:').strip()
    # 去账号dict里去判断password
    if passwd == accounts[user][1]:
        print(f'恭喜{user}成功登录...')
        break
    else:
        print('密码错误, 请重新登录...')
        count += 1
        continue
f.close()

