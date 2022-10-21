#operator aritmatika

angka_1 = int(input("masukkan angka pertama :"))
operator = input("pilih operator(+,-,*,/,%,**) :")
angka_2 = int(input("masukkan angka kedua :"))
#penjumlahan

if operator == "+":
    hasil = angka_1 + angka_2
    print("{} + {} = {}". format(angka_1,angka_2,hasil))
#pengurangan
elif operator == "-":
    hasil = angka_1 - angka_2
    print("{} - {} = {}". format(angka_1,angka_2,hasil))
#perkalian
elif operator == "*":
    hasil = angka_1 * angka_2
    print("{} * {} = {}". format(angka_1,angka_2,hasil))
#pembagian
elif operator == "/":
    hasil = angka_1 / angka_2
    print("{} / {} = {}". format(angka_1,angka_2,hasil))
#sisa bagi
elif operator == "%":   
    hasil = angka_1 % angka_2
    print("{} % {} = {}". format(angka_1,angka_2,hasil))
#pangkat
elif operator == "**":
    hasil = angka_1 ** angka_2
    print("{} ** {} = {}". format(angka_1,angka_2,hasil))
