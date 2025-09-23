class Person:
    def __init__(this, name, age):
        this.name = name
        this.age = age

    # 객체를 문자열로 표현하여 반환.
    def __str__(this):
        return f"{this.name}({this.age})"

    def intro(this):
        print(f"안녕하세요, 저는 {this.age}세 {this.name}입니다.")

#===============================
#객체 생성하기
p = Person("홍길동", 20)
print(p)
