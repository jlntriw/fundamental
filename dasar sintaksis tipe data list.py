daftar_buku = ['naruto','bleach','one piece']
print ('variabel data buku')
print(daftar_buku)

print ('\nsemua dengan for in')
for buku in daftar_buku :
    print (buku)

print ('\ntampilkan isi daftar buku pada indeks tertentu')
print (daftar_buku[0])
print (daftar_buku[2])

print ('\nTampilkan dengan for in range')
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

daftar_buku = ['naruto','313','96']
print ('\nTampilkan dengan for in range tipe data berbeda')
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nkembalikan nilai awal daftar buku')
daftar_buku = ['naruto','bleach','one piece']
daftar_buku.append('buku matematika')
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nclear list')
daftar_buku.clear()
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nganti list pertama')
daftar_buku = ['naruto','bleach','one piece']
daftar_buku [0]= 'boruto'
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nambil elemen ke-2')
buku = daftar_buku.pop(1)
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\nbuku yang diambil')
print(buku)

print ('\npop')
daftar_buku = ['naruto','bleach','one piece']
daftar_buku.pop()
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])

print ('\npop -1')
daftar_buku = ['naruto','bleach','one piece']
daftar_buku.pop(-2)
for i in range (0, len(daftar_buku)):
    print (daftar_buku[i])