print("Enter a message you want to send")
message = input()

i = 0

print("How many times should I send your message? (for example: 50)")
q = int(input())

while i <= q:
    print(i, message)
    i += 1

print("Finished")

