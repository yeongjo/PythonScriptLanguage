a = input("1과 100 사이의 정수들 입력: ").split()
a = [int(a[i]) for i in range(len(a))]

for i in range(len(a)):
    count = 0
    for j in range(len(a)):
        if a[i] == a[j]:
            count += 1

    print(a[i]," - ",count,"번 나타납니다.")