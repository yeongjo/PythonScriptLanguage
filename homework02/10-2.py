a = input("정수들 입력: ").split()
a = [int(a[i]) for i in range(len(a))]
a.reverse()
[print(a[i]) for i in range(len(a))]