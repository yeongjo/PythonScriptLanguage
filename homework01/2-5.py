str_subtotal_and_tip = input("소계와 팁 비율을 입력하세요: ")
subtotal_and_tip = str_subtotal_and_tip.split(",")
subtotal = float(subtotal_and_tip[0])
tip_ratio = float(subtotal_and_tip[1])
tip = subtotal/100*tip_ratio
print("팁은 ",tip,"이고 총액은 ",tip+subtotal,"입니다.")