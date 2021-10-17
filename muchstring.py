#class stack:
 #   def __init__(self):
  #      self.items=[]
   # def push(self,item):
    #    self.items.append(item)
    #def pop(self):
     #   return self.items.pop()
    #def is_empty (self):
     #   return self.items ==[]
          
from truefalse import stack         
def matches(opens,closes):
    opener ="({["
    closer =")}]"
    return opener.index(opens) == closer.index(closes)
          
          
def checker(string):
    s = stack()
    balanced = True
    index = 0
    while index<len(string) and balanced:
        symbol = string[index]
        if symbol in "({[":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False 
            else:
                top = s.pop()
                if not matches (top,symbol):
                    balanced = False
                else:
                    balanced = True  
        index = index +1
    if balanced and s.is_empty ():
        return True 
    else:
        return False 
        
        
        
a = input("Enter some bracket: ")        
print(checker(a))
