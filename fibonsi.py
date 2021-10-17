n = int(input("Enter the number: "))
n1 = 0
n2 = 1 
for i in range(n):
    n3 = n1
    #1.n3 value = 0 =n1 original value
    #2.n3 value = 1 =1.n1 value
    #3.n3 value = 1 =2.n1 value
    n1 = n2
    #1.n1 value = 1 =define by n2 origin
    #2.n1 value = 1 =1.n2 value
    #3.n1 value = 2 =2.n2 value
    n2 = n3 + n2
    #1.n2 value = 1 = 1.n3 value + n2 origin
    #2.n2 value = 2 = 2.n3 value + 1.n2 value
    #3.n2 value = 3 = 3.n3 value + 2.n2 value
    print(n1) #print the number you want. 

