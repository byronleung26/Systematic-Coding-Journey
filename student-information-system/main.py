"""
学生信息管理系统 - 主程序入口
包含：功能菜单menu()、主程序main()
日期：2026-02-26
"""

from student_operations import insert, search, show

def menu():
    """功能菜单"""
    print('='*30)
    print("\033[95m学生信息管理系统\033[0m".center(30))
    print('-'*30)
    print('     1.录入学生信息')
    print('     2.查找学生信息')
    print('     3.修改学生信息')
    print('     4.删除学生信息')
    print('     5.排序')
    print('     6.统计')
    print('     7.显示所有学生信息')
    print('     0.退出系统')
    print('-'*30)
    print("  输入数字进行选择")
    print('='*30)

def main():
    """主函数"""
    while True:
        menu()
        choice = input("在这里输入数字并按回车：").strip()
        if choice in ['0', '1', '2', '3', '4', '5', '6', '7']:
            if choice == '1':
                insert()
                input("按回车继续")
            elif choice == '2':
                search()
                input("按回车继续")
            elif choice == '3':
                print("修改学生信息")
                # modify()
                input("按回车继续")
            elif choice == '4':
                print("删除学生信息")
                # delete()
                input("按回车继续")
            elif choice == '5':
                print("排序")
                # sort()
                input("按回车继续")
            elif choice == '6':
                print("统计")
                # count()
                input("按回车继续")
            elif choice == '7':
                show()
                input("按回车继续")
            elif choice == '0':
                print("退出系统")
                input("按回车继续")
                break
        else:
            print("输入错误")

if __name__ == "__main__":
    main()