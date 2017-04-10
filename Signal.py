from math import *
#from cmath import sin


def indexOf(data, value):
    index = 0
    for line in data:
        if line == value : return index
        else: index += 1
    if index >= len(data):
        return -1;
        
d = []
for i in range(50): d.append(1 + sin(i))
        
a1 = [0,0,0,0,1,0,0]
a2 = [0,0,0,0,0,0,0]
a3 = [0,0,0,0,0,0,1]
a4 = [1,0,0,0,0,0,0]
print(d)
print ('a1 ' , indexOf(a1, 1))
print ('a2 ' , indexOf(a2, 1))
print ('a3 ' , indexOf(a3, 1))
print ('a4 ' , indexOf(a4, 1))

