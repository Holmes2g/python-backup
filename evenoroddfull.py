print("Enter a number that u want to decide to even or odd OR You can out.")
o=input("if you don't want to check, write 'n' and if u want to be, write 'y'")
if o== "n":
    print("Get out mf")
    exit()
elif o=="y":
 a = input("Here's your number to put: ")
 try:
  out = True
  a = int(a)
  if (a%2) ==0:
   result = f"your number is {a} and it is even"
  elif (a%2) ==1:
   result = f"Your number is {a} and it is odd"
  if out:
   print(result)
 except ValueError:
   print("Please enter number only")
   print(ValueError);
Output = True
while Output:
 b = input("next time?enter number for continue and 'n' for no: ")
 Output= False
 try:
  b = int(b)
  if b%2 == 0 : 
   print(f"Your number is {b} and it is even")
   Output = True
  elif int(b)%2 != 0 : 
   print(f"Your number is {b} and it is odd")
   Output = True
 except ValueError:
   print("get out mf")
   print(ValueError);
   Output = False
 
 

