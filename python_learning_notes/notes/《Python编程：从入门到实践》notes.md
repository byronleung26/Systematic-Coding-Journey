# 模块1 Python安装与环境配置
1.  Python解释器安装，Python3.12。环境变量,安装时选中“Add python.exe to PATH”
2.  开发工具VS Code安装。python -version查看版本
3.  .md文件，Markdown一种轻量级标记语言。这是一个**粗体**，这是一个*斜体*，这是~~删除线~~文字，这是`内联代码`，这是```代码块```
4.  python模块——pip工具——pip install命令安装模块——import语句导入模块——“模块.变量/函数/类”使用模块中的内容。 

# 模块2 代码基础
1. 注释comment：单行注释；多行注释（说明文档）
2. 缩进：确定代码之间的逻辑关系和层次关系  
   空格和Tab键，不能混和使用空格和Tab键  
   添加缩进后的代码从属于其上最近的一行非缩进或非同等级别缩进的代码  
   缩进量不同会导致代码语义的改变，不允许出现无意义或不规范的缩进
3. 语句换行  
   在未结束的代码末尾加\  
   使用()包裹代码
4. 标识符：变量名、函数名、类名等  
   由字母、数字或下画线组成，不能以数字开头  
   区分大小写  
   不允许使用关键字作为标识符
5. 关键字：python已经使用且不允许开发人员重复定义的标识符  
   ```python
   import keyword          # 导入ketword模块
   print(keyword.kwlist)   # 使用keyword模块中的kwlist变量
   ```
   False/await/else/import/pass/None/break/except/in/raise/Ture/class/finally/is/return/and/continue/for/lambda/try/as/def/from/nonlocal/while/assert/del/global/not/with/async/elif/if/or/yield
   ```python
   print(help("import"))   # 查看关键字import详细信息
   ```
6. 变量的输入与输出  
   input()函数，接收用户从键盘输入的数据，返回一个**字符串**类型的数据，语法格式input([prompt])  
   - 使用int()来获取数值输入
   print()函数，用于向控制台输出数据，可以输出任何类型的数据，语法格式print(*objects,sep=' ',end='\n',file=None,flush=False)  
   *objects：表示输出的数据，输出多个数据时，数据需要用“,”分隔  
   sep：用于设定数据之间使用的分隔符，默认空格  
   end：用于设定输出结果以什么结尾，默认空格  
   file：表示数据要写入的文件对象，默认值为sys.stdout  
   flush：表示是否刷新标准输出流，默认值为False

# 模块3 变量
1. 变量variable：能被存储结果或表示值的抽象概念  
2. 标识内存单元的标识符又称为变量名，通过“=”定义变量  
3. “变量名=值value”  
4.  通过变量名访问存储在内存中与该变量关联的值，如
   ```python
   data=100
   print(data)
   ```

# 模块4 字符串
1. 字符串string类型（str）：用于表示文本数据  
2. 单引号（'python123'）、双引号（"python4$"）或者三引号（'''python s1~()'''）包裹的一系列字符
3. 使用方法（method）修改字符串的大小
   ```python
   name = "ada lovelace"
   print(name.title())#以首字母大写的方式显示每一个单词
   print(name.upper())#全大写
   print(name.lower())#全小写```
4. 在字符串中使用变量
   f 字符串，f 是 format（设置格式）的简写
5. 使用制表符和换行符来添加空白
   `\t`添加制表符
   `\n`换行
   `\n\t`换行后添加制表符
6. 删除空白
   rstrip()方法，删除右端空白
   lstrip()方法，删除左端空白
   strip()方法，两端空白
   永久删除空白，必须将删除操作的结果关联到变量
7. 删除前缀
   removeprefix()方法，在括号内输入要从原始字符串中删除的前缀
   想保留删除前缀后的值，既可将其重新赋给原来的变量，也可将其赋给另一个变量
   removesuffix()删除后缀

# 模块5 数字类型
1. **数字number**
   整数integer：
     - 进行+，-，*，/，**
     - 二进制：`0b`或`0B`开头（如 `0b1010`）
     - 八进制：`0o`或`0O`开头（如 `0o12`）
     - 十六进制：`0x`或`0X`开头（如 `0xA`）
     - 转换函数：
       `bin(x)`：十进制 → 二进制
       `oct(x)`：十进制 → 八进制  
       `int(x)`：其他进制 → 十进制
       `hex(x)`：十进制 → 十六进制
   浮点数float：
     - 科学计数法：`-3.14e10`（相当于 -3.14×10¹⁰）
     - 浮点数运算可能存在微小的精度误差
     - 将任意两个数相除，结果总是浮点数
     - 无论哪种运算，只要有操作数是浮点数，默认得到的就总是浮点数
   复数类型：
     - 表示形式：`real + imagj`（如 `1 + 2j`）
     - 创建函数：`complex(实部, 虚部)`
     - 属性获取：
       `复数.real`：获取实部
       `复数.imag`：获取虚部
   布尔类型：
     - `bool()`函数检测数据的布尔值
     - `False`：0、0.0、空字符串、空列表等
     - `True`：其他值
2. **数字类型转换**
     - `int(x[, base])`：将x转换为整型，base表示进制数
     - `float(x)`：将x转换为浮点型
     - `complex(x)`：将x转换为复数
3. **数中的下划线**
   在书写很大的数时，可使用下划线将其中的位分组，使其更清晰易读
4. **同时给多个变量赋值**
   `x, y ,z = 4, 5, 6`
5. **常量constant**
   其值始终不变，变量名使用全大写字母

# 模块6 列表
1. 列表（list）
   - 由一系列特定顺序排列的元素组成，用“[]”表示列表，用“,”分隔其中的元素
2. 访问列表元素
   - 可指出列表的名称，再指出列表的索引，并将后者放在方括号内，如
   - ```python 
   bicycles = ['trek', 'cannondale', 'redline','specialized']
   print(bicycles[0])
   ```
3. 索引从0而不是从1开始
   - 可以将索引指定为-1，-2，...
4. 使用列表中的各个值
5. 修改列表元素
6. 在列表中添加元素
   - append()方法，将元素添加到列表末尾
   - insert()方法，在列表任意位置添加新元素，()内需要指定“新元素的索引,值”
7. 从列表中删除元素
   - del语句，如`del motorcycles[0]`，需要知道要删除的元素在列表中的位置
   - pop() 方法删除列表末尾的元素，并让你能够**接着使用它**
   - ```python
   motorcycles = ['honda', 'yamaha', 'suzuki']  # 定义列表motorcycles
   print(motorcycles)  # 打印列表motorcycles
   popped_motorcycle = motorcycles.pop()  # 从这个列表中弹出一个值，并将其赋给变量 popped_motorcycle
   print(motorcycles)  # 打印这个列表，以核实从中删除了一个值
   print(popped_motorcycle)  # 打印弹出的值，以证明依然能够访问被删除的值
   ```
8. 删除列表中任意位置的元素
   - pop()方法，在括号中指定要删除元素的索引
9. 根据值删除元素
   - remove()方法，删除后也可以继续使用它的值
   - remove() 方法只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环，确保将每个值都删除
10. 管理列表
   - 使用sort()方法对列表进行永久排序
   - 使用sorted()函数对列表进行临时排序
   - 在并非所有的值都是全小写的时，按字母顺序排列列表要复杂一些
   - 使用reverse()方法，可以反转列表元素的排列顺序，会永久地修改
   - 使用len()函数可以快速获悉列表的长度，计算时从1开始
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

# 模块7 元组
1. 元组tuple，不可变的列表
2. 使用()来标识
```python
   dimensions = (200, 50)
   print(dimensions[0])
   print(dimensions[1])
   ```
   - 试图修改元组的操作是被禁止的
   - 严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清晰。如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号
   - 使用 for 循环来遍历元组中的所有值
   - 给元组变量重新赋值

# 模块8 if语句
1. 条件测试
   - 一个值为True或False的表达式
   - 检查是否相等`==`（相等运算符）
   - lower()方法，将变量的值临时转化为全小写再进行比较
   - 检查是否不等`!=`（不等运算符）
   - 数值比较
   ```python
   answer = 17
   if answer != 42:
       print("That is not the correct answer.Please try again!")
   ```
   - <，<=，>，>=进行比较
   - 使用and检查多个条件` (age_0 >= 21) and (age_1 >= 21)`
   - 使用or检查多个条件` (age_0 >= 21) or (age_1 >= 21)`
   - 检查特定的值是否在列表中`in`
   - 检查特定的值是否不再列表中`not in`
   - 布尔表达式
2. if语句
   - 简单的if语句
   - if-else语句
   - if-elif-else语句
     在if-elif-else语句中设置price的值后，一个未缩进的函数调用print()会根据这个变量的值打印一条消息
   - 使用多个elif代码块
   - 省略else代码块
     else 是一条包罗万象的语句，只要不满足任何if或elif中的条件测试，其中的代码就会执行。这可能引入无效甚至恶意的数据。如果知道最终要测试的条件，应考虑使用一个elif代码块来代替else代码块。这样就可以肯定，仅当满足相应的条件时，代码才会执行（防御性编程）
   - 测试多个条件
     在可能有多个条件为True，且需要在每个条件为True 时都采取相应措施时，适合使用一系列不包含elif和else代码块的简单if语句
3. 使用if语句处理列表
   - 检查特殊元素
   - 确定列表非空
   - 使用多个列表

# 模块9 字典
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

# 模块10 while循环
1. While循环不断地运行，直到指定的条件不再满足为止
2. 退出值，只要用户输入的不是这个值，程序就将一直运行
3. 标志flag
   - 定义一个变量，用于判断整个程序是否处于活动状态
   - 让程序在标志为True时继续运行，标志的值为False时停止运行
   ```python
   prompt = "\nTell me sonmething, and I will repeat it back to you:"
   prompt += "\nEnter 'quit' to end the program."

   active = True
   while cative:
       message = input(prompt)
       if message == 'quit':
           cative = False
       else:
           print(message)
   ```
4. 使用break语句退出循环
   ```python
   prompt = "\nPlease enter the name of a city you have visited:"
   prompt += "\n(Enter 'quit' when you are finished.) "
   while True:
       city = input(prompt)
       if city == 'quit':
           break
       else:
           print(f"I'd love to go to {city.title()}!")
   ```
   - 在所有python循环中都可使用break语句
5. continue语句
   - 返回循环开头，并根据条件测试的结果决定是否继续执行循环
   ```python
   current_number = 0
   while current_number < 10:
       current_number += 1
       if current_number % 2 == 0:
           continue
       print(current_number)
   ```
6. 在列表之间移动元素
   whlie循环 + pop()方法 + append()方法
7. 删除为特定值的所有列表元素
   while循环语句 + remove()方法
8. 使用用户输入填充字典
   while循环 + “字典[键] = 值”

# 模块11 运算符
1. 算术运算符（Arithmetic Operators）
   - +加法
   - -减法
   - *乘法
   - /除法
   - //整除
   - %取模
   - **幂运算
2. 比较运算符（Comparison Operators）
   - ==等于
   - !=不等于
   - <小于
   - <=小于等于
   - `>`大于
   - `>=`大于等于
3. 赋值运算符（Assignment Operators）
   - =简单赋值
   - +=加法赋值，`x += 3`、字符串连接、列表扩展
   - -=减法赋值，`balance -= 250`、集合差集
   - *=乘法赋值，`price *= 1.1`、字符串重复、列表重复
   - /=除法赋值，`average /= count`等价于average=average/count
   - //=整除赋值，求余数、判断奇偶、循环索引
   - %=取模赋值
   - *=幂赋值，求幂、开平方、计算复利
   - :=海象运算符
4. 逻辑运算符（Logical Operators）
   - and
   - or
   - not
5. 身份运算符（Identity Operators）
   - is
   - is not
6. 成员运算符（Membership Operators）
   - in
   - not in
7. 位运算符（Bitwise Operators）
   - &按位与
   - |按位或
   - ^按位异或
   - ~按位取反
   - <<左移
   - `>>`右移
8. 运算符优先级（从高到低）
   1. 括号: ()
   2. 幂运算: **
   3. 按位取反、正负号: ~x, +x, -x
   4. 乘除、取余、整除: *, /, %, //
   5. 加减: +, -
   6. 位移: <<, >>
   7. 按位与: &
   8. 按位异或: ^
   9. 按位或: |
   10. 比较运算符: ==, !=, >, <, >=, <=, is, is not, in, not in
   11. 逻辑非: not
   12. 逻辑与: and
   13. 逻辑或: or
   14. 赋值运算符: =, +=, -=, *=, 等

# 模块12 函数
1. 定义函数
   ```python
   def greet_user():  # 关键字def 函数名:
       """显示简单的问候语"""  # 文档字符串docstring，描述函数是做什么的
       print("Hello!")
   greet_user()
   ```
2. 向函数传递信息
   ```python
   def greet_user(username):  # username:形参parameter，函数完成工作所需的信息
       """显示简单的问候语"""
       print(f"Hello, {username.title()}!")
   greet_user('jesse')  # 'jesse'：实参argument，在调用函数时传递给函数的信息
   ```
3. 传递实参
   - 位置实参，基于实参的顺序进行关联
   - 关键字实参，传递给函数的名值对
4. 可以给每一个形参指定默认值
5. 返回值，函数返回的值。
   - return语句
   ```python
   def get_formatted_name(first_name,last_name):
       """返回标准格式的姓名"""
       full_name = f"{first_name} {last_name}"
       return full_name.title()
   musician = get_formatted_name('jimi','hendrix')
   print(musician)
   ```
6. 给形参指定默认值（空字符串），并将其移到形参列表的末尾，让实参变成可选的
7. 函数可返回任何类型的值，包括列表和字典等
8. 函数与其他的python结构结合起来使用
9. 向函数传递列表
   - 在函数中修改列表
   ```python
   def print_models(unprinted_designs, completed_models):
       """
       模拟打印每个设计，直到没有未打印的设计为止
       打印每个设计后，都将其移到列表completed_models中
       """
       while unprinted_designs:
           current_design = unprinted_designs.pop()
           print(f"Printing model:{current_design}")
           completed_models.append(current_design)
   def show_completed_models(completed_models)"
       """显示打印好的所有模型"""
       print("\nThe following models have been printed:")
       for completed_model in completed_models:
           print(completed_model)
   unprinted_designs = ['phone case','robot pendant','dodecahedron']
   completed_models = []
   ```
   - 禁止函数修改列表，向函数传递列表的副本而不是原始列表
10. 传递任意数量的实参
   - def 函数名(*形参)，星号创建一个元组，包含函数收到的所有值
   - 在函数定义中将接纳任意数量实参的形参放在最后
   - *args，All Regular Grouped (所有常规参数组合成元组)
   - 使用任意数量的关键字实参，def 函数名(形参,**形参)，两个星号创建字典，包含函数收到的其他所有名值对
   - **kwargs，Key Worded ARGumentS (关键字参数变成字典)
11. 将函数存储在模块中，再将模块导入import主程序
   - 模块，扩展名为.py的文件，包含要导入程序的代码
   - `import()`，导入模块
   - `module_name.function_name()`，调用函数
   - `from module_name import function_nam`，导入特定的函数
   - 用逗号分隔函数名，可根据需要从模块中导入任意数量的函数
   - `from module_name import function_name as alias`，使用as给函数指定别名alias
   - `import module_name as mn`，使用as给模块指定别名
   - `from module_name import *`，导入模块中的所有函数（不建议）
12. 注意事项
   - 应给函数指定描述性名称，且只使用小写字母和下划线
   - 每个函数都应包含简要阐述其功能的注释
   - 在给形参指定默认值时，等号两边不要有空格
   - 如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开
   - 所有的 import 语句都应放在文件开头

# 模块13 类
1. 面向对象编程（object-oriented programming，OOP）
   - 把现实世界中的事物（对象）和它们的行为（方法）用代码模拟出来
   - 类（class），表示现实世界中的事物和情景，定义一批对象都具备的通用行为
   - 对象（object），具备这种通用行为，根据需要赋予每个对象独特的个性
   - 实例化，根据类来创建实例（instance）
2. 创建和使用类
   ```python
   class Dog:  # 定义一个名为Dog的类，按约定首字母大写
       """一次模拟小狗的简单尝试"""  # 文档字符串，描述类的功能，可以通过 Dog.__doc__ 或 help(Dog) 查看

       def __init__(self, name, age):  # 构造函数（__init__方法），约定开头末尾两个下划线，创建新对象时自动调用，设置对象的初始状态。self形参必不可少，是一个指向实例本身的引用，让实例能够访问类中的属性和方法
           """初始化属性name和age"""
           self.name = name
           self.age = age

       def sit(self):  # 普通方法，执行时不需要额外的信息，因此只有一个形参self
           """模拟小狗收到命令时坐下"""
           print(f"{Self.name} is now sitting.")

       def roll_over(self):
           """模拟小狗收到命令时打滚"""
           print(f"{self.name} rolled over!")
3. 根据类创建实例
   - `my_dog = Dog('Willie', 6)`
   - 访问属性，`print(f"My dog's name is {my_dog.name}.`
   - 调用方法，`my_dog.roll_over()`
4. 可按需求根据类创建任意数量的实例
5. 给属性指定默认值
```python
class car:
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # 所有对象创建时自动初始化为0
    def get_descriptive_name(self):
        --snip--
```
6. 修改属性的值
   - 直接通过实例访问修改
   - 通过方法修改
   - 通过方法让属性的值递增
