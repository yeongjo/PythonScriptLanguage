def reverse(number):
    return int(''.join(reversed(str(number))))

a = input("역수출력할수 아무거나 입력: ")
print(reverse(a))