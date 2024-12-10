print("Pilih lah angka di bawah ini pasti kamu jodoh saya :")
print("1. Faktorial")                                         # fung si 
print("2. Fibonacci")
pilihan = input("Pilih (1 atau 2): ")
if pilihan != '1' and pilihan != '2':
    print("Tidak valid. Pilih 1 atau 2.")
else:                                                                # digunakan dalam struktur kondisional 
    angka = input("Masukkan bilangan bulat positif: ")
    if angka.isdigit() == False:             # belom ada pergraman nya 
        print("Input tidak valid. Masukkan bilangan bulat positif.")
    else:
        angka = int(angka)
        if angka < 0:                                                #pernyataan kondisional yang digunakan untuk mengeksekusi blok kode
            print("Harap masukkan bilangan positif.")
        else:
            if pilihan == '1':                                                   #kondisi 
                hasil = 1
                print(f"Proses faktorial dari {angka}:")
                for i in range(1, angka + 1):                                #digunakan untuk melakukan perulangan
                    hasil *= i                                              #faktorial
                    print(f"Iterasi ke-{i}, hasil sementara: {hasil}")
                print(f"Hasil faktorial dari {angka} adalah {hasil}")
            elif pilihan == '2':                                            #fabonaci  struktur pengkondisian
                print(f"Proses Fibonacci hingga bilangan ke-{angka}:")
                if angka == 0:                         
                    print("Bilangan Fibonacci ke-0 adalah 0")
                elif angka == 1:
                    print("Bilangan Fibonacci ke-1 adalah 1")
                else:
                    a, b = 0, 1
                    print(f"Iterasi ke-0, nilai: {a}")
                    print(f"Iterasi ke-1, nilai: {b}")
                    for i in range(2, angka + 1):                     #digunakan untuk melakukan perulangan
                        a, b = b, a + b
                        print(f"Iterasi ke-{i}, nilai: {b}")
                    print(f"Bilangan Fibonacci ke-{angka} adalah {b}")

