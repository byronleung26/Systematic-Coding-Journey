# 打开原始文件（读）
csv_file = open('score.csv', 'r', encoding='utf-8')

# 打开新文件（写+读，w+会覆盖创建）
file_new = open('count.csv', 'w+', encoding='utf-8')

# 存储所有行数据的列表
lines = []

# 第1步：读取原始CSV所有行
for line in csv_file:
    line = line.replace('\n', '')   # 去掉换行符
    lines.append(line.split(','))   # 按逗号切分，变成列表

# 第2步：给表头加"总分"
lines[0].append('总分')

# 第3步：计算每个人的总分
for i in range(len(lines) - 1):     # 跳过表头
    idx = i + 1                     # 当前数据行索引
    sum_score = 0                  # 总分初始0
    
    # 遍历这一行的每一列
    for j in range(len(lines[idx])):
        # 如果是数字字符串（成绩）
        if lines[idx][j].isnumeric():
            sum_score += int(lines[idx][j])  # 累加
    
    # 把总分追加到这一行末尾
    lines[idx].append(str(sum_score))

# 第4步：打印到屏幕，同时写入新文件
for line in lines:
    print(line)                          # 屏幕显示
    file_new.write(','.join(line) + '\n') # 转成CSV格式写入

# 第5步：关闭文件
csv_file.close()
file_new.close()