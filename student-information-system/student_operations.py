"""
学生信息管理系统 - 业务功能模块
包含：录入insert()、查找search()、修改modify()、删除delete()、排序sorting()、统计count()、显示show()
日期：2026-02-26
"""

from data_handler import load_data, save_data

def insert():
    """新增学生信息"""
    stu_data = load_data()

    while True:
        stu_id = input("输入学号(直接回车退出): ")
        if stu_id in stu_data:
            print("\033[91m该学号已存在，如需修改请使用3.修改学生信息功能\033[0m")
            continue
        elif not stu_id:
            break
        else:
            name = input("输入姓名:")
            sex = input("输入性别:")
            major = input("输入专业:")
            stu_data[stu_id] = {
                '姓名':name,
                '性别':sex,
                '专业':major
            }
            save_data(stu_data)
            print("保存成功")

        con = input("直接回车退出，否则将继续添加下一个: ")
        if not con:
            break

def search():
    """查找学生信息"""
    stu_data = load_data()

    kewword = input("请输入学号或姓名：")

    if kewword in stu_data:
        info = stu_data[kewword]
        print(f"学号：{kewword}    姓名：{info['姓名']}    性别：{info['性别']}    专业：{info['专业']}")
        return
    for stu_id, info in stu_data.items():
        if info["姓名"] == kewword:
            print(f"学号：{stu_id}    姓名：{kewword}    性别：{info['性别']}    专业：{info['专业']}")
            return
    print("未找到信息，可能输入错误或未添加该学生")


# def modify():


# def delete():


# def sort():


# def count():


def show():
    """显示所有学生信息"""
    stu_data = load_data()

    if not stu_data:
        print("暂无学生信息")
        return
    
    print(f'\033[91m{"学号":^12}{"姓名":^8}{"性别":^6}{"专业":^10}\033[0m')
    print('-'*40)
    for stu_id, info in stu_data.items():
        print(f"{stu_id:^12}{info['姓名']:^8}{info['性别']:^6}{info['专业']:^10}")
    print('-'*40)
    print(f"共输出{len(stu_data)}条信息")


if __name__ == "__main__":
    print("测试show()函数")
    search()
    print("测试完成")