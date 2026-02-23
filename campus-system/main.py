def main():
    """主函数"""
    optional_item = ['0', '1', '2', '3', '4', '5']
    while True:
        menu()
        user_input = input("请选择功能(输入0-4): ")
        option_str = user_input.strip()
        if option_str in optional_item:
            if option_str == '0':
                break
            elif option_str == '1':
                print("功能正在开发中")
            elif option_str == '2':
                print("功能正在开发中")
            elif option_str == '3':
                print("功能正在开发中")
            elif option_str == '4':
                print("功能正在开发中")
            elif option_str == '5':
                print("功能正在开发中")
        else:
            print("输入错误，请重新输入数字0-5")
            input("输入任意值继续")

if __name__ == "__main__":
    main()