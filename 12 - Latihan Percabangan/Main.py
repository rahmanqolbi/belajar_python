# Aplikasi Kalkulator Sederhana

angka1 = float(input("Masukan Angka Pertama = "))
operasi = input("Pilih Operasi (+,-,x,/) = ")
angka2 = float(input("Masukan Angka Kedua = "))

if operasi == '+' : hasil = angka1+angka2
elif operasi == '-' : hasil = angka1-angka2
elif operasi == '*' or operasi == 'x' : hasil = angka1*angka2
elif operasi == '/' : hasil = angka1/angka2
else : print("Yang bener lah bambang")

print(f"Hasil = {hasil}")
