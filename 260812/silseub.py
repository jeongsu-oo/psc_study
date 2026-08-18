# 문제 1
def divide(num1, num2):
    try:
        suc.append(f"{num1} / {num2} = {round(int(num1) / int(num2), 2)}")
        return f"{num1} / {num2} = {round(int(num1) / int(num2), 2)}"
    except ZeroDivisionError:
        return "실패 - 0으로 나눌 순 없어요"
    except TypeError:
        return "실패 - 숫자를 입력하세요"


def suc_per(x, y):
    return round(x / y * 100, 1)


tot = 0
cnt = 0
suc = []
print("-" * 20, "\n문제 1 답변\n" + "-" * 20)
while True:
    n1 = input("숫자1 (종료 : q) : ")
    if n1 == "q":
        print("[성공 기록]")
        for i in suc:
            print(i)
        print(f"성공률 : {suc_per(cnt, tot)}%")
        break
    else:
        n2 = input("숫자2 : ")
        result = divide(n1, n2)
        print(result)
        if "실패" in result:
            tot += 1
        else:
            cnt += 1
            tot += 1


# 문제 2
def make_int(x):
    lst = []
    ign = []
    over = []
    for i in x:
        try:
            i = int(str(i).strip())
            if 0 > i or i > 1000:
                raise Exception("범위 초과")
            lst.append(i)
        except ValueError:
            ign.append(i)
        except Exception as e:
            over.append(str(i))
    print(f"무시된 값 : {', '.join(ign)}")
    print(f"범위초과 값 : {', '.join(over)}")
    return lst


def smmm(list):
    for i in list:
        mx = list[0]
        mn = list[0]
        if mx < i:
            mx = i
        if mn > i:
            mn = i
    return sum(list), round(sum(list) / len(list), 2), mx, mn


print("-" * 20, "\n문제 2 답변\n" + "-" * 20)
data = input("값 입력(공백 구분) : ").split(" ")
result = smmm(make_int(data))
print(f"합계 : {result[0]}")
print(f"평균 : {result[1]:.2f}")
print(f"최대 : {result[2]} / 최소 : {result[3]}")


# 문제 3
def scores():
    lst = []
    for i in range(3):
        dic = {}
        nm = input("이름 : ")
        while True:
            if not nm or nm.isspace():
                print("이름을 입력하세요.")
                nm = input("이름 : ")
            else:
                nm = nm
                break

        kr = input("국어 : ")
        cnt = 0
        while cnt < 4:
            try:
                cnt += 1
                kr = int(str(kr).strip())
            except ValueError:
                print(f"숫자만 입력하세요 (남은 기회 {3 - cnt}회)")
                kr = input("국어 : ")
            else:
                if cnt < 3:
                    if kr < 0 or kr > 100:
                        print(f"0~100 사이만 가능합니다 (남은 기회 {3 - cnt}회)")
                        kr = input("국어 : ")
                elif cnt == 3 and (not str(kr).isdigit() or (kr < 0 or kr > 100)):
                    print("3회 모두 실패, 0점 처리합니다.")
                else:
                    break

        en = input("영어 : ")
        cnt = 0
        while cnt < 4:
            try:
                cnt += 1
                en = int(str(en).strip())
            except ValueError:
                print(f"숫자만 입력하세요 (남은 기회 {3 - cnt}회)")
                en = input("영어 : ")
            else:
                if cnt < 3:
                    if en < 0 or en > 100:
                        print(f"0~100 사이만 가능합니다 (남은 기회 {3 - cnt}회)")
                        en = input("영어 : ")
                elif cnt == 3 and (not str(en).isdigit() or (en < 0 or en > 100)):
                    print("3회 모두 실패, 0점 처리합니다.")
                else:
                    break

        mt = input("수학 : ")
        cnt = 0
        while cnt < 4:
            try:
                cnt += 1
                mt = int(str(mt).strip())
            except ValueError:
                print(f"숫자만 입력하세요 (남은 기회 {3 - cnt}회)")
                mt = input("수학 : ")
            else:
                if cnt < 3:
                    if mt < 0 or mt > 100:
                        print(f"0~100 사이만 가능합니다 (남은 기회 {3 - cnt}회)")
                        mt = input("국어 : ")
                elif cnt == 3 and (not str(mt).isdigit() or (mt < 0 or mt > 100)):
                    print("3회 모두 실패, 0점 처리합니다.")
                else:
                    break
        dic["name"] = nm
        dic["korean"] = kr
        dic["english"] = en
        dic["math"] = mt
        lst.append(dic)
    return lst


def mk_tier(mean):
    if mean >= 90:
        return "A"
    if mean >= 80:
        return "B"
    if mean >= 70:
        return "C"
    if mean >= 60:
        return "D"
    else:
        return "F"


print("-" * 20, "\n문제 3 답변\n" + "-" * 20)

scs = scores()
dic_avg = {}
for i in scs:
    avg = round((i["korean"] + i["english"] + i["math"]) / 3, 2)
    dic_avg[i["name"]] = avg

avg_kr = 0
avg_en = 0
avg_mt = 0
for i in scs:
    avg_kr += i["korean"]
    avg_en += i["english"]
    avg_mt += i["math"]
avg_kr = round(avg_kr / 3, 2)
avg_en = round(avg_en / 3, 2)
avg_mt = round(avg_mt / 3, 2)


def report(lst):
    print("이름".ljust(5, " "), "평균".ljust(5, " "), "학점".ljust(5, " "))
    print(
        f"{lst[0]['name'].ljust(7, ' ')}{str(dic_avg[lst[0]['name']]).ljust(6, ' ')}{mk_tier(dic_avg[lst[0]['name']]).rjust(5, ' ')}"
    )
    print(
        f"{lst[1]['name'].ljust(7, ' ')}{str(dic_avg[lst[1]['name']]).ljust(6, ' ')}{mk_tier(dic_avg[lst[1]['name']]).rjust(5, ' ')}"
    )
    print(
        f"{lst[2]['name'].ljust(7, ' ')}{str(dic_avg[lst[2]['name']]).ljust(6, ' ')}{mk_tier(dic_avg[lst[2]['name']]).rjust(5, ' ')}"
    )
    print(f"[과목별 평균] 국어 : {avg_kr} / 영어 : {avg_en} / 수학 : {avg_mt}")


report(scs)


# 문제 4
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("-" * 20, "\n문제 4 답변\n" + "-" * 20)

# 문제 5

print("-" * 20, "\n문제 5 답변\n" + "-" * 20)

# 문제 6

print("-" * 20, "\n문제 6 답변\n" + "-" * 20)

# 문제 7

print("-" * 20, "\n문제 7 답변\n" + "-" * 20)

# 문제 8

print("-" * 20, "\n문제 8 답변\n" + "-" * 20)

# 문제 9

print("-" * 20, "\n문제 9 답변\n" + "-" * 20)

# 문제 10

print("-" * 20, "\n문제 10 답변\n" + "-" * 20)
