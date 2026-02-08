def menu():
    """主菜单"""
    print("""
——————————员工管理系统——————————
                
  ==========功能菜单==========

        1.录入员工信息
        2.查看员工信息    
        3.修改员工信息
        4.删除员工信息
        0.退出
  ===========================
———————————————————————————————
  输入0-4选择相应功能
———————————————————————————————
""")
def main():
    """主函数"""
    optional_item = ['0','1','2','3','4']
    while True:
        menu()  # 显示主菜单
        user_input = input("请选择功能(输入0-4): ")
        option_str = user_input.strip()
        if option_str in optional_item:  # 判断输入是否合规
            if option_str == '0':  # 选择0退出
                break
            elif option_str == '1':  # 选择1录入
                print("录入功能正在开发中，请稍待")
                input("按任意键继续") 
            elif option_str == '2':  # 选择2查看
                print("查看功能正在开发中，请稍待")
                input("按任意键继续")
            elif option_str == '3':  # 选择3修改
                print("修改功能正在开发中，请稍待")
                input("按任意键继续")
            elif option_str == '4':  # 选择4删除
                print("删除功能正在开发中，请稍待")
                input("按任意键继续")
        else:  # 输入错误
            print("输入错误，请重新输入数字0-4")
            input("按任意键继续")

if __name__ == "__main__":
    main()