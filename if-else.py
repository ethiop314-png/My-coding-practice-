print("what is your name")
name=input(str())
print(f"I am {name}")
print("what grade are you")
grade =input(int ())
print(f"I am grade",grade)
print( name +" what is your mark")
mark=int(input())
if mark >80 :
	print(f"{name} ,your grade is A")
elif mark>70 :
	print( f"{name},your grade is B")
elif mark >60 :
		print(f"{ name}, your grade is C")
else:
			print( name, "your grade is F")
