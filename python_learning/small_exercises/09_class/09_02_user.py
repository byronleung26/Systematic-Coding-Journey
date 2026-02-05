# 创建一个名为 User 的类，其中包含属性first_name和last_name，
# 还有用户简介中通常会有的其他几个属性。
# 在类User中定义一个名为describe_user()的方法，用于打印用户信息摘要。
# 再定义一个名为greet_user()的方法，用于向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例调用上述两个方法。
class User:
    """打印用户信息摘要，向用户发出问候"""

    def __init__(self,first_name,last_name,age,sex):
        """初始用户属性"""
        self.full_name = f"{first_name} {last_name}"
        self.age = age
        self.sex = sex
    def describe_user(self):
        """打印用户信息"""
        print(self.full_name,self.age,self.sex)
    def greet_user(self):
        """向用户发出个性化问候"""
        print(f"{self.full_name}, long time not see")
user1 = User("Zhao","Gang",30,"nan")
user1.describe_user()
user1.greet_user()