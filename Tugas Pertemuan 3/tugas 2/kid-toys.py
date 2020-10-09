# ============================= Latihan 2 ===========================

title = "Toko Mainan Anak"
print("\n" + title.upper().center(100))
print("================================\n".center(100))

nama_pembeli = input("Masukkan Nama Pembeli : ")
kode_mainan = input("Masukkan Kode Mainan : ")
harga_mainan = int(input("Masukkan Harga Mainan : "))
jumlah_beli = int(input("Masukkan Jumlah Pembelian : "))
total_harga = harga_mainan * jumlah_beli

print("\n================= Faktur Anda  ===============\n")

print("Nama Pembeli : " + nama_pembeli)
print("Kode Mainan : " + kode_mainan.upper())
print("Harga Satuan : ",harga_mainan)
print("Jumlah Pembelian : ",jumlah_beli)
print("Total Harga : ",total_harga)

# ============================= End Latihan 2 ===========================

