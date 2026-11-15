# Project Mini use Loop Simple : Simulasi Percobaan Login dengan Batas Maksimal

password = "admin123"
try_input = ["123456", "admin", "rahasia", "halloword", "admin123"]

for index, tebakan in enumerate(try_input, start=1):
    print(f"Percobaan ke-{index} memasukkan: '{tebakan}'")
    if tebakan == password:
        print("-> Akses diterima! Perulangan dihentikan")
        break
else:
    print("-> Akun terkunci kerena gagal terus")