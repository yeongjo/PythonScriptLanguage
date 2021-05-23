temperature = float(input("화씨 -58°F 와 41°F 사이의 온도를 입력하세요: "))
wind_speed = float(input("풍속을 시간 당 마일 단위로 입력하세요: "))
print("체감온도는 ",35.74 + 0.6215*temperature - 35.75*wind_speed**0.16 + 0.4275*temperature*wind_speed**0.16," 입니다.")