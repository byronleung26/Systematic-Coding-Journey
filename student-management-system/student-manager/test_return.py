import re
all_students = []
def insert():
    """录入学生信息功能"""
    mark = True  # 是否继续添加
    while mark:
        id = input("输入ID：")
        if not id:  # ID为空，跳出循环
            break
        name = input("输入姓名：")
        if not name:  # 姓名为空，跳出循环
            break
        math = input("输入数学成绩：")
        english = input("输入英语成绩：")
        chinese = input("输入语文成绩：")
        # 将信息保存到字典
        student = {'name':name,'id':id,'math':math,'english':english,'chinese':chinese}
        all_students.append(student)  # 将学生字典加入列表
        while True:
            inputmark = input("是否继续添加（输入y或n）")
            if inputmark == 'y':  # 输入正确，跳出循环
                mark = True
                break
            elif inputmark == 'n':  # 输入正确，跳出循环
                mark = False
                break
            else:  # 输入错误，会继续循环
                print("输入错误，请重新输入y或n")
    save()
    print("学生信息录入完毕")
def save():
    """将学生信息保存到文件"""
    file = open("students.txt", "w", encoding="utf-8")  # 打开文件准备写入
    # 遍历所有学生，写入文件
    for student in all_students:  # students是全局的学生列表
        # 把每个学生的信息写一行
        line = f"{student['id']},{student['name']},{student['math']},{student['english']},{student['chinese']}\n"
        file.write(line)
    file.close()  # 关闭文件
    print("✅ 学生信息已保存到 students.txt")
def menu():
    """显示主菜单"""
    print("""
    ——————————学生信息管理系统——————————

      ============功能菜单============

      1.录入学生信息
    
      0.退出系统
      ================================
      说明：通过数字选择菜单，回车确认
    ————————————————————————————————————
    """)
# 主要业务流程
def main():
    """主函数"""
    ctrl = True  # 标记是否退出系统
    while (ctrl):
        menu()  # 显示菜单（调用menu函数）
        option = input("请选择：")  # 选择菜单项
        option_str = re.sub("\D","",option)  # 输入中的非数字替换成空字符串
        if option_str in ['0','1']:  # 检查输入是不是有效的选项（0-1）
            option_int = int(option_str)  # 字符串转换成整型
            if option_int == 0:  # 选择0：退出系统
                print("您已退出学生信息管理系统")
                ctrl = False
            elif option_int == 1:  # 选择1：执行插入（录入）功能
                insert()
        else:
            print("输入错误，请输入0-1之间的数字")  # 输入错误提示
            input("按任意键继续...")  # 暂停让用户看到提示
if __name__ == "__main__":
    main()  # 调用主函数启动程序