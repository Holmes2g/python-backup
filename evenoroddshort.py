try:
 num = int(input("Enter Number"))
 dev = num%2
 if num==0:
  print("Your number is even")
 else:
  print("Your number is odd")
except ValueError:
 print("Please enter only number")
 print(ValueError)
