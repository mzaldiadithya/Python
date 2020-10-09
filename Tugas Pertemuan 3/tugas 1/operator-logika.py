# ============================= Operator Logika ===========================

title = "Operator Logika | AND"
print("\n" + title.upper().center(100))
print("================================\n".center(100))

bil1 = int(input("Masukkan Bilangan 1 : "))
bil2 = int(input("Masukkan Bilangan 2 : "))
modulo = int(input("Masukkan Modulo Bilangan : "))

operasi = bil1 % modulo == 0 and bil2 & modulo == 0

print("\n================================\n")
print(bil1 ,"%", modulo ,"== 0", "AND", bil2 ,"Dan", modulo ,"== 0, Maka :",operasi)

# ============================= End Operator Logika ===========================