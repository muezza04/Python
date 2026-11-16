# Project Mini : Management inventaris sederhana

inventaris = {
    "Kopi Arabika" : {"stok": 15, "harga": 23000},
    "Kopi Kenangan" : {"stok": 10, "harga": 20000},
}

# Menambah item baru (add) dan mengurangi stok item lama (delete)
inventaris["Ameracano"] = {"stok": 20, "harga": 15000} # add key and value (tidak boleh add key yg sudah ada)
inventaris["Kopi Kenangan"]["stok"] -= 5 # -= edit directory yang sudah ada

print("========Daftar Stok Gudang========")
for nama_barang, info in inventaris.items(): # fungsi dari .items() disini untuk mengambil nilainya.
    print(f"- {nama_barang}: {info['stok']} pcs (Rp{info['harga']:,})")