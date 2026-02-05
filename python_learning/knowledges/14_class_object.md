# 学习内容
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

# 实操收获
1. 创建.py文件时，名字里用了/，导致系统把它当成了文件夹
2. 写代码时下意识把input()写成了print()
3. 想把列表包起来，误用{}，导致语法错误
4. 面向对象编程（OOP）核心思想：封装。把数据（属性）和操作数据的函数（方法）捆绑在一起
5. 属性设计哲学：参数 vs 内部初始化。不是所有属性都要放在__init__的参数里
6. 方法比直接赋值更专业。不要让外部随意修改关键数据，要通过方法加一层 “防护网”
7. ", ".join([str1, str2, str3])
8. Python不认识裸写的1010是二进制，必须用 0b前缀或int(..., 2)转换。bin()转二进制，hex()转十六进制