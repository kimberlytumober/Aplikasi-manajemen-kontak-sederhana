# Aplikasi Manajemen Kontak Sederhana

kontak = {}

def tampilkan_kontak():
    if not kontak:
        print("\nBelum ada kontak yang tersimpan.")
    else:
        print("\nDaftar Kontak:")
        for nama, nomor in kontak.items():
            print(f"- {nama} : {nomor}")

def tambah_kontak():
    nama = input("Masukkan nama kontak: ")
    nomor = input("Masukkan nomor telepon: ")
    kontak[nama] = nomor
    print("Kontak berhasil ditambahkan!")

def hapus_kontak():
    nama = input("Masukkan nama kontak yang ingin dihapus: ")
    if nama in kontak:
        del kontak[nama]
        print("Kontak berhasil dihapus!")
    else:
        print("Kontak tidak ditemukan.")

def menu():
    while True:
        print("\n=== Aplikasi Manajemen Kontak ===")
        print("1. Tampilkan Kontak")
        print("2. Tambah Kontak")
        print("3. Hapus Kontak")
        print("4. Keluar")

        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == "1":
            tampilkan_kontak()
        elif pilihan == "2":
            tambah_kontak()
        elif pilihan == "3":
            hapus_kontak()
        elif pilihan == "4":
            print("Terima kasih sudah menggunakan aplikasi!")
            break
        else:
            print("Pilihan tidak valid!")

menu()
