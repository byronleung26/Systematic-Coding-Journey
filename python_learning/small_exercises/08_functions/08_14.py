# 编写一个函数，将一辆汽车的信息存储在字典中。
# 这个函数总是接受制造商和型号，还接受任意数量的关键字实参。
# 在调用这个函数时，提供必不可少的信息，以及两个名值对，如颜色和选装配件。
# 这个函数必须能够像下面这样调用：
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# 打印返回的字典，确认正确地处理了所有的信息。
def make_car(producer,model,**information):
    """创建一个字典，包含汽车信息"""
    car_inf ={
        'car_producer': producer,
        'car_model': model,
        **information,
    }
    return car_inf
car = make_car("Haval","H9",color="Black",tow_package=True)
print(car)
