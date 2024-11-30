def kalkulator_transportasi():
    data = []  # Menyimpan data hasil perhitungan

    def tampilkan_data():
        if not data:
            print("Tidak ada data yang disimpan.\n")
        else:
            hasil = "=== Data Perhitungan ===\n"
            indeks = 1
            for item in data:
                hasil += f"{indeks}. {item}\n"
                indeks += 1
            print(hasil)

    def simpan_data(tipe, hasil):
        data.append(f"{tipe}: {hasil}")

    print(
        "=== Kalkulator Transportasi dan Logistik ===\n"
        "Pilih Menu dibawah ini:\n"
        "1. Hitung Biaya Transportasi\n"
        "2. Hitung Volume Muatan\n"
        "3. Hitung Waktu Perjalanan\n"
        "4. Tampilkan Data Perhitungan\n"
        "5. Update Data Perhitungan\n"
        "6. Hapus Data Perhitungan\n"
        "7. Keluar\n"
    )

    while True:
        pilihan = int(input("Masukkan Pilihan (1-7): "))

        if pilihan == 1:
            jarak = float(input("Masukkan jarak perjalanan (km): "))
            biaya_per_km = float(input("Masukkan biaya per km (Rp): "))
            biaya_total = jarak * biaya_per_km
            simpan_data("Biaya Transportasi", f"Jarak: {jarak} km, Biaya per km: Rp{biaya_per_km}, Total: Rp{biaya_total}")
            print(f"Total biaya transportasi: Rp{biaya_total}\n")
        
        elif pilihan == 2:
            panjang = float(input("Masukkan panjang muatan (meter): "))
            lebar = float(input("Masukkan lebar muatan (meter): "))
            tinggi = float(input("Masukkan tinggi muatan (meter): "))
            volume = panjang * lebar * tinggi
            simpan_data("Volume Muatan", f"Panjang: {panjang} m, Lebar: {lebar} m, Tinggi: {tinggi} m, Volume: {volume} m³")
            print(f"Volume muatan: {volume} meter kubik\n")
        
        elif pilihan == 3:
            jarak = float(input("Masukkan jarak perjalanan (km): "))
            kecepatan = float(input("Masukkan kecepatan rata-rata (km/jam): "))
            waktu = jarak / kecepatan
            simpan_data("Waktu Perjalanan", f"Jarak: {jarak} km, Kecepatan: {kecepatan} km/jam, Waktu: {waktu} jam")
            print(f"Waktu perjalanan: {waktu} jam\n")
        
        elif pilihan == 4:
            tampilkan_data()
        
        elif pilihan == 5:
            tampilkan_data()
            if data:
                index = int(input("Masukkan nomor data yang ingin diperbarui: "))
                if 1 <= index <= len(data):
                    print(f"Data yang akan diperbarui: {data[index - 1]}")
                    print(
                        "Pilih kembali jenis perhitungan yang ingin diperbarui:\n"
                        "1. Hitung Biaya Transportasi\n"
                        "2. Hitung Volume Muatan\n"
                        "3. Hitung Waktu Perjalanan\n"
                    )
                    update_pilihan = int(input("Masukkan Pilihan (1-3): "))

                    if update_pilihan == 1:
                        jarak = float(input("Masukkan jarak perjalanan (km): "))
                        biaya_per_km = float(input("Masukkan biaya per km (Rp): "))
                        biaya_total = jarak * biaya_per_km
                        data[index - 1] = f"Biaya Transportasi: Jarak: {jarak} km, Biaya per km: Rp{biaya_per_km}, Total: Rp{biaya_total}"
                        print(f"Data berhasil diperbarui: Biaya Transportasi - Rp{biaya_total}\n")
                    
                    elif update_pilihan == 2:
                        panjang = float(input("Masukkan panjang muatan (meter): "))
                        lebar = float(input("Masukkan lebar muatan (meter): "))
                        tinggi = float(input("Masukkan tinggi muatan (meter): "))
                        volume = panjang * lebar * tinggi
                        data[index - 1] = f"Volume Muatan: Panjang: {panjang} m, Lebar: {lebar} m, Tinggi: {tinggi} m, Volume: {volume} m³"
                        print(f"Data berhasil diperbarui: Volume Muatan - {volume} m³\n")
                    
                    elif update_pilihan == 3:
                        jarak = float(input("Masukkan jarak perjalanan (km): "))
                        kecepatan = float(input("Masukkan kecepatan rata-rata (km/jam): "))
                        waktu = jarak / kecepatan
                        data[index - 1] = f"Waktu Perjalanan: Jarak: {jarak} km, Kecepatan: {kecepatan} km/jam, Waktu: {waktu} jam"
                        print(f"Data berhasil diperbarui: Waktu Perjalanan - {waktu} jam\n")
                    
                    else:
                        print("Pilihan tidak valid.\n")
                else:
                    print("Nomor data tidak valid.\n")
        
        elif pilihan == 6:
            tampilkan_data()
            if data:
                index = int(input("Masukkan nomor data yang ingin dihapus: "))
                if 1 <= index <= len(data):
                    data.pop(index - 1)
                    print("Data berhasil dihapus.\n")
                else:
                    print("Nomor data tidak valid.\n")
        
        elif pilihan == 7:
            print("Terima kasih telah menggunakan kalkulator ini!\n")
            break
        
        else:
            print("Pilihan tidak valid. Coba lagi.\n")
            
kalkulator_transportasi()