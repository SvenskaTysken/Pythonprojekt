import random

x = random.randint(1,6)
y = random.random()

myList = ['sten','sax','påse']

z = random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"]

random.shuffle(cards)

print(cards)