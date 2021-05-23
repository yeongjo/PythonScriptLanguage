a = input("숫자들을 입력: ").split()
a = [float(a[i]) for i in range(len(a))]

a_same_count_dict = {}

for i in a:
    if i in a_same_count_dict:
        a_same_count_dict[i] += 1
    else:
        a_same_count_dict[i] = 1

print(a_same_count_dict)

max_count = -1

for key,value in a_same_count_dict.items():
    if max_count < value:
        max_count = value

for key, value in a_same_count_dict.items():
    if max_count == value:
        print("숫자: ",key,"횟수: ",value)