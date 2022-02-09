import struct

ret = struct.pack('i', 4096)
print(ret)

ret_un = struct = struct.unpack('i', ret)
print(ret_un)
print(ret_un[0])
