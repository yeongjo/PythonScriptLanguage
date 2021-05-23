import numpy as np

def getRightmostLowestPoint(points):
    global len
    left_top_conner = np.array([-1000000,1000000])
    smallest_len = 0
    smallest_vec = [0,0]
    for i in range(0,len(points),2):
        a = np.array([points[i],points[i+1]])
        len = sum((a - left_top_conner) ** 2) ** (1 / 2)
        if smallest_len < len:
            smallest_len = len
            smallest_vec = a
    return smallest_vec[0],smallest_vec[1]

a = input("6개의 점을 입력하세요: ").split()
a = [float(a[i]) for i in range(len(a))]
print("최우측하단의 점은: ",getRightmostLowestPoint(a))