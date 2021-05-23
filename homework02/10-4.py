a = input("1과 100 사이의 정수들 입력: ").split()
a = [int(a[i]) for i in range(len(a))]

middle=0
for i in range(len(a)):
    middle += a[i]
middle/=len(a)

larger_count = 0
smaller_count = 0
for i in range(len(a)):
    if a[i] >= middle:
        larger_count += 1
    else:
        smaller_count += 1

print("큰수개수: ", larger_count)
print("작은수개수: ", smaller_count)