grade = int(input("학년 입력: "))
ban = int(input("반 입력: "))

if grade == 2:
    if (grade + ban) % 2 == 1:
        if ban == 1:
            print("부담임 선생님은 ooo 선생님입니다.")
        elif ban == 2:
            print("부담임 선생님은 ooo 선생님입니다.")
        elif ban == 3:
            print("부담임 선생님은 이윤지 선생님입니다.")
        elif ban == 4:
            print("부담임 선생님은 ooo 선생님입니다.")
        elif ban == 5:
            print("부담임 선생님 성함이 어떻게 되시나요?????")
        elif ban == 6:
            print("부담임 선생님은 ooo 선생님입니다.")
        else:
            print("존재하지 않는 반입니다.")
    else:
        if ban == 1:
            print("담임 선생님은 정혜선 선생님입니다.")
        elif ban == 2:
            print("담임 선생님은 권지웅 선생님입니다.")
        elif ban == 3:
            print("담임 선생님은 박성래 선생님입니다.")
        elif ban == 4:
            print("담임 선생님은 임진하 선생님입니다.")
        elif ban == 5:
            print("담임 선생님 성함이 어떻게 되시나요?????")
        elif ban == 6:
            print("담임 선생님은 손명수 선생님입니다.")
        else:
            print("존재하지 않는 반입니다.")
else:
    print("2학년 학생만 사용할 수 있어요 ㅎㅎ")
