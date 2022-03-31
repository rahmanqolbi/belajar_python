# list
import numbers


nama = ["Rahman","Qolbi","Si A"]

# perulangan for
for i in nama:
    print(i)

nomor = [1,5,6,7,8,9]

# list method
nomor.append(10) # menambahkan data dibelakang list
print(nomor)

nomor.insert(1,5)
print(nomor)

nomor.pop(1) # menghapus data berdasarkan index
print(nomor)

nomor.remove(9) # menghapus data berdasarkan objek
print(nomor)

# menjumlahkan list
jumlah = 0
for angka in nomor:
    jumlah = jumlah + angka

print(jumlah)

total = sum(nomor)
print("Total :",total)

max = max(nomor)
print("Angka Tertinggi :",total)