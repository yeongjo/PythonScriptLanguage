a = input("3x4 행렬의 행 0번에 대한 원소를 입력하세요: ").split()
a = [float(a[i]) for i in range(len(a))]
a1 = input("3x4 행렬의 행 1번에 대한 원소를 입력하세요: ").split()
a += [float(a1[i]) for i in range(len(a1))]
a2 = input("3x4 행렬의 행 2번에 대한 원소를 입력하세요: ").split()
a += [float(a2[i]) for i in range(len(a2))]

def sumColumn(m, columnIndex):
    return m[columnIndex]+m[columnIndex+4]+m[columnIndex+8]

for i in range(4):
    print("열 ",i,"번 원소의 총 합은 ",sumColumn(a, i),"입니다.")