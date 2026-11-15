# Exsample : Split Bill Simple
# Type data
name_location = "Kopi Kenangan" #str
total_bill = 150000.0 #float
jumlah_org = 4 #int
ppn_persen = 10

total_akhir = total_bill + (total_bill * ppn_persen / 100)
bayar_per_orang = total_akhir / jumlah_org

# Cetak use f-string untuk menyisipkan variabel ke dalam teks
print(f"Struk {name_location}")
print(f"Total setelah pajak {ppn_persen}% : Rp.{total_akhir:,.0f}") # fungsi dari ":,.0f" = angka koma dibelakang adalah 0 ankga
print(f"Patungan per orang ({jumlah_org} org): Rp.{bayar_per_orang:,.0f}")