# 문제 1


def divide(n1, n2):
    try:
        return round(int(n1) / int(n2), 2)
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."
    except ValueError:
        return "숫자를 입력하세요."


print("-" * 20, "\n문제 1 답변\n" + "-" * 20)
# for i in range(3):
#     num1 = input("숫자1 : ")
#     num2 = input("숫자2 : ")
#     print("결과", divide(num1, num2))


# 문제 2
def mk_int(x):
    try:
        return int(str(x).strip())
    except ValueError as ee:
        return f"{x}은(는) 숫자가 아닙니다."


print("-" * 20, "\n문제 2 답변\n" + "-" * 20)
cnt = 0
lst = []
# for i in range(5):
#     data = input("값 : ")
#     if str(mk_int(data)).isdigit():
#         cnt += 1
#         lst += [mk_int(data)]
#     else:
#         print(mk_int(data))
# print(f"유효한 값 : {cnt}개")
# print(f"합계 : {sum(lst)}개")


# 문제 3
def is_adult(x):
    try:
        x = int(x)
        if x < 0:
            return "나이는 0보다 작을 수 없습니다."
        if x >= 19:
            return "성인입니다."
        return "미성년자입니다."
    except ValueError:
        return "숫자를 입력하세요."


print("-" * 20, "\n문제 3 답변\n" + "-" * 20)
# for i in range(3):
#     age = input("나이 : ")
#     print(is_adult(age))


# 문제 4
data = [10, 20, 30, 40, 50]


def idxing(x, y):
    try:
        y = int(y)
        if y > 5:
            return "그 번호는 없습니다."
        return x[y]
    except ValueError:
        return "숫자를 입력하세요."


print("-" * 20, "\n문제 4 답변\n" + "-" * 20)
# cnt = 0
# for i in range(3):
#     idx = input("번호(0~4) : ")
#     if str(idxing(data, idx)).isdigit():
#         cnt += 1
#     print(idxing(data, idx))
# print("성공 : ", cnt, "번")


# 문제 5 (피드백 전)
# def ft_price(x):
#     if x not in list(price.keys()):
#         return "그런 과일은 없습니다."
#     return f"{x} : {price[x]}원"


# price = {"사과": 1000, "바나나": 1500, "포도": 3000}

# print("-" * 20, "\n문제 5 답변\n" + "-" * 20)

# tot = 0
# for i in range(3):
#     fruit = input("과일 이름 : ")
#     print(ft_price(fruit))
#     if "원" in ft_price(fruit):
#         tot += price[fruit]
# print(f"총 가격 : {tot}원")

### 매개변수를 안 받는 함수
### for문도 함수에 넣어봐


# 문제 5 (피드백 후)
def ft_price():
    tot = 0
    for i in range(3):
        try:
            ft = input("과일 이름 : ")
            print(f"{ft} : {price[ft]}원")
        except KeyError:
            print("그런 과일은 없습니다.")
        else:
            tot += price[ft]
    print(f"총 가격 : {tot}원")


price = {"사과": 1000, "바나나": 1500, "포도": 3000}

print("-" * 20, "\n문제 5 답변\n" + "-" * 20)
# ft_price()


# 문제 6
def find_n():
    n = []
    while True:
        try:
            num = input("숫자(1~10) : ")
            if int(num) <= 10:
                n.append(int(num))
            if int(num) > 10:
                print("1~10 사이만 가능합니다.")
            if len(n) == 3:
                print(f"입력한 숫자 : {n}")
                print(f"합계 : {sum(n)}")
                break
        except ValueError:
            print("숫자를 입력하세요.")


print("-" * 20, "\n문제 6 답변\n" + "-" * 20)
# find_n()


# 문제 7
def mk_tier():
    for i in range(3):
        score = input("점수 : ")
        try:
            score = int(score)
            if 0 <= score <= 100:
                if score >= 90:
                    print("학점 : A")
                elif score >= 80:
                    print("학점 : B")
                elif score >= 70:
                    print("학점 : C")
                else:
                    print("학점 : F")
            else:
                raise Exception("0~100 사이만 가능합니다")
        except ValueError:
            print("숫자를 입력하세요.")
        except Exception as e:
            print(e)


print("-" * 20, "\n문제 7 답변\n" + "-" * 20)
# mk_tier()


# 문제 8
oper = ["+", "-", "*", "/"]


def calcul():
    for i in range(3):
        n1 = input("숫자1 : ")
        op = input("연산자(+ - * /) : ")
        n2 = input("숫자2 : ")
        try:
            n1 = str(int(n1))
            n2 = str(int(n2))
            if op not in oper:
                raise Exception("모르는 연산자입니다.")
            exp = n1, op, n2
            exp = " ".join(list(exp))
            print("결과 : ", eval(exp))
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다.")
        except ValueError:
            print("숫자를 입력하세요.")
        except Exception as e:
            print(e)


print("-" * 20, "\n문제 8 답변\n" + "-" * 20)
# calcul()


# 문제 9
def clean():
    dic = {}
    for i in range(3):
        words = input("이름,점수 : ")
        try:
            words = words.strip().split(",")
            if len(words) != 2:
                raise Exception("이름,점수 형태로 입력하세요.")
            dic[words[0]] = int(words[1])
        except ValueError:
            print("점수는 숫자여야 합니다.")
        except Exception as e:
            print(e)
    for i in dic:
        print(f"{i} : {dic[i]}점")


print("-" * 20, "\n문제 9 답변\n" + "-" * 20)
# clean()


# 문제 10
def rep():
    nm = input("이름 : ")
    while True:
        if not nm or nm.isspace():
            print("이름을 입력하세요.")
            nm = input("이름 : ")
        else:
            nm = nm
            break
    sc = input("점수 : ")
    while True:
        if not sc.isdigit():
            print("숫자를 입력하세요.")
            sc = input("점수 : ")
        elif 0 > int(sc) or int(sc) > 100:
            print("0~100 사이만 가능합니다.")
            sc = input("점수 : ")
        else:
            sc = sc
            break
    return [nm, sc]


def manage():
    dic = {}
    for i in range(3):
        lst = rep()
        dic[lst[0]] = lst[1]
    avg = 0
    for i in dic:
        print(f"{i} : {dic[i]}점")
        avg += int(dic[i])
    avg = round(avg / len(dic), 2)
    print(f"평균 : {avg}")
    dic2 = {}
    for i, j in dic.items():
        dic2[j] = i
    st = dic2[max(dic.values())]
    print(f"1등 : {st}")


print("-" * 20, "\n문제 10 답변\n" + "-" * 20)
manage()
