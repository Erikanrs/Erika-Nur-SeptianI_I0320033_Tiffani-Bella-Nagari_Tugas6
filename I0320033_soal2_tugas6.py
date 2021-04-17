nilai = input("Masukkan nilai yang akan dirata-ratakan: ")
listnilai = nilai.split(",")
totalnilai = [float(x) for x in listnilai]

total = 0

for nilai in totalnilai :
    total = total + nilai
ratarata = total/len(totalnilai)
print("Total nilai anda adalah: ", total)
print("Rata-rata nilai anda adalah: ", ratarata)