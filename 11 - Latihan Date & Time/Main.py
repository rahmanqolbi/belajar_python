# date and time

import datetime as dt

print("Silahkan Masukan Tanggal, \nBulan dan Tahun")
tanggal = int(input("Tanggal = "))
bulan = int(input("Bulan = "))
tahun = int(input("Tahun = "))

hari = dt.date(tahun,bulan,tanggal)
print(f"Kamu lahir di hari {hari:%A}, bulan {hari:%B}")

hari_ini = dt.date.today()
umur_hari = hari_ini - hari
umur_tahun = umur_hari.days // 365
print(f"Umur Kamu {umur_tahun} Tahun")

