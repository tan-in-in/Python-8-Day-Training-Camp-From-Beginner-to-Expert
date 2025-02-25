f = open('7.6 文本', 'r', encoding='utf-8')

# print(f.readlines())
for line in f:
    line = line.split()
    # print(line)
    if int(line[3]) >= 170 and int(line[4]) <= 50:
        print(line)
