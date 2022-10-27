""" Diamond Ring Problem """
""" avoid multiple inharitance, diamond ring problem """
class A:
    def print_some(self):
        print('Im on A')
class B(A):
    def print_some(self):
        print('Im on B')
class C(A):
    def print_some(self):
        print('Im on C')
class D(B,C):
    def print_some(self):
        print('Im on D')

obj1 = A()
obj2 = B()
obj3 = C()
obj4 = D()

obj1.print_some()
obj2.print_some()
obj3.print_some()
obj4.print_some()