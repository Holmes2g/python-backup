class mymath:
    def plus(self,x,y):
        c=x+y
        print(f"Result is {c}.")
    def minus(self,x,y):
        c=x-y
        print(f"Result is {c}.")
    def into(self,x,y):
        c=x*y
        print(f"Result is {c}.")
    def divide(self,x,y):
        c=x/y
        print(f"Result is {c}.")
op = input("Please choose op \n '+','-','*','/':  ")
math = mymath()
x = int(input("Ente first number : "))
y = int(input("Enter second number : " ))
if op == '+':
    math.plus(x,y);
elif op == '-':
    math.minus(x,y);
elif op == '*':
    math.into(x,y);
elif op == '/':
    math.divide(x,y);
