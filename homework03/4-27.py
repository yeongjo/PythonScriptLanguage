a = input("점 x와 y 좌표값을 입력하세요: ").split()
a = [float(a[i]) for i in range(len(a))]

if -1/2*a[0]+100 > a[1] and a[0] > 0 and a[1] > 0:
    print("점은 삼각형의 내부에있습니다.")
else:
    print("점은 삼각형의 내부에 있지 않습니다.")
