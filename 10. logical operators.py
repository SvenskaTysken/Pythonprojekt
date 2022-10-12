temp = int(input("hur varmt är det ute?: "))

if temp >= 10 and temp <= 30:
    print("Det är lagom temperatur idag")
    print("ta en promenad!")
elif temp < 0:
    print("Det är för kallt")
    print("stanna hemma!")
elif temp > 30:
    print("Det är för varmt")
    print("stanna hemma!")