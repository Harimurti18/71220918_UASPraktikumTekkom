print("==== Selamat datang di XXV ====")
tanggal = int(input("Masukan tanggal hari ini: "))
print("\f== Berikut genre film yang tersedia ==")
print("1. Horror")
print("2. Action")
genre = int(input("\fSilahkan pilih mau nonton film bergenre apa: "))
print("")
if genre == 1:
    print("== Berikut pilihan film horor yang sedang tayang ==")
    print("1. The Devil's Light")
    print("2. Pengabdi Setan")
    pilih = int(input("Silahkan pilih mau nonton film apa: "))
    tiket = int(input("Mau memesan tiket sebanyak: "))
    if tanggal % 2 == 0:
        print("Total yang harus dibayar adalah Rp.", ((25000*tiket)*(98/100)))
    else:
        print("Total yang harus dibayar adalah Rp.", (25000*tiket))
elif genre == 2:
    print("== Berikut pilihan film action yang sedang tayang ==")
    print("1. Black Panther: Wakanda Forever")
    print("2. Avatar: The Way of Water")
    pilih = int(input("\fSilahkan pilih mau nonton film apa: "))
    tiket = int(input("Mau memesan tiket sebanyak: "))
    if tanggal % 2 == 1 and tiket > 4:
        print("Total yang harus dibayar adalah Rp.", (25000*tiket)*(95/100))
    else:
        print("Total yang harus dibayar adalah Rp.", (25000*tiket))
else:
    print("Pilihan yang anda pilih tidak tersedia di bioskop ini")