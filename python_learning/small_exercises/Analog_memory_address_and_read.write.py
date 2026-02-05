# 用列表模拟主存储器，每个元素代表1个存储单元(cell)，存1个字节(byte)
main_memory = [0] * 5
print("初始存储器:",main_memory)
# 写操作(write)：往地址2存数据10
address = 2
data = 10
main_memory[address] = data
print(f"往地址{address}写入{data}后",main_memory)
# 读操作(read)：从地址2读数据
read_data = main_memory[address]
print(f"从地址{address}读出的数据:",read_data)