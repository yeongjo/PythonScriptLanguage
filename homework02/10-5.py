a = input("1과 100 사이의 정수들 입력: ").split()
a = [int(a[i]) for i in range(len(a))]

print("중복을 제거한 고유한 숫자: ",list(set(a)))