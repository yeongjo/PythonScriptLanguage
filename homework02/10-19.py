import random

ball_count = int(input("떨어뜨릴 공의 개수를 입력하세요: "))
slot_count = int(input("공 기계의 슬롯 개수를 입력하세요: "))

slots = [0 for i in range(slot_count)]

for i in range(ball_count):
    r_count = 0
    for j in range(slot_count):
        if random.randint(0,2) == 0:
            print("R", end='')
            r_count += 1
        else:
            print("L", end='')
    print("")
    slots[r_count] += 1

for j in range(ball_count,0,-1):
    for a in slots:
        if a < j:
            print(" ", end='')
        else:
            print("0", end='')

    print("")