s = '路飞'
s_gbk = s.encode('gbk')
print(s_gbk)  # b'\xc2\xb7\xb7\xc9'

s_unicode = s_gbk.decode('gbk')
print(s_unicode)  # 路飞

s_utf8 = s_unicode.encode('utf-8')
print(s_utf8)  # b'\xe8\xb7\xaf\xe9\xa3\x9e'
