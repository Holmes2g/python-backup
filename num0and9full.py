number= input("Give me a number to check that's between 0 and 10 : ")
n=int(number)
Output = True
if n>10:
 print("Your number is greader than 10")
elif n<0:
 print("Your number is smaller than 0") 
elif 0<=n<=10:
 Output = False
 print("Yes, your number is between 0 and 10")
while Output:
  n= int(input("Wanna try again, just put a number.Come on! : "))
  Output = False
  if n>10: 
   Output = True 
   print("Your number is greader than 10")
  elif n<0:
   Output = True 
   print("Your number is smaller than 0")
   
  elif 0<=n<=10:
   Output = False
   print("Right.Excellent")
   
  
  

 
