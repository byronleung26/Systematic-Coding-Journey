def main():
    """主程序"""
    # menu() 菜单功能待开发
    choice = input("请选择功能(输入0-4)：")
    if choice == '1':
        print("空格删除功能待开发")
    elif choice == '2':
        print("段落缩进功能待开发")
    elif choice == '3':
        print("标点替换功能待开发")
    elif choice == '4':
        print("对齐功能待开发")
    elif choice == '5':
        print("字母大小写转换待开发")
    elif choice == '6':
        print("段落划分功能待开发")
    elif choice == '0':
        print("退出")
    else:
        print("输入错误")