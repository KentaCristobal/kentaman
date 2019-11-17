#多重承継の作り方
class A:
    def say_a(self):
        print('A!')
    def say_hi(self):
        print('hi from A')

class B:
    def say_b(self):
        print('B!')
    def say_hi(self):
        print('hi from B')
class C(A,B):#同じメゾットが二つのクラスにある時は、（）の中の優先順位
    pass

c= C()
# c.say_a()
# c.say_b()
c.say_hi()
