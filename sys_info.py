import platform
import os

print("--- የስልክዎ/የሲስተምዎ መረጃ ---")

# የሲስተሙን አይነት ማወቅ (ለምሳሌ Android/Linux)
print(f"ኦፕሬቲንግ ሲስተም: {platform.system()}")
print(f"የሲስተም ስሪት (Version): {platform.release()}")

# የፕሮሰሰር (CPU) አይነት
print(f"ፕሮሰሰር: {platform.machine()}")

# ተርመክስ ውስጥ ያለህን ተጠቃሚ (User) ስም ማወቅ
print(f"የተርመክስ ተጠቃሚ: {os.getlogin()}")

# የስልኩን Architecture (32-bit ወይስ 64-bit)
print(f"Architecture: {platform.architecture()[0]}")

print("---------------------------")
