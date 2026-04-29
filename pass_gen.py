import random
import string

# የፓስዎርዱ ርዝመት
length = int(input("የፓስዎርዱ ርዝመት ስንት ይሁን? (ለምሳሌ 12): "))

# ሁሉንም ፊደላት፣ ቁጥሮች እና ምልክቶች ማዘጋጀት
chars = string.ascii_letters + string.digits + string.punctuation

# በዘፈቀደ መምረጥ (Random Selection)
password = "".join(random.sample(chars, length))

print(f"\nየተፈጠረው ጠንካራ ፓስዎርድ: {password}")
print("--- ይህንን ማንም ሊገምተው አይችልም! 🛡 ---")
