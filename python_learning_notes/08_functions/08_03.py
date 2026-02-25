# 编写一个名为make_shirt()的函数，它接受一个尺码以及要印到T恤上的字样。
# 这个函数应该打印一个句子，简要地说明T恤的尺码和字样。
'''
def make_shirt(size,text):
    """说明T恤的尺码和字样"""
    print(f"T恤的尺码是{size},字样是{text}")
make_shirt('2XL','火力全开')'''
# 修改make_shirt()函数，使其在默认情况下制作一件印有
# “I love Python”字样的大号T恤。
# 调用这个函数分别制作一件印有默认字样的大号T恤，
# 一件印有默认字样的中号T恤，
# 以及一件印有其他字样的T恤（尺码无关紧要）。
def make_shirt(size='Large',text='I love Python'):
    """说明T恤的尺码和字样"""
    print(f"T恤的尺码是{size},字样是{text}")
make_shirt()
make_shirt('Medium')
make_shirt(text='超越自己')