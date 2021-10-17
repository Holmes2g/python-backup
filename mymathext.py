class math:
    def plus(self,x,y):
        return print(f"Result is {x+y}.")
    def minus(self,x,y):
        return print(f"Result is {x-y}.")
    def into(self,x,y):
        return print(f"Result is {x*y}.")
    def divide(self,x,y):
        return print(f"Result is {x/y}.")
    def double(self,x):
        return print(f"Result is {x**2}.")
    def tripple(self,x):
        return print(f"Result is {x**3}.")
op = input("Please choose op \n '+','-','*','/':\n if you want to double it type 'd'\n if you want to tripple if type 't' ; ")
mymath = math()
if op == '+':
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : " ))
    mymath.plus(x,y)
elif op == '-':
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : " ))
    mymath.minus(x,y)
elif op == '*':
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : " ))
    mymath.into(x,y)
elif op == '/':
    x = int(input("Enter first number : "))
    y = int(input("Enter second number : " ))
    mymath.divide(x,y)
elif op == 'd':
    x = int(input("Enter the number : "))
    mymath.double(x)
elif op == 't':
    x = int(input("Enter the number : "))
    mymath.tripple(x)