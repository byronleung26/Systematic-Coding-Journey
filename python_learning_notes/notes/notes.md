# 第1章 Python概论
掌握模块的导入与使用,能够在程序中熟练导入并使用模块
## 1.认识Python
- 1991年第一个版本，使用C语言实现
- 2000年Python2.0，从maillist的开发方式转变为完全开源的开放方式
- 2008年Python3.0，在语法和解释器内部做了很多重大改进
- Python的特点：简洁、风格统一、简单易学、开源、可移植性好、库丰富、通用灵活、具有良好的中文支持
- Python的缺点：运行速度较慢
## 2.Python解释器的安装与程序的运行
- Python官网：https://www.python.org/
- 勾选add python.exe to PATH，将 Python解释器的安装路径自动添加到环境变量中
- 交互式运行
- 文件式运行
## 3.Python开发工具
- PyCharm，功能强大且流行的Python集成开发环境，用于开发大型的项目
- Sublime Text，轻量级但功能强大的文本编辑器
- Visual Studio Code，微软开发的一个跨平台的轻量级代码编辑器
- Jupyter Notebook，非常流行的交互式笔记本，适用于数据科学、机器学习和教育领域的程序开发和演示。
- Anaconda，开源的Python发行版本,专注于提供科学计算和数据分析所需的软件包和工具
## 4.Python模块
- 模块的安装  
pip工具(在线工具)安装第三方模块：  
`pip install 模块名`  
`pip install 模块名==版本号`  
`pip install 模块名1 模块名2 模块名 3...`
- 使用`pip list`命令查看当前开发环境中已经安装的模块
- 使用import语句导入模块：  
`import 模块1, 模块 2,...`
- 通过点字符“.”使用模块中的内容  
`模块.变量`  
`模块.函数`  
`模块.类`
- 如果不存在同名变量、函数或类,则可以使用`from 模块名 import...`直接将模块中的指定内容导入程序
- `from 模块名 import *`，导入指定模块的全部内容，不推荐
- 代码的组织方式：模块、包(包含多个模块的目录，需要包含__init__.py文件)、库(包含多个模块或包的集合)

# 第2章 Python基础知识
## 1.代码格式
- 注释  
`# 我是单行注释`  
`print('志当存高远)  # 我也是单行注释`
- 说明文档：主要用于说明函数或类的功能  
`"""`  
`函数或类的说明`  
`"""`
- 缩进  
确定代码之间的逻辑关系和层次关系  
首选——4个空格  
不允许混合使用空格和Tab键
- 语句换行  
在未结束的代码末尾加上“\”  
用()进行包裹
## 2.标识符与关键字
- 标识符：变量名、函数名、类名等  
Python中的标识符由字母、数字或下画线组成,且不能以数字开头  
Python中的标识符区分大小写。例如,andy和Andy是不同的标识符  
Python不允许使用关键字作为标识符  
见名知意，命名格式规范（变量名、函数名、模块名小写；常量名大写；类名首字母大写）
- 关键字：Python已经使用不允许开发人员重复定义的标识符  
全部存储在keyword模块的变量kwlist中,通过变量kwlist可获取
## 3.变量与数据类型
- 变量指能存储计算结果或表示值的抽象概念
程序在运行期间用到的数据会被保存在计算机的内存单元中,为了方便存取内存单元中的数据, Python使用标识符来标识不同的内存单元,从而在程序中通过标识符来引用和操作存储在内存单元中的数据。  
标识内存单元的标识符又称为变量名,Python通过赋值运算符“=”将内存单元中存储的数据与变量名建立联系,即定义变量  
`变量名 = 值`  
通过变量名访问存储在内存中与该变量关联的值
- 常用的数据类型  
数字：用于表示不同种类的数值数据，整数、浮点数、复数、布尔类型  
字符串：用于表示文本数据,由单引号、双引号或者三引号包裹一系列字符  
列表：保存任意数量、任意类型的元素  
元组：与列表类似，不可以被修改  
集合：与列表、元组类似，但元素之间没有特定的顺序，每个元素必须是唯一的  
字典：元素是“Key:Value”形式的键值对,键不能重复  
使用type()函数查看数据的类型
- 变量的输入与输出  
`input ([prompt])`  
`print (*objects, sep=' ', end='\n', file=None, flush=False)`  
*objects: 表示输出的数据。输出多个数据时,数据需要用英文逗号分隔
sep:可选参数,用于设定数据之间使用的分隔符,默认值为空格
end:可选参数,用于设定输出结果以什么结尾,默认值为换行符\n
fle:可选参数,表示数据要写入的文件对象,默认值为sys.stdout(表示标准输出文件,默认情况下程序会将结果输出到控制台)
flush:可选参数,表示是否刷新标准输出流,默认值为False(表示不刷新)
## 4.数字类型
- 整型  
`5      十进制数`，int(x)，将x转为十进制数  
`0b101  二进制数`，bin(x)，将x转为二进制数  
`0o5    八进制数`，oct(x)，将x转为八进制数  
`0x5    十六进制数`，hex(x)，将x转为十六进制数
- 浮点型  
可以直接用小数点的形式表示  
较大的实数用科学计数法  
`-3.14e10`，相当于-3.14×1010,结果为-31400000000
- 复数类型  
`complex_one = 1 + 2j`，#实部为1,虚部为2  
complex()函数创建复数，没有传入虚部则虚部默认为0  
`complex_one = complex(3,2)`，创建复数3+2j  
`complex_one.real`，获取复数的实部  
`complex_one.imag`，获取复数的虚部
- 布尔类型  
可以使用bool()函数检测数据的布尔值  
布尔值为False的常见情况：None；任何值为0的数字类型的数据,如0、0.0、0j；任何空的组合数据类型的数据,如空字符串、空元组、空列表、空集合、空字典  
- 数字类型转换  
`int(x[, basc])`，将x转为整数类型，base指定进制数  
`float(x)`，将x转换为浮点型  
`complex(x)`，将x转换为复数
## 5.运算符
- 算术运算符  
+，加法  
-，减法  
*，乘法  
/，除法  
//，整除  
%，取模  
**，幂  
在进行混合运算时Python会强制将数值的类型进行类型转换：  
(1)整型与浮点型进行混合运算时,将整型转化为浮点型  
(2)其他类型与复数类型进行运算时,将其他类型转换为复数类型
- 赋值运算符  
`=`  
`+=`  ，`num += 2`等价于`num = num+2`  
`-=`  ，`num = 2`等价于`num = num - 2`  
`\*=`  ，`num *= 2`等价于`num = num*2`  
`/=`  ，`num/= 2`等价于`num = num/2`  
`//=`  ，`num //= 2`等价于`num = num//2`  
`%=`  ，`num %= 2`等价于`num = num%2`  
`**=`  ，`num **= 2`等价于`num = num**2`  
海象运算符`:=`，用于在表达式内部同时为变量赋值和使用变量  
    ```python
    num_one = 1
    result = num_one + (num_two:=2)  # 使用海象运算符为变量num_two赋值2
    print (result)
    ```
- 比较运算符，通常用于布尔测试，测试结果只能是True或者False  
`==`，相等  
`!=`，不相等  
`>`，大于  
`<`，小于  
`>=`，大于等于  
`<=`，小于等于
- 逻辑运算符  
`and`，进行逻辑与运算  
`or`，进行逻辑或运算  
`not`，进行逻辑非运算
- 成员运算符  
用于检测给定数据是否存在于字符串、列表、元组、集合、字典等之中  
`in`，如果指定数据在上述数据类型中返回True,否则返回False  
`not in`，如果指定数据不在上述数据类型中返回True,否则返回False
- 位运算符  
对操作数的二进制位进行逻辑运算,操作数必须为整数  
`<<`，操作数按位左移，按位左移n位当于操作数乘2的n次方,  
`>>`，操作数按位右移，按位右移n位相当于操作数除以2的n次方并向下取整  
`&`，左操作数与右操作数执行按位与运算  
`|`，左操作数与右操作数执行按位或运算  
`^`，左操作数与右操作数执行按位异或运算  
`~`，操作数按位取反
- 运算符优先级  
如果表达式中包含小括号,那么解释器会先执行小括号包裹的子表达式  
幂运算**  
乘法*、除法/、取模%、整除//  
加法+、减法-  
按位右移>>、按位左移<<  
按位与&  
按位或|、按位异或^  
比较运算符  
成员运算符  
逻辑运算符  
复合赋值运算符  
赋值运算符

# 第3章 流程控制
## 1.条件语句
- if语句
    ```python
    score = 88
    if score >= 60:
        print("考试及格！")
    ```
- if-else语句
    ```python
    score = 88
    if score >= 60:
        print("考试及格！")
    else:
        print("考试不及格！")
    ```
- if-elif-else语句
    ```python
    score = 88
    if score >= 85:
        print("优秀")
    elif 75 <= score < 85:
        print("良好")
    elif 60 <= score < 75:
        print("中等")
    else:
        print("差")
    ```
- if嵌套
    ```python
    year = 2026
    month = 2
    if month in [1,3,5,7,8,10,12]:
        print(f"{month}月有31天")
    elif month in [4,6,9,11]:
        print(f"{month}月有30天")
    elif month == 2:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            print(f"{year}年{month}月有29天")
        else:
            print(f"{year}年{month}月有28天")
    ```
## 2.循环语句
- while语句
    ```python
    i= 1
    result = 0
    while i <= 10:
        result += i
        i += 1
    print(result)
    ```
- for语句，实现遍历循环
    ```python
    for word in "Python":
        print(word)
    ```
    range()函数，控制循环中代码的执行次数
    ```python
    for i in range(5):  # 输出0-4
        print(i)
    ```
    ```python
    for i in range(5,9):  # 输出5-8
        print(i)
    ```
- while循环嵌套
    ```python
    i = 1
    while i < 6:
        j = 0
        while j < i:
            print("*",end='')
            j += 1
        print()
        i += 1
    ```
- for循环嵌套
    ```python
    for i in range(1,7):
        for j in range(i):
            print('*',end='')
        print
    ```
## 3.跳转语句
- break语句
    ```python
    for word in 'Python':
        if word == 'o':
            break  # 结束循环
        print(word,end='')
    ```
- continue语句
    ```python
    for word in 'Python':
        if word == 'o':
            continue  # 跳出本次循环
        print(word,end='')
    ```

# 第4章 字符串控制
## 1.字符串
- 字符串是由一系列字符组成的不可变序列，使用单引号、双引号、三引号定义字符串
- 转义字符  
`\b`，退格符，用于删除光标前面的一个字符  
`\n`，换行符  
`\v`，纵向制表符  
`\t`，横向制表符  
`\r`，回车符，用于将光标移至当前行的起始位置  
`print('转义字符中:\n 表示换行;\r 表示回车;\b 表示退格')`  
转义字符中:  
表示回车表示退格&nbsp;&nbsp;#&nbsp;“表示回车”到了行首；“表示换行;”被覆盖了；“表示回车”和“表示退格”之间的“;”消失了
## 2.使用%格式化字符串
- `format % values`  
- `%[flags][width][.precision]type`  
format表示一个字符串，该字符串中可以插入单个或多个为真实数据占位的格式符  
values表示单个或多个真实数据,多个真实数据以元组的形式进行存储  
%代表执行格式化操作,即将format中的格式符替换为values
`%s`，格式化为字符串  
`%d`，格式化为有符号的十进制数  
`%o`，格式化为有符号的八进制数  
`%x`，格式化为有符号的十六进制数  
`%f`，格式化为浮点数，可指定浮点数精度，默认6位小数  
`%e`，格式化为科学计数法表示的浮点数，e小写  
`%E`，格式化为科学计数法表示的浮点数，E大写  
`%c`，用于将对应的数据(整数或包含单个字符的字符串)格式化为字符
    ```python
        value = 10
        format_str = '我今年%d岁了' % value
        print(format_str)
    ```
    ```python
    name = '小明'
    age = 27
    address = '北京市昌平区'
    print('我叫%s，今年%d岁，来自%s。' % (name,age,address))
    ```
## 3.使用format方法格式化字符串
- `str.format (values)`  
    ```python
    name = '小明'
    age = 27
    address = '北京市昌平区'
    string = '我叫{}，今年{}岁，来自{}'
    print(string.format(name,age,address))
    ```
    ```python
    name = '小明'
    age = 27
    string = '我叫{1},今年{0}岁了'  # 字符串中插入两个符号{},并在{}中指定编号
    print (string.format(age,name))  # 从0开始计数，age为0，name为1
    ```
    ```python
    name = '小明'
    age = 27
    # 字符串中插入两个符号{},并在{}中指定变量名
    string = '我叫{arg_one},今年{arg_two}岁了'
    # 使用format()方法格式化字符串
    print (string.format(arg_one=name, arg_two=age))
    ```
## 4.使用f-string格式化字符串
- ```python
    name = '小明'
    age = 27
    string = f'我叫{name},今年{age}岁了'
    print (string)
    ```
- ```python
    num1 = 9
    num2 = 6
    string = f"{num1}x{num2}={num1 * num2}"  # 号{}中可以嵌入变量、表达式等
    print (string)
    ```
- ```python
    value = 3.141592653589793
    print (f'n 的值为: {value:.2f}')  # 使用英文冒号为变量的值指定格式化的规则
    ```
## 5.字符串的查找与替换
- 字符串查找  
find()方法，可查找字符串中是否包含子串,若包含子串则返回子串首次出现的位置的索引,否则返回-1  
`find(sub[,start,[,end]])`  
sub:用于指定要查找的子串  
start:用于指定查找的开始索引，默认值为0  
end:用于指定查找的结束索引，默认值为字符串的长度
在指定范围内只返回第一个子串的位置，即使范围内有多个匹配  
如果想找所有匹配位置需要自己写循环逻辑：循环查找/使用正则表达式
    ```python
    words = "与其临渊羡鱼，不如退而结网"
    result_one = words.find("鱼")
    print(result_one)
    result_two = words.find("与"[,6])
    print(result_two)
    ```
- 字符串替换  
replace()方法，用于将当前字符串中的指定旧子串替换成新子串,可以指定替换次数,并返回替换后的新字符串  
`replace(old, new[, count])`  
old:表示被替换的旧子串  
new:表示用于替换旧子串的新子串  
count:表示替换旧子串的次数，默认替换所有的旧子串
    ```python
    old_string = "All things Are difficult before they Are easy."
    new_string = old_string.replace("Are", "are")
    print(new_string)
    ```
## 6.字符串的分割与拼接
- 字符串分割  
split()方法，用于根据指定分隔符对字符串进行分割,分割后返回一个列表,该列表中保存多个子串  
`split(sep=None, maxsplit=-1)`  
sep:表示分隔符，默认值为空格，也可被设置为其他字符  
maxsplit:分割次数，默认值为-1表示不限制分割次数
分隔符本身不会出现在结果中
    ```python
    string_example = "The more efforts you make, the more fortune you get."
    print(string_example.split())  # 根据空格分割字符串
    print(string_example.split('m'))  # 根据m分割字符串
    print (string_example.split('e', 2))  # 根据e分割字符串，并且分割2次
    ```
- 字符串拼接  
join()方法，用于将某个字符串作为连接符,通过连接符拼接可迭代对象的每个元素,并返回一个新的字符串。可迭代对象可以是字符串、列表、元组、集合、字典  
`join(iterable)`  
interable:表示可迭代对象  
    ```python
        symbol = 1*1
        world = 'Python'
        print (symbol.join (world))
    ```
    Python中还可以使用运算符“+”将两个字符串拼接成一个字符串
## 7.删除字符串的指定字符
- strip()，删除字符串头部和尾部指定的字符，默认删除空格
- lstrip()，删除字符串头部指定的字符，默认删除空格
- rstrip()，删除字符串尾部指定的字符，默认删除空格
## 8.字符串大小写转换
- upper()，将字符串中的小写字母全部转换为大写字母
- lower()，将字符串中的大写祖母全部转换成小写字母
- title()，将字符串中每个单词的首字母大写，其余字母小写
- capitalize()，将字符串中第一个字母大写，其他字母小写
## 9.字符串对齐
- `center(width[,fillchar])`，使用fillchar填充字符串至指定长度,原字符串居中显示
- `ljust(width[,fillchar])`，使用fillchar填充字符串至指定长度,原字符串左对齐显示
- `rjust(width[,fillchar])`，使用fillchar填充字符串至指定长度,原字符串右对齐显示
    ```python
    sentence = 'hello world'
    center_str = sentence.center(13,'-')  # 字符串长度为13，居中显示，使用-填充
    ljust_str = sentence.ljust(13, '*')  # 字符串长度为13，左对齐，使用*填充
    rjust_str = sentence.rjust(13, '%')  # 字符串长度为13，右对齐，使用%填充
    print (f"居中显示:{center_str}")
    print (f"左对齐显示: {ljust_str}")
    print (f"右对齐显示: {rjust_str}")
    ```
- f-string方法对齐  
{s:<5}，左对齐长度到5，右边字符  
{s:>5}，右对齐长度到5，左边补字符  
{s:^5}，居中对齐长度到5，两边补字符  
{s:-<5}，右边补指定字符“-”长度到5  
{n:03d}，补零（数字专用）

# 第5章 组合数据类型
## 1.认识组合数据类型
- 序列类型：字符串（string）、列表（list）、元组（tuple）  
来源于数学概念中的数列  
正向索引（从0开始从左往右依次递增）；反向索引（从-1开始从右往左依次递减）
- 集合类型：确定性（不可变数据类型）、互异性、无序性
- 映射类型：以键值对的形式存储元素,键值对中的键与值之间存在映射关系，字典
## 2.列表
- 创建列表  
使用[]创建列表  
使用list()函数创建列表
    ```python
    # 创建空列表,结果为[]
    li_one = list()
    # 根据字符串创建列表,结果为['p', 'y', 't', 'h', 'o', 'n']
    li_two = list('python')
    #根据另一个列表创建列表,结果为[1, 'python']
    li_three = list([1, 'python'])
    ```
    可迭代对象：支持通过for,in语句获取其内部元素的对象。可以从collections.abc模块中导入Interable函数类，使用inistance()函数判断一个对象是不是可迭代
- 访问列表元素  
通过索引访问列表元素，`list[n]`  
通过切片访问列表元素，`list[m:n:step]`  
通过for循环依次访问列表元素
- 添加列表元素  
append()方法，在列表末尾添加新元素，直接操作返回None  
extend()方法，将另一个序列中的每个元素逐个添加到列表的末尾  
insert()方法，在列表的指定位置插入一个新元素，插入位置后的元素依次向后移动
- 列表元素排序  
1. sort()，按特定顺序对列表中的所有元素进行排序  
`sort(key=None, reverse=False)`  
key：用于指定排序规则
reverse：用于控制列表元素排序的方式，True表示降序排列，False表示升序排列  
使用sort()方法对列表元素排序后,排序后的元素会覆盖列表原有的元素,不产生新列表
2. sorted()，用于按升序的方式排列列表元素，该函数的返回值是升序排列后的新列表，不会对原列表产生影响
3. reverse()，用于逆置列表，即把列表中的元素从右向左依次排列
- 删除列表元素  
1. del语句，用于删除列表中指定位置的元素，也可以删除整个列表
    ```python
    names = ['小明','小红','小兰']
    del names[0]
    print(names)
    del names
    print(names)
    ```
2. remove()方法，用于删除列表中的某个元素，若有多个匹配元素只删除第一个
    ```python
    chars = ['h', 'e', 'l', 'l', 'e']
    chars.remove('e')
    print(chars)
    ```
3. pop()方法，用于删除列表中指定位置的元素,并返回被删除的元素。若未指定具体元素,则该方法会删除列表中的最后一个元素
    ```python
    numbers = [1, 2, 3, 4, 5]
    print(numbers.poр())
    print(numbers.pop(1))
    print(numbers)
    ```
    如果指定位置超出了列表的长度,则会导致程序出错
4. clear()方法，用于清空列表中的所有元素，将列表转变为空列表
- 列表推导式  
用于以简洁的方式根据已有的列表构建满足特定需求的列表  
`[表达式 for 临时变量 in 目标对象]`  
1. 带if语句的列表推导式  
`[表达式 for 临时变量 in 目标对象 if 判断条件]`
    ```python
    ls = [1, 2, 3, 4, 5, 6, 7, 8]
    new_ls = [temp for temp in ls if temp > 4]
    print(new_ls)
    ```
2. 带if-else语句的列表推导式  
`[表达式1 if 判断条件 else 表达式2 for 临时变量 in 目标对象]`
    ```python
    ls = [1, 2, 3, 4, 5, 6, 7, 8]
    new_ls = [temp if temp % 2 == 0 else temp + 1 for temp in ls]
    print(new_ls)
    ```
3. 带for循环嵌套的列表推导式  
`[表达式 for 临时变量1 in 目标对象1 for 临时变量2 in 目标对象2]`
    ```python
    ls_one = [1, 2, 3]
    ls_two = [3, 4, 5]
    ls_three = [x + y for x in ls_one for y in ls_two]
    print(ls_three)
    ```
## 3.元组
- 一组包含在小括号“0”中、由英文逗号分隔的元素,元素的个数、类型不受限制  
- 使用小括号可以直接创建元组  
- 若元组中只有一个元素,则该元素之后的英文逗号是不能省略的  
- 使用内置函数tuple()也可以创建元组。当该函数接收的参数为空时会创建一个空元组,当该函数接收的参数为可迭代对象时会创建非空元组  
`t1 = tuple()`  
`t2 = tuple([1, 2, 3])`
- 通过索引与切片的方式访问元组的元素,也可以通过循环依次访问元组的元素
    ```python
    t2 = tuple([1, 2, 3])
    t3 = tuple('python')
    print (t2[1])  # 以索引的方式访问元组元素
    print (t3[2:5])  # 以切片的方式访问元组元素
    for data in t3:  # 通过循环遍历元组的元素
    print(data,end='')
    ```
- 元组是不可变的数据类型,元组创建以后其内部的元素不能被修改,因此元组不支持添加元素、删除元素和元素排序等一些会修改元素的操作
## 4.集合
- 创建集合
一组包含在大括号“{}”中、由英文逗号“”分隔的元素。使用{}可以直接创建集合  
使用内置函数set()可以创建集合,如果该函数的参数列表为空,则创建的是一个空集合  
用{}不能创建空集合,空集合只能利用set()函数创建
- 集合的常见操作  
add(x)，向集合中添加x，x已存在时不做处理  
remove(x)，删除集合中的元素x，若x不存在抛出KeyError错误  
discard(x)，删除集合中的元素x，若x不存在不做处理  
pop()，随即返回集合中的一个元素，同时将该元素从集合中删除。若集合为空，抛出KeyError错误  
clear()，清空集合  
copy()，复制集合，返回值为集合  
isdishint(T)，判断当前集合和集合T是否包含相同的元素，如果不包含返回True，包含返回False
- 集合推导式  
`{表达式 for 临时变量 in 目标对象 if 判断条件}`
```python
ls = [1,2,3,4,5,6,7,8]
s = {data for data in ls if data % 2 == 0}
print(s)
```
## 5.字典
- 创建字典  
字典的值可以是任意类型的数据，键可以是任意不可变类型的对象  
字典中的元素无序，且键必须唯一  
使用{}可以直接创建字典  
使用内置函数dict()创建字典
- 字典的访问  
可以使用字典的键访问其对应的值  
`字典变量[键]`  
内置方法get()，可以根据键从字典中获取对应的值，若指定的键不存在则返回指定的默认值  
`d.get(key[, default])`  
key表示要获取值的键；defaulr是可选参数，未指定默认值则返回None  
`字典变量.keys()`，获取所有键  
`字典变量.values()`，获取所有值  
`字典变量.items()`，获取所有元素，返回的都是可迭代对象
- 字典元素的添加
`字典变量[键] = 值`  
update()方法可以一次性给字典添加多个元素  
`update([other])`，other可以是字典、可以是键值对元组组成的可迭代对象[('b',3),('c',4)]、可以是形如“键1=值1， 键2=值2， ...”的值
- 字典元素的修改  
本质是通过键获取值，并重新对元素进行赋值  
使用update()方法
- 字典元素的删除  
pop()方法，根据指定键删除字典中的指定元素，若删除成功则返回被删除元素的值  
popitem()方法，随机删除字典中的一个元素，返回被删除的元素  
clear()方法，清空字典中的元素
- 字典推导式  
`{键的表达式:值的表达式 for 临时变量 in 目标对象}`  
字典推导式也支持if语句和for循环
## 6.组合数据类型使用运算符
- “+”运算符，进行变量的拼接
- “*”运算符，字符串、列表和元组可以和整数进行乘法运算，运算后产生的新变量为原变量重复整数次的结果
- “in”“not in”运算符，字符串、列表、元组、集合、字典都支持成员运算符

# 第6章 函数
- 函数式编程将代码模块化，可减少冗余代码，使程序结构更加清晰
## 1.函数的定义和调用
-   ```python
    def 函数名([参数列表]):
        ["""文档字符串"""]
        函数体
        [return语句]
    ```
- 语法格式说明：  
关键字def，用于标记函数的开始  
函数名，函数唯一的标识，其命名遵循标识符的命名规则  
参数列表，负责接收传入函数中的数据，可以包含一个或多个参数，也可以为空  
冒号，用于标记函数体的开始  
文档字符串，由一对三引号包裹的、用于说明函数功能的字符串，可以省略  
函数体，实现函数功能的具体代码  
return语句，用于将函数的处理结果返回给函数的调用方，同时也标记函数的结束，若函数没有返回值可以省略
- 调用函数  
`函数名([参数列表])`  
函数内部也可以调用其他函数，称为嵌套调用
- 在定义函数时，可以在其内部嵌套定义另一个函数。在函数外部无法直接调用内层函数，只能在外层函数中调用内层函数
## 2.函数参数的传递
- 形式参数(形参)：定义函数时设置的参数
- 实际参数(实参)：调用函数时设置的参数
- 位置参数的传递  
实参的数量和位置必须与函数定义中位置参数的数量和位置保持一致
- 关键字参数的传递  
- 使用符号“/,”来限定部分形参只能接收通过位置参数的传递方式传递的实参
    ```python
    def func(a, b, /, c):  # 使用/限制前面的a和b只能用位置参数传递
        print(a, b, c)
    ```
- 使用符号“*,”限定后面的参数只能通过关键字参数传递
    ```python
    def func(*, a, b):   # ✨ 这是分隔符，不是打包！
        print(a, b)
    func(a=1, b=2)
    ```
- 默认参数的传递  
定义函数时可以指定形参的默认值
- 参数的打包  
打包：将多个实参打包成一个元组或字典,在函数调用时将其作为一个整体传递给形参  
如果形参的前面加上“\*”,那么它可以接收以元组形式打包的多个值，建议使用*args  
如果形参的前面加上“\**”,那么它可以接收以字典形式打包的多个值，建议使用**kwar
    ```python
    def test(**kwargs):
        print(kwargs)
    ```
- 参数的解包  
解包：使用特殊语法将元组或字典拆分为多个值并赋给对应的形参  
如果函数在调用时接收的实参是元组类型的数据,那么可以使用“*”将元组拆分成多个值,并按照位置参数的传递方式赋给对应的形参  
如果函数在调用时接收的实参是字典类型的数据,那么可以使用“**”将字典拆分成多个键值对,并按照关键字参数的传递方式赋给与键名称对应的形参
    ```python
    def test(a, b, c, d, e) :
        print (a, b, c, d, e)
    nums = {"a":11, "b":22, "c":33, "d":44, "e":55}
    test(**nums)
    ```
- 混合传递  
传递方式按优先级为位置参数、关键字参数、默认参数、打包传递
    ```python
    def test(a, b, c=33, *args, **kwargs):
        print(a, b, c, args, kwargs)
    test(1, 2)
    test(1, 2, 3)
    test(1, 2, 3, 4)
    test(1, 2, 3, 4, e=5)
    ```
## 3.函数的返回值
- 函数中的return语句会在函数结束时将数据返回给程序,同时让程序回到函数被调用的位置继续执行
    ```python
    def filter_sensitive_words(words):
        if "山寨" in words:
            new_words = words.replace ("山寨", "**")
            return new_words
    ```
    如果函数使用return语句返回了多个值,那么这些值将被保存到元组中
## 4.变量作用域
- Python变量并不是在哪个位置都可以访问,具体的访问权限取决于变量定义的位置,变量的有效范围视为变量的作用域,作用域决定了在哪些位置能够访问变量
- 局部变量  
局部变量是指在函数内部定义的变量,它的作用域仅限于函数内部,只能在函数内部对它进行访问或使用。一旦函数执行结束,局部变量将无法被访问或使用
    ```python
    def test_one():
        number = 10
        print(number)
    test_one()
    print(number)  # NameError: name 'number' is not defined
    ```
    不同函数内部可以包含同名的局部变量，他们相互独立、互不影响
- 全局变量
全局变量是指在整个程序中都可以使用的变量,它们一般定义在函数外部,并且在整个程序运行期间占用存储单元  
全局变量可以在程序的任意位置被访问  
全局变量在函数内部只能被访问,而无法被直接修改
- LEGB原则  
L(Local):局部作用域，例如在函数内部定义的局部变量和形参的作用域  
E(Enclosing):嵌套作用域，例如在嵌套函数中外层函数声明的变量的作用域  
G(Global):全局作用域，例如在模块中定义变量的作用域  
B(Built-in):内置作用域，例如Python内置的模块或函数中声明的变量的作用域
- global关键字  
global关键字用于在函数内部声明一个全局变量,并允许在函数内部对该全局变量进行修改
```python
number = 10
def test_one():
    global number
    number += 1
    print(number)
test_one()
print(number)
```
- nonlocal关键字  
如果在嵌套函数内部访问和修改外层函数中的变量,而不是创建新的局部变量,可以使用nonlocal关键字
```python
def test():
    number = 10
    def test_in():
        nonlocal number
        number = 20
    test_in()
    print(number)
test()
```
## 5.特殊形式的函数
- 递归函数  
函数内部调用了自身,则这个函数被称为递归函数  
递归函数通常用于解决结构相似的问题,它采用递归的方式,将一个复杂的大型问题转化为与原问题结构相似的、规模较小的若干子问题,之后对最小化的子问题求解,从而得到原问题的解  
递归函数在定义时需要满足两个基本条件:一个是有递归公式,另一个是有边界条件  
递归公式描述如何通过解决子问题来解决原问题  
边界条件是最小化的子问题,也是递归结束的条件  
(1)递推：递归的执行基于上一次的运算结果,将问题规模逐渐缩小,通过不断调用自身来求解子问题,这一阶段也称为递归调用  
(2)回溯：当递归达到边界条件时,递归开始,逐级返回函数调用过程中得到的结果,将得到的部分结果组合成最终的解
    ```python
    def 函数名([参数列表])：
        if 边界条件:
            return 结果
        else:
            return 递归公式
    ```
    ```python
    def func(num) :
        if num == 1:
        return 1
        else:
        return num * func (num - 1)
        num = int (input ("请输入一个整数:"))
        result = func(num)
        print("5!=%d"%result)
    ```
- 匿名函数  
匿名函数是一类不需要命名的函数,它与普通函数一样可以在程序的任何位置使用  
`lambda <形参列表>:<表达式>`  
定义好的匿名函数不能直接使用,最好使用一个变量保存它,以便后期可以随时使用这个函数   
`temp = lambda x : pow(x, 2)`
# 第7章 文件与数据格式化
## 1.文件概述
- 文件标识  
1. 路径  
路径是文件在计算机中的位置表示,用于指明文件所在的目录结构,以帮助操作系统定位文件  
路径可以分为相对路径或绝对路径
2. 文件名主干  
文件名主干通常是用于描述文件的内容、用途或其他相关信息的字符串,有助于用户识别和区分不同的文件
3. 扩展名  
扩展名是文件名中表示文件类型或格式的部分,用于帮助操作系统和应用程序辨识和处理不同种类的文件,通常紧跟在文件名主干之后
- 文本文件  
文本文件是由字符组成的文件,包含可被人类读取和理解的文本信息  
一般情况下以纯文本形式存储,并使用ASCII、Unicode或其他编码方式来表示其中的字符。常见的文本文件格式包括TXT、CSV、XML、HTML、JSON等
- 二进制文件  
二进制文件是由字节组成的文件，以二进制形式存储数据,包含计算机能够直接解读和处理的信息  
二进制文件可以包含各种类型的数据,如图像、音频、视频等,这类文件不能直接使用文字处理程序正常读写,必须使用相关程序才能正确获取文件信息
- Python的sys模块中定义了3个标准文件,分别为stdin(标准输入文件)、stdout (标准输出文件)和stderr(标准错误文件)  
标准输入文件对应输入设备,如键盘;标准输出文件和标准错误文件对应输出设备,如显示器  
每个终端都有其对应的标准文件,这些文件在终端启动的同时打开  
在Python解释器中导入sys模块后便可对标准文件进行操作
    ```python
    import sys
    file = sys.stdout
    file.write("hello")
    ```
    以上代码将标准输出文件赋给文件对象file,又通过文件对象file调用内置方法write()向标准输出文件中写入数据。程序执行后,字符串"hello"将被写入标准输出文件,即输出到终端
## 2.文件的基础操作
- 打开文件  
内置函数open()用于打开文件并返回相应的文件对象  
`open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`  
file，指定文件名或者文件路径  
mode，设置文件的打开模式，r(读取)，w(写入)，a(追加)，可以与b，+组合使用  
encoding，指定文件的编码方式，默认为None(系统默认的编码方式)  
若open()函数成功打开文件,则会返回一个文件对象
- 关闭文件  
close()方法：  
close()方法是为文件对象提供的方法,用于关闭已经打开的文件  
`file.close()`  
with语句：  
如果打开文件与关闭文件之间的操作较多,容易遗漏关闭文件操作,使用with语句预定义清理操作,实现文件的自动关闭
    ```python
    with open(文件路径, 打开模式) as 变量名:
        代码段
    ```
- 读取文件  
1. read()方法：  
`read(size=-1)`  
size用于指定从文件中读取的数据的字节数或字符数，默认值为-1，表示一次性读取所有数据
    ```python
    with open('test.txt', 'r', encoding='utf-8') as file:
        result = file.read(3)   # 读第1-3个字符
        print(result)
        result = file.read(3)   # 读第4-6个字符
        print(result)
        result = file.read()    # 读剩下的所有字符
        print(result)
    ```
2. readline()方法：  
readline()方法用于从指定文件中读取一行数据,并保留该行数据末尾的换行符\n  
`readline()`  
    ```python
    with open('test.txt') as file:
        result = file.readline() # 第1次读取,读取第1行数据
        print (result)
        result = file.readline() # 第2次读取,读取第2行数据
        print (result)
        result = file.readline ()# 第3次读取,读取第3行数据
        print (result)
        result = file.readline() # 第4次读取,读取第4行数据
        print (result)
    ```
3. readlines()方法：  
readlines()方法用于一次性读取文件中的所有数据,若读取成功返回一个列表,文件中的每一行对应列表中的一个元素  
`readlines(hint=-1)` 
- 写入文件
1. write()方法可以将字符串写入文件  
`write(data)`
    ```python
    string = "Nothing in the world is difficult"\
            "for one who sets his mind to it."
    with open('write_file.txt', mode='w') as file:
        size = file.write(string)
        print (size)
    ```
2. writelines()方法用于将字符串或字符串列表写入文件  
`writelines (lines)`
    ```python
    string_list = ["Interest is the best teacher!\n",
                   "Interest is the best teacher!\n",
                   "Interest is the best teacher!"]
    with open('write file.txt', mode='w') as file:
    file.writelines(string_list)
    ```
- tell()方法  
tell()方法用于获取文件当前的读写位置,会返回一个表示文件读写位置的整数,这个整数以字节为单位
    ```python
    with open('write_file.txt') as file:
        read location = file.tell()  # 获取文件读写位置
        print (read_location)
        file.read (5)
        read location = file.tell()
        print (read location)
    ```
- seek()方法  
用于移动文件读写位置到指定的位置,以便用户能够从任意位置开始读写文件  
`seek(offset, whence=os.SEEk_SET, /)`  
offset表示偏移量,即文件读写位置需要移动的字节数,它的取值可以为正数、负数或0,其中正数表示相对于指定位置向文件末尾移动的字节数,负数表示相对于指定位置向文件开头移动的字节数,0表示不移动,即保持位置不变  
whence用于指定偏移量的参考位置,该参数支持的取值及其代表的含义分别如下：os.SEEK_SET或0:，默认值,表示从文件开头位置开始偏移；os.SEEK_CUR或1:，表示从当前位置开始偏移；os.SEEK_END或2:，表示从文件末尾位置开始偏移
    ```python
    with open('write_file.txt') as file:
        read_location = file.seek(5, 0)
        print(read_location)
        result = file.read(3)
        print(result)
    ```
    只能在from参数值为0的情况下从文件开头位置开始移动文件读写位置,而不能在from参数值为1或2的情况下进行相对移动,这样会导致程序出现错误  
    若要相对于当前的文件读写位置或文件末尾移动文件读写位置,则需要以二进制读取的方式打开文件
## 3.文件与目录管理
- os模块常用函数  
- remove()，删除文件  
`os.remove(path)`  
 path表示待删除文件的路径
- rename()，重命名目录或文件  
`os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)`  
src:表示旧的目录名或文件名  
dst:表示新的目录名或文件名  
src_dir_fd: 表示旧目录或文件对应的文件描述符  
dst_dir_fd: 表示新目录或文件对应的文件描述符
- mkdir()，创建目录  
`os.mkdir('dir')`
- rmdir()，删除目录  
`os.rmdir('dir')`
- getcwd()  
`result = os.getcwd()`  
`print(result)`
- chdir()，更改默认目录  
若对文件或文件夹进行操作时传人的是文件名而非路径, Python解释器会从默认目录中查找指定文件,或在默认目录下创建新的文件  
若没有特别设置,当前目录即为默认目录  
`os.chdir('E:\\')`  
`result = os.getcwd()`  
`print(result)`
- listdir()，获取文件名列表  
`dirs = os.listdir('./')`
`print (dirs)`
## 4.数据维度与数据格式化
- 一维数据
- 二维数据(表格数据)
- 多维数据
- 一维和二维数据的存储  
通用的一维数据和二维数据的存储格式为CSV  
CSV文件以纯文本形式存储表格数据,文件的每一行对应表格中的一条数据记录,每条记录由一个或多个字段组成
- 一维和二维数据的读取
    ```python
    csv_file = open('score.csv')
    lines = []
    for line in csv_file:
        line = line.replace('\n', '')
        lines.append(line.split(','))
        print (lines)
    csv_file.close()
    ```
- 一维和二维数据的写入
- 多维数据的格式化  
JSON是一种常见的轻量级数据交换格式,JSON格式的数据本质上是一种格式化的字符串,既易于被人们阅读和编写,也容易被机器解析和生成  
JSON 格式的数据遵循以下语法规则:  
(1)数据存储在键值对中,例如"姓名"张华”  
(2)数据的字段由英文逗号分隔,例如"姓名":"张华","语文":"116"  
(3)一个大括号保存一个JSON对象,例如{"姓名":"张华","语文":"116"}  
(4)一个中括号保存一个数组,例如[{"姓名":"张华","语文":"116"}]  
网络平台也会使用XML、HTML等格式组织多维数据,XML和HTML格式通过标签组织数据

# 第8章 面向对象
## 1.类与对象的基础应用
- 类的定义  
类是现实中具有共同特征的一些事物的抽象，对象是类的实例  
程序中的每一个类都有一个名称，并且包含描述类特征的数据成员（属性），以及描述类行为的成员函数（方法）  
    ```python
    class 类名:
        属性名 = 属性值
        def 方法名(self, 参数1, 参数2, ...)
            方法体
    ```
- 对象的创建与使用  
类需要实例化为对象才能实现其意义  
`对象名 = 类名()`  
通过对象名访问对象的属性和调用对象的方法  
`对象名.属性名`  
`对象名.方法名(参数1, 参数2, ...)`
## 2.类的成员
- 属性  
属性用于表示类所拥有的状态或特征  
类属性指的是定义在类内部、方法外部的属性：共享性；持久性；便携性  
    ```python
    class Car:
        wheels = 4
    car = Car()
    print(Car.wheels)
    print(car.wheels)
    Car.wheels = 3
    print(Car.wheels)
    print(car.wheels)
    car.wheels = 4
    print(Car.wheels)
    print(car.wheels)
    ```
实例属性指的是在方法内部通过`self.属性名`定义的属性
## 3.特殊方法
## 4.封装
## 5.继承
## 6.多态
## 7.运算符重载

# 第9章 异常
## 1.异常概述
## 2.异常捕获语句
## 3.抛出异常
## 4.自定义异常

# 第10章 Python计算生态与常用库
## 1.Python计算生态概览
## 2.Python生态库的构建与发布
## 3.常见的内置库
## 4.常用的第三方库
