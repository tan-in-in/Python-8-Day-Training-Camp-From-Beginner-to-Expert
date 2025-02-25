# 1.确定在文件里 存储文本结构
f = open('7.12 文本信息.txt', 'w', encoding='utf-8')

# 2.把账号数据读到内存 为了方便调用 用字典数据类型
accounts = {
    'tan': ['tan', '123', '0'],
    'jin': ['jin', '1234', '0'],
    'lin': ['lin', '12345', '0'],
}
f.write(str(accounts))
f.close()


# 3.循环 要求用户输入账号信息
accounts = {}
f = open('7.12 文本信息.txt', 'r', encoding='utf-8')
data = f.read()
f.close()
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

while True:
    user = input('Username:').strip()
    if user not in accounts:
        print('该用户未注册...')
        continue
    elif accounts[user][2] == '1':
        print('此账户已锁定, 请联系管理员...')
        continue
    count = 0
    while count < 3:
        passwd = input('Password:').strip()
        # 去账号dict里去判断password
        if passwd == accounts[user][1]:
            print(f'恭喜{user}成功登录...')
            exit('bye...')
        else:
            print('密码错误, 请重新输入...')
            count += 1
            if count == 3:
                accounts[user][2] = '1'
                print(f'{user}账号已锁定')
                # 更新文件内容
                f = open('7.12 文本信息.txt', 'w', encoding='utf-8')
                for i, j in accounts.items():
                    line = ','.join(j) + '\n'  # 把列表转为字符串
                    f.write(line)
                f.close()
            continue
