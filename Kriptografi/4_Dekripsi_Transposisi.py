# Metode Transposisi Sederhana
import math

def main():
    myMessage = 'CAPAHUB RED IM EDRA'
    myKey = 8
    plaintext = decryptMessage(myKey, myMessage)

    # print simbol | ("pipe" character) setelah pesan terenkripsi
    print (plaintext + '|')

def decryptMessage(key, message):
    # Fungsi dekripsi transposisi akan mensimulasikan "kolom" dan "baris"
    # dari grid tempat plaintext ditulis dengan menggunakan list string.
    # Pertama, kita perlu menghitung beberapa nilai.

    # Jumlah "kolom" pada grid transposisi:
    numOfColumns = int(math.ceil(len(message) / float(key)))
    # Jumlah "baris" pada grid transposisi:
    numOfRows = key
    # Jumlah "elemen kosong" pada akhir "kolom" grid:
    numOfshadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Tiap string pada plaintext mewakili kolom pada grid.
    plaintext = [''] * numOfColumns

    # Variabel kolom dan baris menunjuk kemana di grid berikutnya
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1 # titik ke kolom berikutnya.

        # Jika tidak ada lagi kolom atau berada di kotak yang diarsir
        # kolom pertama dan baris berikutnya:
        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfshadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)

if __name__ == '__main__':
    main()
