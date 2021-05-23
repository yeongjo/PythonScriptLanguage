a = input("세개의수를 입력하세요: ").split()
a = [float(a[i]) for i in range(len(a))]

def displaySortedNumbers(num1, num2, num3):
    t = [num1, num2, num3]
    t.sort()
    print("정렬된 숫자는 ",t,"입니다")

displaySortedNumbers(a[0],a[1],a[2])