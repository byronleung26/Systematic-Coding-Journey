# 学习内容
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