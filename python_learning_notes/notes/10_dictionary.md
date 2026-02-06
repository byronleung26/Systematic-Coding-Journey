# 知识点
1. 字典（dictionary）
   - 一系列键值对。每个键都与一个值关联，可以使用键来访问与之关联的值
   - 键必须是不可变类型Immutable Types：字符串、数字、元组（不能是列表、字典）
   - 与键相关联的值可以是数、字符串、列表乃至字典。事实上，可将任意Python对象用作字典中的值
   - 字典用放在花括号{}中的一系列键值对表示
   - 键值对包含两个相互关联的值，当你指定键时，python将返回与之关联的值
   - 键和值之间用冒号分隔，键值对之间用逗号分隔
2. 访问字典中的值
   - 指定字典名并把键放在后面的方括号内
   ```python
   alien_0 = {'color': 'green', 'points': 5}
   new_points = alien_0["points"]
   prints(f"You just earned {new_points} points!")
   ```
3. 添加键值对
   `alien_0["x_position"] = 0`，键为x_position，值为0
   `alien_0["y_position"] = 25`，键为y_position，值为25
   - 字典中元素排列顺序与添加顺序相同
4. 如果要使用字典来存储用户提供的数据或者编写能自动生成大量键值对的代码，通常需要先定义一个空字典
5. 修改字典中的值
   - 依次指定字典名、用方括号括起来的键和与该键关联的新值 
   `alien_0['x_position'] = alien_0['x_position'] + x_increment`
   `alien_0['x_position'] += x_increment`
6. 删除键值对
   del语句
   `del alien_0['points']`，从字典alien_0中删除"points"及其值
7. 由类似的对象组成的字典
   - 字典可以存储一个对象的多种信息
   - 也可以使用字典来存储众多对象的同一种信息
   ```python
   person = {
      'name': 'Alice',   # 冒号后一个空格
      'age': 25,   #逗号后一个空格
      'city': 'Beijing',  #最后一行推荐加逗号
   }  # 右花括号单独一行
8. 使用get()来访问值
   - 第一个参数用来指定键，第二个参数为当指定的键不存在时返回的值
9. 遍历Loop / Iterate列表
   - 编写遍历字典的for循环，可声明两个变量，分别用于存储键值对中的键和值。for语句的第二部分包含字典名和items()方法
   - 在不需要使用字典中的值时，使用keys() 方法。遍历字典时，会默认遍历所有的键，所以keys()可省略
   - 使用sorted()函数来获得按特定顺序排列的键列表的副本
   `for name in sorted(favorite_languages.keys()):`
       `print(f"{name.title()}, thank you for taking the poll.")`
   - 遍历字典中的所有值，使用values()方法
   - 可使用集合set()函数，来剔除重复的值
   - 可以使用一对花括号直接创建集合，并在其中用逗号分隔元素
10. 嵌套Nesting，将多个字典存储在列表中或将列表作为值存储在字典中
11. 字典列表
```python
aliens = []  # 生成一个用于存储外星人的空列表
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print(f'The number of alien:{len(aliens)}')
```
12. 在字典中存储列表
13. 在字典中存储字典
   - 列表和字典的嵌套层级不应太多

# 实操收获
1. 语句，构成程序的基本**执行单元**，完成特定操作
   函数
      **独立的代码块**，有输入和输出，可以被多次调用。
      定义方式：def 函数名(参数):
      调用方式：函数名(参数)
   方法，属于某个**对象的函数**，通过对象调用。对象.方法名(参数)
2. 教程中出现--snip--，意思是省略部分代码
3. 带条件的列表推导式List Comprehension：[结果 for 变量 in 序列 if 条件]
4. join()方法，将序列（列表、元组等）中的元素连接成一个字符串，格式："分隔符".join(列表)
   ```python
   words = ["Hello", "World", "Python"]
   result = " ".join(words)  # 用空格连接
   print(result)  # 输出: Hello World Python
   result = ",".join(words)  # 用逗号连接
   print(result)  # 输出: Hello,World,Python
   result = "-".join(words)  # 用连字符连接
   print(result)  # 输出: Hello-World-Python
   ```
5. 嵌套循环print的问题
6. 大段代码用括号自然续行，清晰
6. 变量名保持简介