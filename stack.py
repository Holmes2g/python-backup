class stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1] 
    def is_empty(self):
        return self.items == []
    def size(self):
        return print(len(self.items))
