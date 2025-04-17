fruit = {
    '사과': 1000,
    '배': 2000,
    '감': 3000,
    '샤인머스켓': 4000,
    '딸기': 5000,
    '바나나': 6000,
    '포도': 7000,
    '블루베리': 8000
}

sum = 0

while True:
    print("최소 금액 10000원")
    fruit_name = input("과일 이름 입력:")

    if fruit_name == '장바구니':
        if sum < 10000:
            print("최소 금액을 채워 주세요")
        else:
            print("구매 가능합니다")
            break

    if fruit_name in fruit:
        sum += fruit[fruit_name]
        print("현재 금액 " + str(sum) + " 원")

    if sum < 10000:
        print("최소 주문금액을 채워주세요")