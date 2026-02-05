# 十进制转二进制(binary)
num = 10
binary_num = bin(num)  # bin()函数转二进制
print(f"十进制{num} = 二进制{binary_num}")  # 输出：十进制10 = 二进制0b1010

# 十进制转十六进制(hexadecimal)
hex_num = hex(num)  # hex()函数转十六进制
print(f"十进制{num} = 十六进制{hex_num}")  # 输出：十进制10 = 十六进制0xa

# 二进制转十六进制（刚学的4位分组转换）
binary_str = "10101110"
hex_from_binary = hex(int(binary_str, 2))
print(f"二进制{binary_str} = 十六进制{hex_from_binary}")  # 输出：二进制10101110 = 十六进制0xae