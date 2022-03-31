# operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_depan = "Rahman"
nama_belakang = "Qolbi"

nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("Panjang dari nama lengkap :" ,panjang)

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string

o = "o"
status = o in nama_lengkap
print(o + " ada di " + nama_lengkap + " = " + str(status)) 

o = "C"
status = o not in nama_lengkap
print(o + " tidak ada di " + nama_lengkap + " = " + str(status)) 

# mengulang
print("wk"*10)

# indexing
print("indeks ke-0 : " + nama_lengkap[0])
print("indeks ke-(-2) : " + nama_lengkap[-2])
print("indeks ke-[0,3]  : " + nama_lengkap[0:3])
print("indeks ke-[0,2,4,6,8,10]  : " + nama_lengkap[0:11:2])

# item paling kecil
print("Paling kecil : " + min(nama_lengkap))

# item paling besar
print("Paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# 4. operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count ("o")
print("jumlah o pada " + data + " = " + str(jumlah ))

## merubah case dari string

# merubah semua ke uppercase
salam = "bro!"
print("Normal = " + salam)
salam = salam.upper()
print("Upper = " + salam)

# merubah semua ke lowercase
test = "TeSt ya GaEz"
print("Normal = " + test)
test = test.lower()
print("Lower = " + test)

## pengecekan dengan is... method

# contoh pengecekan lower case
salam = "sis"
apakah_lower = salam.islower()
print("Apakah " + salam + " lower ? = " + str(apakah_lower))

salam = "123"
apakah_nomor = salam.isnumeric()
print("Apakah " + salam + " nomor ? = " + str(apakah_nomor))

## ngecek komponen startswith () endswith() <-- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))
cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku','sayang', 'kamu'] 
gabung = '*'.join(pisah)
print(pisah)
print(gabung)

pisah_lagi = gabung.split('*')
print(pisah_lagi)

# format string

# generic
nama = "Rahman"
str = "Hello " + nama
print(str)

# format str
nama = "Rahman Qolbi"
uang = 7000000.5678
str = f"Nama Saya {nama}, \nbeli laptop Rp{uang:,.2f}"
print(str)
str = f"Nama Saya {nama}, \nbeli laptop Rp{uang:013.2f}"
print(str)

# menampilkan tanda + atau
angka_minus = -10
angka_plus = 10
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+d}" 
print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}" 
print(format_persen)

# Width and Multiline
# Data
data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# string
data_string = f"nama {data_nama}, umur = {data_umur}, tinggi {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(data_string)

# string multiline
data_string = f"nama {data_nama}, \numur = {data_umur},\ntinggi {data_tinggi},\nsepatu = {data_nomor_sepatu}"
print(data_string)