def printChars(ch1, ch2, numberPerLine):
    i = 0
    while ord(ch1)+i <= ord(ch2):
        print(chr(ord(ch1)+i), end=" ")
        i+=1

        if i % numberPerLine == 0:
            print("")

    print("")

printChars('1', 'Z', 10)
