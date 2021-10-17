def triangle_star(a):
    for i in range(1,a+1):
      for b in range(i):
          print("*",end="")
      print("")
     
    
a=int(input("please enter a num"))
print(f"triangle_star({a})")
triangle_star(a)   
print(f"triangle_star({a})")
