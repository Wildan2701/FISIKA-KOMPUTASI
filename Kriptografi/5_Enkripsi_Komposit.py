#Metode Komposit Sederhana
import sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = 'SESUNGGUHNYA DALAM PENCIPTAAN LANGIT DAN BUMI DAN PERGANTIAN MALAM DAN SIANG TERDAPAT TANDA TANDA KEBESARAN ALLAH BAGI ULIL AL BAB'

    #Substitusi
    myKey = 'BADCFEHGJILKNMPORQTSVUXWZY'
    myMode = 'enkripsi' # Set sebagai 'enkripsi' atau 'deskripsi'

    if not keyIsValid(myKey):
        sys.exit('Terdapat error pada kunci atau simbol')
    if myMode == 'enkripsi':
        translated = encryptMessage(myKey, myMessage)
        output = str(translated)
    elif myMode == 'dekripsi':
        translated = decryptMessage(myKey, myMessage)
    print('Menggunakan Kunci: %s'% (myKey))
    print('Pesan Ter%s Tahap 1:'% (myMode))
    print(translated)

    #transposisi
    myMessage2 = str(translated)
    myKey2 = 8
    ciphertext = encryptMessage2(myKey2, myMessage2)
    print('Pesan Terenkripsi Tahap 2:')
    # Print pesan terenkripsi
    # simbol | ("pipe" character) setelah pesan enkripsi untuk spasi
    # akhir dari pesan terenkripsi
    print (ciphertext + '|')

# Metode enkripsi substitusi
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

# Metode enkripsi transposisi
def encryptMessage2(key, message):
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
