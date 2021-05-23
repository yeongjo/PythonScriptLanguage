a1 = input("사원 이름을 입력하세요:")
a2 = float(input("주 당 근무시간을 입력하세요:"))
a3 = float(input("시간 당 급여를 입력하세요:"))
a4 = float(input("원천징수세율을 입력하세요"))
a5 = float(input("지방세율을 입력하세요:"))

t = a2*a3

print("사원이름: ", a1)
print("주당 근무시간: ", a2)
print("임금: ", a3)
print("총 급여: ", t)

print("공제: ")
print("  원천징수세(","%0.1f"%float(a4*100),"%): ", a4*t)
print("  주민세(","%0.1f"%float(a5*100),"%): ", t*a5)
print("  총 공제: ", a4*t+t*a5)
print("공제 후 급여: ", t-(a4*t+t*a5))