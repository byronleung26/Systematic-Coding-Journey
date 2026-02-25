# 创建一个名为Restaurant的类,为其__init__()方法设置两个属性：
# restaurant_name和cuisine_type。
# 创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，
# 其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业
class Restaurant:
    """餐馆信息及营业状态"""
    def __init__(self,restaurant_name,cuisine_type):
        """初始化属性restaurant_name和restaurant_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        """打印餐馆信息"""
        print(self.name + self.type)
    def open_restaurant(self):
        """打印餐馆营业状态"""
        print("餐馆正在营业")
# 根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。
restaurant = Restaurant("好再来","川菜餐厅")
print(f"{restaurant.restaurant_name}是一家{restaurant.cuisine_type}")