# latihan konversi satuan temperatur

# program konversi fahrenheit ke kelvin
print("\nProgram Konversi Temperatur\n")
fahrenheit = float(input("Masukan Suhu (Fahrenheit) : "))
celsius = (5/9)*(fahrenheit-32)
kelvin = celsius+273
print("Suhu dalam Kelvin adalah",kelvin,"Kelvin\n")

# program konversi kelvin ke fahrenheit
kelvin = float(input("Masukan Suhu (Kelvin) : "))
celsius = kelvin-273
fahrenheit = (9/5)*celsius+32
print("Suhu dalam fahrenheit adalah",fahrenheit,"Fahrenheit")