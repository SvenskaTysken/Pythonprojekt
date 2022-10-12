
try:
    täljare = int(input("ange ett tal att dividera: "))
    nämnare = int(input("ange ett tal att dividera med: "))
    result = täljare / nämnare
except ZeroDivisionError as e:
    print(e)
    print("Du kan inte dividera med 0 din idiot.")
except ValueError as e:
    print(e)
    print("Dividera med tal förihelvete")
except Exception as e:
    print(e)
    print("Oj då, något gick fel :(")
else:
    print(result)
finally:
    print("Käften, gå och plugga grunken")