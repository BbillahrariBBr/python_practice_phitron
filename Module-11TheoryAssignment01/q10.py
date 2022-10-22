# Write a Python class named Distance constructed by two points (x1, y1), (x2, y2) and a method which will compute the distance between those points.

import math

class Distance():
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def result(self):
        return math.sqrt(((self.x2-self.x1)**2 + (self.y2-self.y1)**2))

dis = Distance(4,9,10,5)
out = dis.result()
print("%.4f" % out)