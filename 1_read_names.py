word = input()

while word != "Stop":
    print(word)
    word = input()

#ИЛИ:

while True:
    name = input()
    if name == "Stop":
         break
    print(name)
