a = eval(input("a açısı: "))
b = eval(input("b açısı: "))
c = eval(input("c açısı: "))

if (a <= 0 or b <= 0 or c <= 0) :
    print("yanlış açı girdiniz")
elif a + b + c != 180:
    print("üçgen oluşmaz")
else:
    print("üçgen oluşur")
