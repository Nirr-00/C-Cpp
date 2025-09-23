num = int(input("1~10 사이의 숫자를 입력하세요: "))

if num < 1 or num > 10:
    print("잘못된 입력입니다.")
elif num == 1:
    print(f"{num}은(는) 소수가 아닙니다.")
elif num == 2 or num == 3 or num == 5 or num == 7:
    print(f"{num}은(는) 소수입니다.")
else:
    print(f"{num}은(는) 소수가 아닙니다.")
