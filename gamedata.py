#game_data
from random import randrange
class data:
    def __init__(self):
        self.list ={
        111 : 1000,
        112 : 1000,
        113 : 1000,
        114 : 1000,
        115 : 1000,
        116 : 1000,
        117 : 1000,
        118 : 1000,
        119 : 1000,
        120 : 1000,
        121 : 1000,
        122 : 1000,
        123 : 1000,
        124 : 1000,
        125 : 1000,
        126 : 1000,
        127 : 1000,
        128 : 1000,
        129 : 1000,
        130 : 1000
            }
    def push(self,index,item):
            self.list[index] = item
    
    
#b = randrange(10,100)

#print(a.list[120])
#print(b)
#list ={111 : 1000,112 : 1000, 113 : 1000, 114 : 1000, 115 : 1000, 116 : 1000,117 : 1000, 118 : 1000, 119 : 1000, 120 : 1000, 121 : 1000, 122: 1000, 123 : 1000, 124 : 1000, 125 : 1000, 126 : 1000, 127 1000, 128 : 1000, 129 : 1000,130 : 1000}
a = data()
#a.push(111,3000)
print(a.list[130])
