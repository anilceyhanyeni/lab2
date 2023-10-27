a = int(input("a kenarı= "))
b = int(input("b kenarı= "))
c = int(input("c kenarı= "))

if a == b and b == c:
    print("Eşkenar")
elif (a != b and b == c) or ( a == b and b != c ):
    print("İkizkenar")
else:
    print("Çeşitkenar")
