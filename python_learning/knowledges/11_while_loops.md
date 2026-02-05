# 学习内容
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
# 实操收获
1. 循环条件是在每次循环开始时检查的，不是在输入后立即检查
2. 如果程序出现奇怪的行为（比如无限循环），可以:打印变量值、检查拼写、使用IDE的拼写检查
3. 交互模式旧的循环还没有结束，修改后的代码无法运行
4. break， 立即退出整个循环
   continue，跳过本次循环剩余代码，继续下一次循环
5. 关键是要在循环内部重新获取输入，否则变量值永远不会变。
6. 空列表被视为False