#Metode Substitusi Sederhana
import sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = 'DBAF NFQBG CJ CBOVQ'
    myKey = 'BADCFEHGJILKNMPORQTSVUXWZY'
    myMode = 'dekripsi' # Set sebagai 'enkripsi' atau 'deskripsi'

    if not keyIsValid(myKey):
        sys.exit('Terdapat error pada kunci atau simbol')
    if myMode == 'enkripsi':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'dekripsi':
        translated = decryptMessage(myKey, myMessage)
    print('Menggunakan Kunci: %s'% (myKey))
    print('Pesan Ter%s:'% (myMode))
    print(translated)

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
