import time
def encode_lz78(text):
    startc = time.time()
    dictionary = dict()
    i = 0
    index = 1
    encodedNumbers = []
    encodedLetters = []
    while i < len(text):
        stringToBeSaved = text[i]
        indexInDictionary = 0
        while stringToBeSaved in dictionary:
            indexInDictionary = dictionary[stringToBeSaved]
            if (i == len(text) - 1):
                stringToBeSaved = " "
                break
            i = i + 1
            stringToBeSaved = stringToBeSaved + text[i]
        encodedNumbers.append(indexInDictionary)
        encodedLetters.append(stringToBeSaved[len(stringToBeSaved) - 1])
        if (stringToBeSaved not in dictionary):
            dictionary[stringToBeSaved] = index
            index = index + 1
        i = i + 1

    endc = time.time()
    print("Tempo de codificacao:", endc - startc)

    return encodedNumbers, encodedLetters, dictionary


l = []
def decode_lz78(encodedNumbers, encodedLetters, dictionary):
    startd = time.time()
    i = 0

    while(i<len(encodedNumbers)):

        if (encodedNumbers[i] != 0):

            l.append(list(dictionary.keys())[list(dictionary.values()).index(encodedNumbers[i])])

        l.append(encodedLetters[i])

        i = i + 1

    endd = time.time()
    print("Tempo de Descodificação:", endd - startd)
    return l


print("Algoritmo de Compressão LZ78")
print("=================================================================")
h = int(input("Introduza 1 se pretende introduzir a string pelo terminal ou 2 se pretende ler de um ficheiro:"))
if h == 1:
    stringToEncode = input("Introduza a string que pretende comprimir:")
elif h == 2:
    file = input("Introduza o nome do ficheiro:")
    with open(file, 'r') as f:
        stringToEncode = f.read()
else:
    print("Ficheiro não encontrado!")
# print ("String introduzida:",stringToEncode)
print("Ficheiro introduzido foi comprimido e guardado em compressed.txt")
[encodedNumbers, encodedLetters, dictionary] = encode_lz78(stringToEncode)

output = open("compressed.txt", "w+")

i = 0
# escrever para o ficheiro comprimido
while i < len(encodedNumbers):
    output.write(str(encodedNumbers[i]) + encodedLetters[i])
    i = i + 1

#decode_lz78(encodedNumbers, encodedLetters, dictionary)

# abertura de ficheiros
decodedFile = open("Decoded.txt", 'w')
readfromfile = open('webster', 'r')  # trocar para o nome do ficheiro
inputFile = readfromfile.read()
readfromfile1 = open('compressed.txt', 'r')
compressedFile = readfromfile1.read()

j = 0
# caso seja um input pequeno, mostra o dicionario e escreve para o terminal, caso contrário escreve para o ficheiro e mostra apenas o resutlado final
if h == 1:
    while j < len(encodedNumbers):
        print("{", encodedNumbers[j], ":", encodedLetters[j], "}", end=" ")
        j = j + 1
    print("\n")
    print("String Descodificada:", "".join(l))
    # print("Racio de compressao:", len(stringToEncode) / len(compressedFile))
elif h == 2:
    print("Racio de compressao:", len(inputFile) / len(compressedFile))
    decodedFile.write("".join(l))
