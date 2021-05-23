num = int(input("0과 1000 사이의 숫자를 입력하세요: "))
hundred_num = num//100
ten_num = num//10%10
one_num = num%10
print("이 자릿수들의 합은  ",hundred_num+ten_num+one_num,"입니다.")