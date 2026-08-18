#
# 연산자
#

# 활용
print(130 // 60, 130 % 60)  # 2 10   130초 = 2분 10초


#
# 논리 연산자
#

# 여러 조건을 묶을 때 사용

# and, or , not


#
# 짧은 회로 평가
#

# and는 앞이 False면 뒤를 안 본다
# or는 앞이 True면 뒤를 안 본다
# 그래서 이런 순서가 안전하다
value = ""
print(value != "" and int(value) > 0)  # False (앞에서 걸러서 에러 안 남)

#
# 멤버십 연산자 (in / not in)
#

#
# 식별 연산자 (is / is not)
#

# 주 용도는 None 확인
result = None
print(result is None)  # True 권장되는 방식
print(result is not None)  # False
print(result == None)  # True (동작은 하지만 is가 관례)

a = [1, 2]
b = [1, 2]
print(a is b)  # False 서로 다른 리스트 두 개

# 정리 : 값 비교는 ==, None 확인은 is


#
# 연산자 우선순위
#
# 위에 있는 것이 우선
# 1. () 괄호
# 2. ** 거듭제곱
# 3. 곱하기 나누기 계열
# 4. + -
# 5. 비교 계열 (부등호, !=, ==, in, is)
# 6. not
# 7. and
# 8. or

# 비교보다 논리가 우선
