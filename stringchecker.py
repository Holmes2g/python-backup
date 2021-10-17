from truefalse import stack
def Checker(string):
	s= stack()
	balanced=True
	index= 0
	while index<len(string) and balanced:
		symbol = string[index]
		if symbol == "(":
			s.push(symbol)
		else:
			if s.is_empty():
				balanced = False
			else:
				s.pop()
		index = index+1
	if balanced and s.is_empty():
		print(True)
	else:
		print(False)
check = input("please enter the symbol of string:\n")
Checker(check)
	
