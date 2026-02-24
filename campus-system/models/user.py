class User():
    """账号基类"""
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
    def verify_pwd(self, pwd):
        self.verify_pwd = pwd