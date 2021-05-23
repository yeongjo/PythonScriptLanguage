from math import *

def get_distance(pos1, pos2):
    return 6370.01 * acos(sin(pos1[0])*sin(pos2[0])+cos(pos1[0])*cos(pos2[0])*cos(pos1[1]-pos2[1]))

def get_area_of_triangle(l1, l2, l3):
    s = (l1 + l2 + l3) / 2
    return sqrt(s * (s - l1) * (s - l2) * (s - l3))

pos = [[37.565289,126.8491259],[37.7637326,128.8824475],[35.1645701,129.0015892],[35.1768201,126.7735892]]
length = [get_distance(pos[0],pos[1]),get_distance(pos[1],pos[2]),get_distance(pos[0],pos[2]),get_distance(pos[2],pos[3]),get_distance(pos[0],pos[3])]
total_area = get_area_of_triangle(length[0],length[1],length[2]) + get_area_of_triangle(length[3],length[4],length[2])

print("전체넓이는 ",total_area)