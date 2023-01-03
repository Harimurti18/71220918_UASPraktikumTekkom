print("========================================")
print("************ Justice League ************")
print("========================================")

nama = str(input("Masukan username anda: "))
# if nama == "brucewyne":
#     print("==== WELCOME", nama, "====")
# elif nama == "victorstone":
#     print("==== WELCOME", nama, "====")
# elif nama == "ciscoramon":
#     print("==== WELCOME", nama, "====")
# else:
#     exit("Access Denied")
while True:
    print("1. Tambah anggota Justice League")
    print("2. Hapus anggota Justice League")
    print("3. Tampilkan anggota Justice League")
    print("4. Exit")
    data = []
    pilih = int(input("Masukan pilihan anda: "))
    if pilih == 1:
        tambah = str(input("Nama anggota baru: "))
        data.append(tambah)
        print("data", data, "berhasil ditambahkan")
    elif pilih == 2:
        hapus = str(input("Anggota yang akan dihapus: "))
        if hapus == data:
            data.remove(hapus)
            print("data", data.remove(hapus), "berhasil dihapus")
        else:
            print("data", hapus, "tidak ditemukan")
    elif pilih == 3:
        print("Daftar anggota Justice League:")
        print(data)
    elif pilih == 4:
        print("see u next time Mr.", nama, ",GLHF")
        break