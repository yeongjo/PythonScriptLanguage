import numpy as np
import math

def get_length(a,b):
    return sum((a-b)**2)**(1/2)

tripos = input("삼각형의 세 꼭짓점을 입력하세요: ")
pos = tripos.split(",")

n1 = np.array([float(pos[0]), float(pos[1])])
n2 = np.array([float(pos[2]), float(pos[3])])
n3 = np.array([float(pos[4]), float(pos[5])])
line1 = get_length(n1, n2)
line2 = get_length(n1, n2)
line3 = get_length(n1, n2)

s = (line1+line2+line3)/2
print("삼각형의 넓이는 ",math.sqrt(s*(s-line1)*(s-line2)*(s-line3)),"입니다.")