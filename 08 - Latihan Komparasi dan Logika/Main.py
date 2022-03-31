# membuat gabungan area rentang dari angka

# 1. --------0+++++++5--------8++++++++11--------- 

angka = float(input("Masukan Angka : "))
isLebihDari0 = angka > 0
isKurangDari5 = angka < 5
isLebihDari8 = angka > 8
isKurangDari11 = angka < 11
isCorrect = (isLebihDari0 and isKurangDari5) or (isLebihDari8 and isKurangDari11)
print(isCorrect)

# 2. ++++++0-------5+++++++8-------11+++++++

angka = float(input("Masukan Angka : "))
isKurangDari0 = angka < 0
isLebihDari5 = angka > 5
isKurangDari8 = angka < 8
isLebihDari11 = angka > 11
isCorrect = isKurangDari0 or (isLebihDari5 and isKurangDari8) or isLebihDari11
print(isCorrect)