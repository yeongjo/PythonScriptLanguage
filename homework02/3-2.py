from math import *
x1,y1 = map(float, input("첫번째 점 (위도와 경도)을 60분법 각으로 입력하세요: ").split(","))
x2,y2 = map(float, input("두번째 점 (위도와 경도)을 60분법 각으로 입력하세요: ").split(","))
d = 6370.01 * acos(sin(x1)*sin(x2)+cos(x1)*cos(x2)*cos(y1-y2))
print("두저마이의 거리는 ",d)