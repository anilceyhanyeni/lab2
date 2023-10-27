sicaklik = eval(input("Sıcaklık = "))

if sicaklik < 0:
    print("Dondurucu")
elif 0<sicaklik<10:
    print("Çok Soğuk")
elif 10<sicaklik<20:
    print("Soğuk")
elif 20<sicaklik<30:
    print("Normal")
elif 30<sicaklik<40:
    print("Sıcak")
else:
    print("Çok Sıcak")
