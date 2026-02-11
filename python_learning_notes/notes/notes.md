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

## 6.组合数据类型使用运算符

# 第6章 函数
## 1.函数概述
## 2.函数的定义和调用
## 3.函数参数的传递
## 4.函数的返回值
## 5.变量作用域
## 6.特殊形式的函数

# 第7章 文件与数据格式化
## 1.文件概述
## 2.文件的基础操作
## 3.文件与目录管理
## 4.数据维度与数据格式化

# 第8章 面向对象
## 1.面向对象概述
## 2.类与对象的基础应用
## 3.类的成员
## 4.特殊方法
## 5.封装
## 6.继承
## 7.多态
## 8.运算符重载

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
