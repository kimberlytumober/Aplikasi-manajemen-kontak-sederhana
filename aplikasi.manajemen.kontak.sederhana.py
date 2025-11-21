# Aplikasi Manajemen Kontak Sederhana

kontak = {}

def tampilkan_kontak():
    if not kontak:
        print("\nBelum ada kontak yang tersimpan.")
    else:
        print("\nDaftar Kontak:")
        for nama, nomor in kontak.items():
            print(f"- {nama} : {nomor}")
