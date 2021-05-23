money = float(input("약정 금액을 입력하세요: "))
interest_rate = float(input("연이율(%)을 입력하세요: "))
year_range = float(input("약정 기간(년) 을 입력하세요: "))
print("월 납입금: ",money/((1+interest_rate)*(year_range*12)))