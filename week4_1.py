#함수 정의 연습
def printHello():
    print("Hello Python!!")

#---------------------------------------    
def sayHello(name):
    print(f"안녕하세요 {name}씨, 반갑습니다.")
#---------------------------------------
def intro(name = "김종현", age=20):
    print(f"저는 {age}세, {name}입니다.")
#---------------------------------------
def myFruits(*fruits): #호출시 전달되는 인수들은 list에 담겨 fruits에 전달된다.
    for item in fruits:
        print(f"I like {item}.")
#---------------------------------------
def average(*n):
    if len(n) == 0:  # 입력값이 없을 경우 대비
        print("값을 입력해주세요.")
        return

    print(f"평균값은 {sum(n) / len(n):.2f}입니다.")  # 소수점 두 자리까지 출력
#----------------------------------------
#함수호출
average(11,23)
