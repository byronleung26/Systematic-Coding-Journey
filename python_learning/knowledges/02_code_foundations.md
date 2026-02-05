# 知识点
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

# 实操收获
1. 在#后面空格再添加相应说明文字，注释与代码之间至少两个空格
2. 4个空格是首选的缩进方法
3. 标识符应具有明确的含义  
   变量名使用小写的单个单词或由下画线连接的多个单词，如name/native_place  
   常量名使用大写的单个单词或由下画线连接的多个单词，如ORDER_LIST_LIMIT  
   模块名、函数名使用小写的单个单词或由下画线连接的多个单词，如low_With_under  
   类名使用以大写字母开头的单个或多个单词，如Cat、Capworld
4. 通过type()函数查看变量所存储的数据的具体类型
5. 变量就像贴标签的盒子，用来存放数据
6. input()永远返回字符串，需要时要用int()或float()转换
7. print()可以输出文字、变量，还能用f-string格式化