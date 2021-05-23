a = input("1과 100 사이의 정수들 입력: ").split()
a = [int(a[i]) for i in range(len(a))]

def indexOfSmallestElement(lst):
    smallest = 10000000
    smallest_idx = -1
    for i in range(len(lst)):
        if smallest > lst[i]:
            smallest = lst[i]
            smallest_idx = i
    return smallest_idx

print(a)
print(indexOfSmallestElement(a))