import math

a = input("A, b, c를 입력하세요: ").split()
a = [float(a[i]) for i in range(len(a))]

detect_num = a[1]**2-4*a[0]*a[2]
r1 = (-a[1]+math.sqrt(detect_num))/2*a[0]
r2 = (-a[1]-math.sqrt(detect_num))/2*a[0]

if detect_num > 0:
    print("실근은 ",r1, "과 ",r2, "입니다.")
elif detect_num == 0:
    print("실근은 ",r1 , "입니다.")
else:
    print("이 방정식은 실근이 존재하지 않습니다.")

