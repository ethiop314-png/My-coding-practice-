import os

def encrypt_file(file_name, key):
    # ፋይሉን ማንበብ
    with open(file_name, 'rb') as f:
        data = f.read()
    
    # መቆለፍ (Simple XOR Encryption)
    encrypted_data = bytearray()
    for byte in data:
        encrypted_data.append(byte ^ key)
    
    # የተቆለፈውን ፋይል መልሶ መጻፍ
    with open(file_name, 'wb') as f:
        f.write(encrypted_data)

filename = "secret.txt"
password_key = 123 # ይህ ሚስጥራዊ ቁልፋችን ነው

choice = input("1 ለቆልፍ / 2 ለፍታ: ")

if choice == '1' or choice == '2':
    encrypt_file(filename, password_key)
    print(f"ፋይሉ '{filename}' በተሳካ ሁኔታ ተስተካክሏል! ✅")
else:
    print("ስህተት ምርጫ! ❌")

