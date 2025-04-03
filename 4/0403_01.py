a = int(input("성적을 입력하세요: "))

if a >= 90 :
    print("A")
elif a >= 80 :
    if a < 90 :
        print("B")
elif a >= 70 :
    if a < 80 :
        print("C")
else :
    print("D")