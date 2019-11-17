#クラスの作り方,ユーザー情報のクラスを作る
# class User:
#     pass    #始まりは大文字
# tom= User()   #変数へクラスを代入。これをインスタンスという
# tom.name= 'tom'
# tom_score = 20
#
# bob = user()
# bob.name="bob"
# bob.level=3
#
# print(tom.name)
# print(bob.level)

# class User:
#     def __init__(self , name):
#         #インスタンス変数
#         self.name=name
# tom= User('tom')
# bob= User('bob')
# print(tom.name)
# print(bob.name)

# class User:#クラス変数
#     count = 0
#     def __init__(self , name):
#         User.count +=1
#         self.name=name
#
# print(User.count)#0
# tom= User('tom')
# bob= User('bob')
#  # print(tom.name)
#  # print(bob.name)
# print(User.count)#2 インスタンスが作成された数
# print(tom.count)#2インスタンス変数とクラス変数の数
#インスタンスメゾット

    #関数（メゾット）　
#     def __init__(self , name):
#          User.count +=1
#          self.name=name
# #クラスメゾット
#     def say_hi(self):
#          print('hi {0}'.format(self.name))
#     @classmethod
#     def show_info(cls):
#         print('{0} instances'.format(cls.count))
#
# tom = User('tom')
# bob = User('bob')
# tom.say_hi()
# bob.say_hi()
# User.show_info()

#継承のやり方、親クラスを持ってきて子クラスで定義を追加
# import user
from user import adminUser, User
# bob = user.adminUser('bob',23)
bob = adminUser('bob',23)
print(bob.name)
bob.say_hi()
bob.say_hello()
