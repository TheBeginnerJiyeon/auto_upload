# 한 줄, 여러 줄 주석 처리
""" alt + shift + a(바꿈)
print("mulcam")
print("hihi") """


# 원시 데이터 타입 int, float, string, boolean

num_int=30
print(type(num_int)) # <class 'int'>

num_float=30.012
print(type(num_float)) # <class 'float'>

# boolean

a= True or False
print(a) # True

# operation - parameter

x=6
y=3
result1=x+y
result2=x-y
result3=x*y
result4=x/y
print(result1,result2,result3,result4)

""" print(1/0) ZeroDivisionError: division by zero """

print(x//y) # 몫

print(x%y) # 나머지

x=2
result=x**4
print(result)

# 조건 연산자
x=400
y=456
print(x==y,x>=y,x<y) # False False True

# 사용자에게 입력받기

""" a=input("임의의 숫자를 입력: ")
b=input("임의의 숫자를 입력: ")
print(type(a)) # 임의의 숫자를 입력: 3, <class 'str'>
print(type(int(a))) # <class 'int'>
# 입력값은 문자 >> 숫자로 변환해준다
a=int(a)
b=int(b)
print(a,b)
print(a*b,type(a*b)) """

# 논리 연산자

print(True or False) # True
print((3>2) or (2<3)) # True

# string -1. 덧셈, 곱셈, indexing, slicing

a="boy"
b="loves"
c="girl"

letter= a +" " + b + " " + c + "forever"
x="야야야야야....사랑한다고"
print(x*5) # 사랑한다고.....사랑한다고.....사랑한다고.....사랑한다고.....사랑한다고.....

# indexing
print(x[-5:]) # [-5:-1]로 하면 마지막은 제외니까 안됨!! 헷갈리지 말 것

print()

email='drwill@naver.com'
print(email[:5])
print(email[7])

tel='010-5123-7890'

print(tel[-9:-5])

주소='서울시 강남구 대치3동 멀티캠퍼스 옆 pc방'

print(주소[4:7],주소[8:12])

전주소="  서울시 강남구 선릉역 1번 출구"
처리한_전주소=전주소.strip()
처리한_전주소=전주소.lstrip()
print(처리한_전주소)

# 이 주소로 가려면 어느 지하철 무슨역?
index=처리한_전주소.find("역")
print(index, 처리한_전주소[index-2:index+1]) 

print(처리한_전주소.index("역")) # 10. index는 숫자도 가능
print(처리한_전주소.find("역")) # 10

""" print(처리한_전주소.index("왈")) # ValueError: substring not found """
print(처리한_전주소.find("뢍")) # -1 value error 안냄

""" # index() 
- 문자열, 리스트, 튜플 다 가능
- 찾고자 하는 값이 존재하면 그 위치의 index 반환
- 단 찾는 값이 없으면 >> 에러 발생(value error)

# find 문자열에 사용
- 주로 문자열에 사용
- 찾고자 하는 값이 존재하면 그 위치의 index 반환
- 단 찾는 값이 없으면 -1 반환
- 문자열 검색 시 , 예외 처리가 필요없다는 장점 """

""" a=1,2,3,4,5
print(a.find(1)) # AttributeError: 'tuple' object has no attribute 'find' """


# 문장 중 문자열이 몇 번째인지 세는 함수
# .count() 메소드

text="hi my name is jy"
print(text.find("name")) # 6

# 문자열 수정

greeting="Hello, everyone~!"
""" greeting[0]="h" # TypeError: 'str' object does not support item assignment
print(greeting)  """

greeting=greeting.lower()
print(greeting) # hello, everyone~!

greeting='H'+greeting[1:]
print(greeting)

# 대문자로 전환, 소문자로 전환

greeting=greeting.upper()
print(greeting) # HELLO, EVERYONE~!

greeting=greeting.capitalize()
print(greeting) # Hello, everyone~!

greeting=greeting.title()
print(greeting) # Hello, Everyone~!


# replace(대체하다)

a=greeting.replace("Hello","방가루")
print(a) # 방가루, Everyone~!

# split
splited=a.split(" ")
print(splited) # ['방가루,', 'Everyone~!']
# sep로 분리한 후 리스트로 변환

