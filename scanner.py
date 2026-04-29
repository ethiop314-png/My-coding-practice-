import socket

target = input("ሊፈተሽ የሚገባውን IP ወይም URL ያስገቡ: ")

print(f"--- {target} ላይ ፍተሻ እየተካሄደ ነው ---")

# ከ 1 እስከ 100 ያሉትን በሮች ለመፈተሽ
for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5) # ፍጥነቱን ለመጨመር ሰከንዱን ቀነስነው
    
    # 0 ማለት በሩ ክፍት ነው ማለት ነው
    if s.connect_ex((target, port)) == 0:
        print(f"በር {port}: ክፍት (OPEN) ✅")
    
    s.close()

print("--- ፍተሻው ተጠናቋል ---")s.close()
