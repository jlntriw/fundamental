"""
Perulangan while tak terbatas
"""
jumlah_buku = 10
print ('ibu berkata , "baca semua buku" ')
jumlah_dibaca = 0

jumlah_paham = 0

print (f'jumlah buku yang di baca {jumlah_dibaca}')
print (f'jumlah buku yang di pahami {jumlah_paham}')

while jumlah_dibaca < jumlah_buku * 2 :
    jumlah_dibaca = jumlah_dibaca + 1
    if jumlah_paham == 9 :
        print (f"Buku ke {jumlah_paham + 1} belum paham")
    else :
        jumlah_paham = jumlah_paham + 1
        print (f"buku ke {jumlah_paham} sudah dibaca dan dipahami")

print( f"Jumlah buku yang sudah dibaca dan dipahami {jumlah_paham}")
if jumlah_paham == jumlah_dibaca  :
    print(f'semua buka sudah dibaca dan dipahami')
else:
    print(f'ada buku yang tidak dipahami')


