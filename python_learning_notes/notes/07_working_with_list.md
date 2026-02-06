# 知识点
1. 遍历整个列表
   - for循环
   ```python
   magicians = ['alice', 'david', 'carolina']
   for magician in magicians:
       print(magician)
   ```
2. 常见缩进错误
   - 忘记缩进
   - 忘记额外的缩进
   - 不必要的缩进
   - 循环后不必要的缩进
   - 遗漏冒号
3. 创建数值列表
   - 使用range()函数来生成一系列的数
   - 从指定的第一个值开始，在到达第二个值时停止，因此输出不包含第二个值
   - 使用list()函数将range()的结果直接转换为列表
   - 使用range()时，可以指定步长（第三个参数）
   - min()，找出数值列表的最小值
   - max()，找出数值列表的最大值
   - sum()，计算数值列表的总和
   - 列表推导式list comprehension
     首先指定一个描述性的列表名。然后指定一个左方括号，并定义一个表达式，用于生成要存储到列表中的值。接下来，编写一个 for 循环，用于给表达式提供值，再加上右方括号。
     ```python
     squares = [value**2 for value in range(1, 11)]
     print(squares)
     ```
4. 切片，语法list[start:end:step]
   ```python
   players = ['charles', 'martina', 'michael', 'florence', 'eli']
   print(players[1:3])
   print(players[:4])
   print(players[2:])
   print(players[-3:])
   ```
   - 可在表示切片的方括号内指定第三个值。这个值告诉 Python 在指定范围内每隔多少元素提取一个
   - 遍历切片
   ```python
   players = ['charles', 'martina', 'michael', 'florence', 'eli']
   print("Here are the first three players on my team:")
   for player in players[:3]:
       print(player.title()) 
   ```
5. 复制列表
   - 创建一个包含整个列表的切片，同时省略起始索引和终止索引[:]

# 实践收获
1. 数值列表注意范围错误