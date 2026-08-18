#
# 조건 자리에 값을 그대로 넣기
#

# 파이썬은 True / False가 아닌 값도 참 거짓으로 판단합니다.
# 거짓 취급 : 0, 0.0, "", None, [], {}
# 그 외 전부 참

name = ""
if name:
    print(f"{name}님 안녕하세요.")
else:
    print("이름이 입력되지 않았습니다.")

count = 0
if count:
    print("항목이 있음")
else:
    print("항목이 없음")


#
# 중첩 조건문
#

age = 25
has_ticket = False

if age >= 20:
    print("나이 확인 완료")
    if has_ticket:
        print("입장하세요")
    else:
        print("티켓 구매 필요")
else:
    print("성인만 입장 가능")


#
# pass - 아무것도 안 하기
#

# 파이썬은 if 아래 비어 있으면 에러
# 나중에 채울 자리 표시로 pass를 사용할 수 있다


#
# 한 줄로 쓰는 조건문 (조건부 표현식)
#

# 기본 형태
age = 25

if age >= 20:
    status = "성인"
else:
    status = "미자"

# 한 줄 코드
status = "성인" if age >= 20 else "미자"

print(f"{'짝수' if 10 % 2 == 0 else '홀수'}")
