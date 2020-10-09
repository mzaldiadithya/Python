title = "Program Menghitung Nilai Matakuliah Praktek"
print(title.center(100))
print("=========================================================".center(100))

# Define Variable
nama_matkul = input("\nMasukkan Nama Matakuliah : ")
max_pertemuan = int(input("Masukkan Max Pertemuan : "))
kehadiran = int(input("Masukkan Jumlah Hadir : "))

n_absen = kehadiran*100/max_pertemuan
print("Nilai Absen Yang Didapat Dari Perhitungan Diatas :", sep=' ', end=' ', flush=True)
print(n_absen)

n_tugas = int(input("Masukkan Nilai Tugas : "))
n_project = int(input("Masukkan Nilai Project : "))

# -----------------------------------------------

kehadiran20 = n_absen*20/100
tugas25 = n_tugas*25/100
project55 = n_project*55/100

total_nilai = kehadiran20+tugas25+project55
# End Define Variable

print("=====================================")

# Output
print("Konversi Nilai Berdasarkan Persentase Nilai Sesuai Ketentuan")

print("Nilai Absen (20%) Anda Adalah :", sep=' ', end=' ', flush=True)
print(kehadiran20)

print("Nilai Tugas (25%) Anda Adalah :", sep=' ', end=' ', flush=True)
print(tugas25)

print("Nilai Project (55%) Anda Adalah :", sep=' ', end=' ', flush=True)
print(project55)

print("=====================================")

print("Pada Mata Kuliah : " + nama_matkul)
print("Anda Mendapatkan Total Nilai :", sep=' ', end=' ', flush=True)
print(total_nilai)

if total_nilai >=80:
    print("Selamat Anda Mendapat Grade 'A', \nDan Anda Dinyatakan Lulus")
elif total_nilai >=70:
    print("Selamat Anda Mendapat Grade 'B', \nDan Anda Dinyatakan Lulus")
elif total_nilai >=60:
    print("Selamat Anda Mendapat Grade 'C', \nDan Anda Dinyatakan Lulus")    
elif total_nilai >=31:
    print("Maaf Anda Mendapat Grade 'D', \nSayangnya Anda Dinyatakan Tidak Lulus ")                
elif total_nilai < 31:
    print("Maaf Anda Mendapat Grade 'E', \nSayangnya Anda Dinyatakan Tidak Lulus ")

# End Output