filename = input("파일이름을 입력하세요: ")
f = open(filename, 'r')
letterCount = 0
wordCount = 0
lineCount = 0
while True:
    line = f.readline()
    if not line: break
    letterCount += len(line)
    arr = line.split(' ')
    wordCount += len(arr)
    lineCount += 1
    
print("단어수: ", wordCount)
print("문자수: ", letterCount)
print("행수: ", lineCount)

f.close()
