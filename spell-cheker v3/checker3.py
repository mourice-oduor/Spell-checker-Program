####Spell Checker with functions####

from textblob import TextBlob


def f():
    global a 
    a = inputFile.read()
    print("original text : "+str(a))
    b = TextBlob(a)
# print("original text : "+str(a))


def readDictionaryFile(dictionaryFilename):
    dictionarywords = []
    inputFile = open(dictionaryFilename, "r")
    # a = inputFile.read()
    # print("original text : "+str(a))
    
    # b = TextBlob(a)

    for line in inputFile:
        word = line.strip()
        dictionarywords.append(word)
    inputFile.close()
    return dictionarywords


def readTextFile(textFilename):
    words = []
    inputFile = open(textFilename, "r")
    # a = inputFile.read()

    for line in inputFile:
        wordsOnLine = line.strip().split()
        for word in wordsOnLine:
            words.append(word.strip(".,!\;:?").lower())
    inputFile.close()
    return words


def findErrors(dictionarywords, textwords):
    misspelledwords = []
    for word in textwords:
        if word not in dictionarywords:
            misspelledwords.append(word)
    return misspelledwords

def printErrors(errorList):
    print("The misspelled words are: ")
    for word in errorList:
        print(word)


def main():
    print('Welcome to my Spell Checker!!')
    dictionaryFile = input('Please enter the dictionary file: ')
    textFile = input('Please enter the text file: ')
    dictionaryList = readDictionaryFile(dictionaryFile)
    textList = readTextFile(textFile)
    errorList = findErrors(dictionaryList, textList)
    printErrors(errorList)
    

# a = globals
# b = TextBlob(a)
# print("corrected text : "+str(b.correct()))
# inputFile.close()

# d = open("dictionary.txt", "w")
# d.write(str(b.correct()))
# d.close()

if __name__ == '__main__':
    main()
    
