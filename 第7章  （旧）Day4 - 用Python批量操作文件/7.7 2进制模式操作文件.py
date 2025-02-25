f = open('7.7 img.png', 'rb')

# print(f)  # <_io.TextIOWrapper name='7.7 img.jpg' mode='r' encoding='cp936'>
f_read = str(f.read())

f.close()

f = open('7.7 text.txt', 'w')
f.write(f_read)
f.close()

