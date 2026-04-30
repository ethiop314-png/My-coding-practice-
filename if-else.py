print("What is your name")
while True:
    name = input("Enter your name: ")

    if name.replace(" ", "").isalpha():
        break
    else:
        print("Invalid! Use letters only.")
print(f"I am {name}")

print(f"{name} what grade are you in")
            
while True:        
    grade = int(input("Enter class: "))

    if 1 <= grade <= 12:
        break
    else:
        print("Invalid! Please enter between 1 and 12.")

print("I am grade", grade)
print(name + " what is your mark")

while True:
    mark = int(input("Enter your mark: "))

    if 0 <= mark <= 100:
        break
    else:
        print("Please enter your mark again, you entered out of range")
           
if mark > 85:
    print(f"{name}, your grade is A")
elif mark > 80:
    print(f"{name}, your grade is A-")
elif mark > 75:
    print(f"{name}, your grade is B")
elif mark > 60:
    print(f"{name}, your grade is C")
elif mark > 50:
    print(f"{name}, your grade is D")
else:
    print(f"{name}, your grade is F")
if mark >= 50:
    print("Keep up the good work!")
else:
    print("Please study hard.")
