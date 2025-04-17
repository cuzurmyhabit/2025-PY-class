num1 = int(input("숫자 입력: "))
num2 = int(input("숫자 입력: "))

def result():
    sum = 0
    for i in range(num1, num2 + 1):
        sum += i

    print(sum)

result()