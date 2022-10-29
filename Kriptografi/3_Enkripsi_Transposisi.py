# Metode Transposisi Sederhana

def main():
    myMessage = 'CABE MERAH DI DAPUR'
    myKey = 8
    ciphertext = encryptMessage(myKey, myMessage)

    # Print pesan terenkripsi
    # simbol | ("pipe" character) setelah pesan enkripsi untuk spasi
    # akhir dari pesan terenkripsi
    print (ciphertext + '|')

def encryptMessage(key, message):
    # Tiap string pada enkripsi menunjukkan kolom pada grid.
    ciphertext = [''] * key

    # Ulangi setiap kolom pada enkripsi
    for column in range(key):
        currentIndex = column

        # Terus mengulangi sampai index baru  mencapai panjang pesan.
        while currentIndex < len(message):
            #Tempatkan karakter pada indeks baru dalam pesan
            #di akhir kolom dalam list enkripsi text.
            ciphertext[column] += message[currentIndex]

            #Pindahkan indeks baru ke atas
            currentIndex += key

    # Ubah list enkripsi text menjadi nilai string tunggal dan kembalikan.
    return ''.join(ciphertext)

if __name__ == '__main__':
    main()
