import numpy as np


a0 = input("3x3 행렬의 행 0번에 대한 원소를 입력하세요: ").split()
a0 = np.array([float(a0[i]) for i in range(len(a0))])
a1 = input("3x3 행렬의 행 1번에 대한 원소를 입력하세요: ").split()
a1 = np.array([float(a1[i]) for i in range(len(a1))])
a2 = input("3x3 행렬의 행 2번에 대한 원소를 입력하세요: ").split()
a2 = np.array([float(a2[i]) for i in range(len(a2))])

t = np.array([a0,a1,a2])
t.sort(0)
print(t)