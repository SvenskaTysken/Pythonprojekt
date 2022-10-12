
text = "Yo wassup dude\nThis is some text i wrote\nCY@ motherf*cker\n"

with open('test.txt','w') as file: #använd "a" istället för "w" för att lägga till text.
    file.write(text)

with open('test.txt') as file:
    print(file.read())
