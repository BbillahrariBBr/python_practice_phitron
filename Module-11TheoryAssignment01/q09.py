# Write a class with two instance variables X, n . Add two methods sum() and pow() to get the sum of X+n and exponential/power of Xn .


class Sumpow():
    def __init__(self,x,n):
        self.x = x
        self.n = n
    
    def sum(self):
        return self.x + self.n
    
    def pow(self):
        return self.x ** self.n

obj= Sumpow(2,3)
s = obj.sum()
print(s)
p = obj.pow()
print(p)

