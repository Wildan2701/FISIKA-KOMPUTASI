#Metode Dekripsi Komposit

import math
import sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    # dekripsi transposisi
    myMessage = 'XKJBJ TV JF C FZKMBBPMMLTN C NLBNMBJ MGM VBBFOKBNABLBF LBHCT MMFBMBVN NNLCFJBBJLHFMM LTVBOAFFL MMBBHNIHABK LVVDMVH NVAVJV BSB TVHBPINIVOVQSNSGJMNMBBS'
    myKey = 8
    plaintext = decryptMessage2(myKey, myMessage)
    print('Pesan Terenkripsi Tahap 1:')
    # print simbol | ("pipe" character) setelah pesan terenkripsi
    print (plaintext + '|')

    # dekripsi substitusi
    myMessage = str(plaintext)
    myKey = 'BADCFEHGJILKNMPORQTSVUXWZY'
    myMode = 'dekripsi' # Set sebagai 'enkripsi' atau 'deskripsi'

    if not keyIsValid(myKey):
        sys.exit('Terdapat error pada kunci atau simbol')
    if myMode == 'enkripsi':
        translated = encryptMessage(myKey, myMessage)
        output = str(translated)
    elif myMode == 'dekripsi':
        translated = decryptMessage(myKey, myMessage)
    print('Menggunakan Kunci: %s'% (myKey))
    print('Pesan Ter%s Tahap 2:'% (myMode))
    print(translated)
    
# Metode Dekripsi Transposisi

def decryptMessage2(key, message):
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

# Metode Dekripsi Substitusi
def keyIsValid(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    return keyList == lettersList

def encryptMessage(key, message):
    return translateMessage(key, message, 'enkripsi')

def decryptMessage(key, message):
    return translateMessage(key, message, 'dekripsi')

def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'dekripsi':
        # Untuk dekripsi kita dapat menggunakan kode sama dengan enkripsi
        # Kita hanya perlu menuar dimana string kuncidan huruf digunakan
        charsA, charsB = charsB, charsA

    # Ulangi setiap simbol dalam pesan
    for symbol in message:
        if symbol.upper() in charsA:
            # Enkripsi/dekripsi simbol:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # Simbol bukan huruf; hanya perlu tambahkan
            translated += symbol

    return translated

def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

if __name__ == '__main__':
    main()
