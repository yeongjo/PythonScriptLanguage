num = int(input("분에 대한 숫자를 입력하세요: "))
year = num//60//24//365
day = num//60//24%365
print(num,"분은 약 ",year,"년",day,"일 입니다.")