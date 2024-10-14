print("--------------------------------")
print("------- Dhita Olivia R.K -------")
print("---------- 2409116040 ----------")
print("--------------------------------")

# Masukkan Nilai atau Data 
jumlah_barang = int(input("Masukkan Jumlah Barang Yang Diinginkan: "))
harga_1_barang = float(input("Masukkan Harga 1 Barang: "))
kode_voucher = input("Masukkan Kode Voucher Yang Anda Punya: ")

# Menghitung Total Harga 
diskon = 0
total_harga = jumlah_barang * harga_1_barang

if jumlah_barang > 15:
    if kode_voucher == "DAPAT20":
        diskon = 20/100 * total_harga
        if diskon > 30000:
            diskon = 30000
elif jumlah_barang > 7:
    if kode_voucher == "DAPAT12":
        diskon = 12/100 * total_harga
        if diskon > 15000:
            diskon = 15000
elif jumlah_barang > 3:
    if kode_voucher == "DAPAT7":
        diskon = 7/100 * total_harga
        if diskon > 10000:
            diskon = 10000

total_harga_akhir = total_harga - diskon

print(f"Total Harga: Rp {total_harga}")
print(f"Anda Mendapat Diskon Sebesar: Rp {diskon}")
print(f"Total Harga Yang Harus Anda Bayar: Rp {total_harga_akhir}")