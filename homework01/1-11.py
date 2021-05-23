passed_year = 5
passed_sec = passed_year*365*24*60

human_count = 312032486

add_human_count = passed_sec//7
remove_human_count = passed_sec//13
immigrant_human_count = passed_sec//45

total_human_count = human_count

print(add_human_count," ",remove_human_count," ",immigrant_human_count," ")

while(True):
    total_human_count = total_human_count + add_human_count - (remove_human_count+immigrant_human_count)
    print("5년후 인구수 ",total_human_count)
    input()
