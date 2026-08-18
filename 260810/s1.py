#
# while문
#

# 조건이 True(참)인 동안 같은 코드를 계속 반복

# while문 3요소
# 1. 초기화 : 반복에 쓸 변수를 미리 만들어 둔다.
# 2. 조건식 : 언제까지 반복할지
# 3. 변화식 : 변수를 바꿔서 언젠가 조건을 거짓으로 만든다.
# 주의 : 3번 오류 시 무한 루프


#
# 1부터 10까지 더하기
#

total = 0
n = 1  # 변수 지정

while n <= 10:  # 반복 종료 시점 (조건문)
    total += n
    n += 1  # 반복 종료를 위한 식
print(total)


#
# 거꾸로 세기
#

cnt = 5

while cnt >= 1:
    print(cnt, "거꾸로")
    cnt -= 1


#
# break - 반복 즉시 종료
#

num = 1
while num <= 100:
    if num > 5:
        break
    print(num, "break")
    num += 1


#
# continue - 넘어가기
#

k = 0
while k < 10:
    k += 1
    if k % 2 == 0:
        continue
    print(k, "continue")

# 만약 k += 1을 print 아래에 두면?
# 짝수에서 continue >> k가 안 늘어남 >> 무한 루프

pw = "1234"
tries = 0
while True:
    tries += 1
    put = input("비밀번호를 입력하세요 : ")
    if put == pw:
        print(f"{tries}번째 시도 : 성공")
        break
    print(f"{tries}번째 시도 : 실패")

#
# while - else (python에만 있음)
#

x = 1
while x <= 3:
    print("반복 중 : ", x)
    x += 1
else:
    print("break 없이 정상 종료 >> else 실행")


#
# 누적 & 조건 조합 (2의 거듭제곱)
#

# 1000을 처음 넘는 2의 거듭제곱
value = 1
power = 0

while value <= 1000:
    value *= 2
    power += 1
print(f"2^{power} = {value}")


#
# for문과의 차이점
#
# for : 반복 횟수를 "이미 알고 있을 때"   >> list, range 등
# while : 반복 횟수를 "모를 때"         >> 조건이 만족될 떄까지

for i in range(1, 4):
    print("for:", i)

i = 1
while i < 4:
    print("while", i)
    i += 1
