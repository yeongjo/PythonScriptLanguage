def decimalToBinary(value):
    print(value)
    a = ""
    while value > 0:
        a = (str(value%2)) + a
        value = int(value/2)

    print(a)

decimalToBinary( int(input("10진수 입력: ")))
