a = input("1과 100 사이의 정수들 입력: ").split()
a = [int(a[i]) for i in range(len(a))]

def isSorted(lst):
    smallest = -1
    for i in range(len(lst)):
        if lst[i] >= smallest:
            smallest = lst[i]
        else:
            return False
    return True

if isSorted(a):
    print("리스트는 이미 정렬되어 있습니다.")
else:
    print("리스트는 정렬되어 있지 않습니다.")