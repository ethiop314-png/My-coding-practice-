import requests

# መረጃ የምንሰበስብበት ድረ-ገጽ (ለምሳሌ Google)
url = "https://www.google.com"

print(f"{url} ን በመፈተሽ ላይ... 🔍")

try:
    response = requests.get(url)
    
    # የድረ-ገጹን የውስጥ ኮድ (HTML) በከፊል ማሳየት
    print("\nየድረ-ገጹ ይዘት (የመጀመሪያዎቹ 500 ፊደላት):")
    print("-" * 30)
    print(response.text[:500])
    print("-" * 30)
    
    if response.status_code == 200:
        print("\nግንኙነቱ ተሳክቷል! ✅")
    else:
        print(f"ችግር ተፈጥሯል! ስህተት ቁጥር: {response.status_code}")

except Exception as e:
    print(f"መገናኘት አልተቻለም: {e}")
