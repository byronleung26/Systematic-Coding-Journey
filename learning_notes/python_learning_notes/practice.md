# 时间相关工具
1. time模块
```python
import time
# 打印本地的时间元组
print(time.localtime())
# 打印时间戳
print(time.time())
# 打印时间字符串
print(time.asctime())
```
2. 万年历
```python
import calendar
yy = int(input("输入年份: "))
calendar.setfirstweekday(firstweekday = 6)
calendar.prcal(yy, w=0, l=0, c=6, m=4)
```
3. 倒计时程序
```python
import datetime, time
# 获取当前时间，转换为int形式
now_time = datetime.datetime.now()
print("当前时间为:", now_time)
target = datetime.datetime.strptime(target_date, "%Y-%m-%d %H:%M:%S")
# 打印转换后的时间对象
print(" 目标时间：",target)
while True:
    # 实时获取时间
    now_time = datetime.datetime.now()
    # 对比两个时间的差距，Python 中时间的 datetime 类型可以直接对比
    if target > now_time:
        print(" 时间未到，当前时间：", now_time)
        # 延迟一秒执行，不用实时判定
        time.sleep(1)
    else:
    # 目标时间已到
        print(" 时间已到 ")
        break
```

# Python处理CSV文件
1. （Comma-Separated Values，CSV）文件
- CSV文件的开头无空白行，每一行在文件中也以行的形式显示
- 第一行可含列名或不含列名，如果含列名，则认为是文件的第一行
- 同行数据不跨行，数据之间无空行
- 数据之间以半角逗号作为分隔符
2. CSV文件的创建
```python
f = open("5-1-2-1.csv", "a+")
t_head = ["姓名", "性别", "年龄"]
t_body = ["张三", "男", "28", "李四", "女", "21", "王五", "男", "30"]
# 写表头
for i in t_head:
    f.write(i + ',')
f.write('\n')
# 写表体
j = 0
# 循环输出表体
while True:
    for i in range(len(t_head)):
        f.write(t_body[len(t_gead)*j+i] + ',')
    # 换行
    f.write('\n')
    j += 1
    if j*(len(t_head)) == len(t_body):  # !!!
        break
    f.close()
```
3. 使用CSV模块读取文件
```python
import csv
# 打开CSV文件
f = open("test.csv")
# 读取文件中的内容
reader = csv.reader(f)
for i in reader:
    print(i)  # 每1行转换为1个列表
```
4. 计算商品和库存的预期收益
```python
# 打开CSV文件
f = open("test.csv") 
# 读取文件中的内容
reader = csv.reader(f)
index = 0
new_csv = []
# 循环计算数据，并且放入新的列表中
for i in reader:
    temp = []
    for j in i:
        temp.append(j)  # ???——>把原来的内容加入列表
    if index == 0:
        temp.eppend("预期收益")  # ???——>表头增加1列“预期收益”
    else:
        temp.append(str((int(i[2]) - int(i[4])) * int(i[3])))  # ???看不懂——>是(价格-进价)*库存
    index += i
    # 构建新的列表
    new_csv.append(temp)
    print(new_csv)  # ???打印干嘛
# 关闭读取的文件
f.close()
# 写文件，注意打开文件时需要指定换行时不空行
f = open("5-1-2-2.csv", "a+", newline="")
# 创建写CSV文件对象
write = csv.writer(f)  # ???为什么要这样
## 将所有数据写入文件中
write.writerows(new_csv)  # write是个实例对象了，writerows可能是csv的方法
f.close()
```


