import locale

text_str = 'The quick brown fox jumped over the lazy dogs'
print(text_str.encode('utf-8'))

byte_str =  b'The quick brown fox jumped over the lazy dogs'
print(byte_str.decode())

print('foo' == b'foo')



print (locale.getpreferredencoding())


with open('b_text.py','rb') as f:
    text_str=f.read()
    print (type(text_str))
    print (text_str)


