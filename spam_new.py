import time

# የሚላከው መልዕክት እና ብዛቱ
message =  input("Enter the message to send: ")
count = int(input("How many times should it be sent? (likeሌ 50): "))

print("\nThe explosion will start in 3 seconds.\n")
time.sleep(3) 

for i in range(1, count + 1):
    print(f"[{i}] {message}")
    # to control the speed (to rest a little)                          
    time.sleep(0.1)                    
print("\nfinished! ✅")         
