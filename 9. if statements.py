age = int(input("Hur gammal är du?: "))
if age == 100:
    print("Du är gammal.")
elif age >= 18:
    print("Du är vuxen.")
elif age < 0:
    print("Du är inte född än.")
else:
    print("Du är ett barn.")