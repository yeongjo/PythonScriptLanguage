import random

getting_number = 0
for i in range(10000000):
    a = [random.random()*2-1, random.random()*2-1]
    if -1/2*a[0]+100 > a[1]  and a[1] > 0:
        getting_number += 1

print(getting_number, "번 맞췄습니다.")