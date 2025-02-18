# 分支嵌套
# 身份证号判断

pid = input('请输入你的身份证号:')

# 身份证号是否为18位
if len(pid) == 18:
    print('打印个人基本信息:')
    # 1.打印性别 身份证号倒数第二位如果是偶数 代表是女生 否则男生
    if int(pid[-2]) % 2 == 0:
        print('性别:女性')
    else:
        print('性别:男性')
    # 打印籍贯
    origin = pid[:3]
    if origin == '110':
        print('籍贯:北京市')
    elif origin == '120':
        print('籍贯:天津市')
    elif origin == '310':
        print('籍贯:上海市')
    elif origin == '500':
        print('籍贯:重庆市')
    else:
        print('不是直辖市!')

else:
    print('身份证位数有误!')
print('程序结束!')
