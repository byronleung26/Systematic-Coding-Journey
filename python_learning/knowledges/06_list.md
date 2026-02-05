# 知识点
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

# 实操收获
1. 避免不必要的列表创建