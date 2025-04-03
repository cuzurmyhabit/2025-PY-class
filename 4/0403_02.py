사과 = 1000
배 = 2000
감 = 3000
샤인머스켓 = 4000
딸기 = 5000
바나나 = 6000
포도 = 7000
블루베리 = 8000

sum = 0

print("최소 주문 금액: 5000원")
fruit = input("과일 이름 입력: ")

if fruit == "사과":
    sum += 사과
elif fruit == "배":
    sum += 배
elif fruit == "감":
    sum += 감
elif fruit == "샤인머스켓":
    sum += 샤인머스켓
elif fruit == "딸기":
    sum += 딸기
elif fruit == "바나나":
    sum += 바나나
elif fruit == "포도":
    sum += 포도
elif fruit == "블루베리":
    sum += 블루베리

if sum >= 5000 :
    print("구매 가능합니다")
else :
    print("최소 주문 금액을 채워 주세요.")