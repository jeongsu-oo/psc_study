# 문제 1
age = input("1번 문제. 나이를 입력하시오 :")

if int(age) >= 20:
    print("성인")
else:
    print("미성년자")

# 문제 2
num = input("2번 문제. 숫자를 입력하시오 :")

if int(num) % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 문제 3
score = input("3번 문제. 점수를 입력하시오 (100점 만점) : ")
score = int(score)

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# 문제 4
id = input("4번 문제. 아이디를 입력하시오. :")
pw = input("4번 문제. 비밀번호를 입력하시오. :")

if id == "admin" and pw == "1234":
    print("로그인 성공")
elif id == "admin" and pw != "1234":
    print("비밀번호가 틀렸습니다.")
elif id != "admin":
    print("존재하지 않는 아이디입니다.")

# 문제 5
n1 = input("5번 문제. 세 개의 숫자 중 하나를 입력하세요. (첫번째) :")
n2 = input("5번 문제. 세 개의 숫자 중 하나를 입력하세요. (두번째) :")
n3 = input("5번 문제. 세 개의 숫자 중 하나를 입력하세요. (세번째) :")

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 > n2 and n1 > n3:
    print(f"가장 큰 수는 첫번째 작성한 숫자 {n1}입니다")
elif n2 > n1 and n2 > n3:
    print(f"가장 큰 수는 두번째 작성한 숫자 {n2}입니다")
elif n3 > n1 and n3 > n2:
    print(f"가장 큰 수는 세번째 작성한 숫자 {n3}입니다")

# 문제 6
yr = input("6번 문제. 연도를 입력하시오. : ")
yr = int(yr)

if yr % 100 == 0:
    print("평년입니다.")
elif yr % 4 == 0 or yr % 400 == 0:
    print("윤년입니다.")
else:
    print("평년입니다.")
