def tampilkan_barang():
    print("======Daftar Barang======")
    print("1. Laptop MSI       - Rp75.000")
    print("2. GPU RTX 5090     - Rp88.000")
    print("3. Monitor Gaming   - Rp50.000")
    print("4. Hp Iphone 18 Pro - Rp.99.900")
    print("5. Mouse Gaming     - Rp.25.000")
    print("0. Keluar")

def hitung_pembayaran(total):
    if total >= 100000:
        diskon = total * 10 / 100
    else:
        diskon = 0

    total_bayar = total - diskon
    return diskon, total_bayar

while True:
    tampilkan_barang()
    kode = input("Masukkan Kode barang anda: ")

    if kode == "0":
        print("Transaksi Selesai")
        break
    elif kode == "1":
        barang = "Laptop MSI"
        harga = 75000
    elif kode == "2":
        barang = "GPU RTX 5090"
        harga = 88000
    elif kode =="3":
        barang = "Monitor Gaming"
        harga = 50000
    elif kode =="4":
        barang = "HP Iphone 18 Pro"
        harga = 99900
    elif kode =="5":
        barang = "Mouse Gaming"
        harga = 25000
    else:
        print("Pilihan Tidak Valid Kocak!")
        continue
    jumlah = int(input("Masukkan jumlah barang yang ingin anda beli bray: "))

    if jumlah <=0:
        print("Jumlah Pembelian harus lebih dari 0")
        continue

    total = harga * jumlah
    diskon, total_bayar = hitung_pembayaran(total)
    

    print("\n===== STRUK PEMBELIAN =====")
    print("Nama Barang   :", barang)
    print("Harga Satuan  : Rp", format(harga, ",").replace(",", "."))
    print("Jumlah Beli   :", jumlah)
    print("Total Belanja : Rp", format(total, ",").replace(",", "."))
    print("Diskon        : Rp", format(int(diskon), ",").replace(",", "."))
    print("Total Bayar   : Rp", format(int(total_bayar), ",").replace(",", "."))
   


    

