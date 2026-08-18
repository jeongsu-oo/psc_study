# 문제 1
def tem(x):
    if x >= 37.5:
        return "발열"
    elif 37.5 > x >= 36:
        return "정상"
    else:
        return "저체온"


temps = [36.5, 38.2, 35.1, 37.0, 39.1]

print("-" * 20, "\n문제 1 답변\n" + "-" * 20)
for i in temps:
    print(f"{i} -> {tem(i)}")


# 문제 2
def tax(x):
    return int(x * 1.1)


products = {"노트북": 1200000, "마우스": 25000, "키보드": 45000}

print("-" * 20, "\n문제 2 답변\n" + "-" * 20)
for i in products:
    print(f"{i} : {tax(products[i])}원")


# 문제 3
def cnt_string(x):
    cnt = 0
    for i in x:
        if i.isalpha():
            cnt += 1
    return cnt


sentences = ["안녕 하세요", "파 이 썬 좋 아", "hello world"]

print("-" * 20, "\n문제 3 답변\n" + "-" * 20)
for i in sentences:
    print(f"{i} -> {cnt_string(i)}")


# 문제 4
def tx(x):
    if x.replace(" ", "").isdigit():
        return int(x)
    else:
        return 0


raw = [" 100 ", "50", "", "삼십", "3.5"]

print("-" * 20, "\n문제 4 답변\n" + "-" * 20)
for i in raw:
    print(f"{i} -> {tx(i)}")


# 문제 5
def maxi(x):
    if x == []:
        return
    mx = x[0]
    for i in x:
        if mx < i:
            mx = i
    return mx


lst = [[3, 9, 1, 7], [-5, -2, -9], []]

print("-" * 20, "\n문제 5 답변\n" + "-" * 20)
for i in lst:
    print(f"{i} -> {maxi(i)}")


# 문제 6
def get_average(x):
    return round(sum(x) / len(x), 1)


def get_grade(x):
    for i in x:
        if i >= 90:
            return "A"
        elif i >= 80:
            return "B"
        elif i >= 70:
            return "C"
        else:
            return "D"


students = {
    "김철수": [90, 85, 100],
    "이영희": [70, 95, 70],
    "박민수": [80, 85, 90],
}

print("-" * 20, "\n문제 6 답변\n" + "-" * 20)
for i in students:
    print(f"{i} 평균 {get_average(students[i])}  등급 {get_grade(students[i])}")


# 문제 7
def get_overtime_pay(x):
    return x * 20000


def get_tax(x):
    return int(x * 0.1)


def get_final_pay(x, y):
    return (x + get_overtime_pay(y)) - get_tax(x + get_overtime_pay(y))


workers = [
    {"이름": "김철수", "기본급": 3000000, "초과시간": 5},
    {"이름": "이영희", "기본급": 3500000, "초과시간": 0},
]

print("-" * 20, "\n문제 7 답변\n" + "-" * 20)
for i in workers:
    print(
        f"{i['이름']} : 기본급 {i['기본급']}, 초과 {i['초과시간']}시간 -> 실수령 {get_final_pay(i['기본급'], i['초과시간'])}"
    )


# 문제 8
def is_long_enough(x):
    return len(x) >= 8


def has_number(x):
    for i in x:
        if i.isdigit():
            return True


def has_letter(x):
    for i in x:
        if i.isalpha():
            return True


def check_password(x):
    if is_long_enough(x) and has_number(x) and has_letter(x):
        return "안전"
    elif not is_long_enough(x):
        return "8자 이상이어야 합니다."
    elif not has_number(x):
        return "숫자를 포함해야 합니다."
    elif not has_letter(x):
        return "영문자를 포함해야 합니다."


passwords = ["abc12345", "abc123", "abcdefgh", "12345678"]


print("-" * 20, "\n문제 8 답변\n" + "-" * 20)
for i in passwords:
    print(f"{i} -> {check_password(i)}")


# 문제 9
def make_star(x):
    if x == 5:
        return "★★★★★"
    elif x == 4:
        return "★★★★☆"
    elif x == 3:
        return "★★★☆☆"
    elif x == 2:
        return "★★☆☆☆"
    elif x == 1:
        return "★☆☆☆☆"
    else:
        return "☆☆☆☆☆"


def show_review(x, y):
    print(f"{x}     {make_star(y)} ({y})")


reviews = {"노트북": 4, "마우스": 5, "키보드": 2}

print("-" * 20, "\n문제 9 답변\n" + "-" * 20)
for i in reviews:
    show_review(i, reviews[i])


# 문제 10
# stock = {}


# def add_stock(stk, nm, cnt):
#     if nm not in stock:
#         stock[nm] = int(cnt)
#     else:
#         stk = stock[nm]
#         stock[nm] += int(cnt)


# def remove_stock(stk, nm, cnt):
#     if int(cnt) > stock[nm]:
#         print(f"재고 부족 : {nm} (요청 {cnt}, 보유 {stock[nm]})")
#     else:
#         stk = stock[nm]
#         stock[nm] -= int(cnt)


# def show_stock(stk):
#     print("[재고 현황]")
#     for i in stk:
#         print(f"{i} : {stk[i]}개")


# print("-" * 20, "\n문제 10 답변\n" + "-" * 20)
# stock = add_stock(stock, "마우스", 10)
# stock = remove_stock(stock, "마우스", 3)
# show_stock(stock)
# while True:
#     stk = input("원하는 것을 입력하세요 (입고 / 출고 / 전체 출력 / 종료) : ")
#     if stk == "종료":
#         break
#     elif stk == "전체 출력":
#         show_stock(stock)
#         break
#     nm = input("상품명을 입력하세요. : ")
#     cnt = input("개수를 입력하세요 (숫자 입력) : ")
#     if stk == "입고":
#         add_stock(stk, nm, cnt)
#     elif stk == "출고":
#         remove_stock(stk, nm, cnt)
#     else:
#         print("오타 주의")


# 문제 10
stock = {}


def add_stock(stk, nm, cnt):
    stk = stock
    if nm not in stock:
        stk[nm] = cnt
        return stk
    else:
        stk[nm] += cnt
        return stk


def remove_stock(stk, nm, cnt):
    stk = stock
    if stk[nm] < cnt:
        print(f"재고 부족 : {nm} (요청{cnt}, 보유{stk[nm]})")
        return stk
    else:
        stk[nm] -= cnt
        return stk


def show_stock(stk):
    print("[재고 현황]")
    for i in stk:
        print(f"{i} : {stk[i]}개")


print("-" * 20, "\n문제 10 답변\n" + "-" * 20)
stock = add_stock(stock, "마우스", 10)
stock = add_stock(stock, "키보드", 5)
stock = remove_stock(stock, "마우스", 3)
stock = remove_stock(stock, "키보드", 10)
stock = add_stock(stock, "모니터", 2)
show_stock(stock)


# 문제 11
def reverse_text(x):
    x = x.replace(" ", "").lower()
    a = ""
    for i in range(len(x) - 1, -1, -1):
        a += x[i]
    return a


def is_palindrome(x):
    x = x.replace(" ", "").lower()
    if x == reverse_text(x):
        return "회문입니다."
    else:
        return "회문이 아닙니다."


words = ["level", "기러기", "python", "Never odd or even"]

print("-" * 20, "\n문제 11 답변\n" + "-" * 20)
for i in words:
    print(f"{i} -> {is_palindrome(i)}")


# 문제 12
def count_words(x):
    y = {}
    x = x.lower().split(" ")
    for i in x:
        if i not in y:
            y[i] = 1
        else:
            y[i] += 1
    return y


text = "Python is fun Python is easy Python"
dic = count_words(text)

rvs_dic = {}
for i, j in dic.items():
    rvs_dic[j] = i

print("-" * 20, "\n문제 12 답변\n" + "-" * 20)
print(dic)

print(f"가장 많이 나온 단어 : {rvs_dic.get(max(dic.values()))} ({max(dic.values())}회)")


# 문제 13
def withdraw(bal, amt):
    if bal < amt:
        print(f"잔액 부족 (요청 {amt}, 잔액 {bal})")
        return balance
    else:
        bal = bal - amt
        print(f"출금 {amt} -> 잔액 {bal}")
        return bal


def deposit(bal, amt):
    bal = bal + amt
    print(f"입금 {amt} -> 잔액 {bal}")
    return bal


balance = 10000
print("-" * 20, "\n문제 13 답변\n" + "-" * 20)
balance = withdraw(balance, 3000)
balance = deposit(balance, 5000)
balance = withdraw(balance, 20000)
print(f"최종 잔액 : {balance}")


# 문제 14
def add_item(cart, nm):
    cart = cart.copy()
    if nm not in cart:
        cart += [nm]
        return cart


def remove_item(cart, nm):
    cart = cart.copy()
    if nm not in cart:
        print(f"없는 상품입니다 : {nm}")
        return cart
    else:
        cart.remove(nm)
        return cart


print("-" * 20, "\n문제 14 답변\n" + "-" * 20)
cart1 = ["사과"]
cart2 = add_item(cart1, "우유")
print(cart2)
cart3 = add_item(cart2, "빵")
print(cart3)
remove_item(cart3, "라면")
cart4 = remove_item(cart3, "우유")
print(cart4)
print(cart1)


# 문제 15

og = [3, 1, 2]


def sort_bad(data):
    data.sort()
    return data


def sort_good(data):
    return sorted(data)


print("-" * 20, "\n문제 15 답변\n" + "-" * 20)
print(f"원본 : {og}")
print(f"sort_good 결과 : {sort_good(og)} / 원본 : {og}")
print(f"sort_bad 결과 : {sort_bad(og)} / 원본 : {og}")


# 문제 16
BASE_FEE = 3000  # (기본 배달료)
FREE_LIMIT = 20000  # (무료배달 기준액)
EXTRA_PER_KM = 500  # (1km당 추가요금)


def get_delivery_fee(x, y):
    if x >= FREE_LIMIT:
        return 0
    else:
        return BASE_FEE + (EXTRA_PER_KM * y)


orders = [[15000, 3], [25000, 5], [8000, 1]]

print("-" * 20, "\n문제 16 답변\n" + "-" * 20)
for i in orders:
    print(
        f"주문 : {i[0]}, {i[1]}km -> 배달료 {get_delivery_fee(i[0], i[1])}, 총 {i[0] + get_delivery_fee(i[0], i[1])}"
    )


# 문제 17
def visit(cnt):
    return cnt + 1


def reset():
    return 0


def show_count(cnt):
    return f"현재 방문자 : {cnt}명"


print("-" * 20, "\n문제 17 답변\n" + "-" * 20)
count = 0
count = visit(count)
count = visit(count)
count = visit(count)
count = show_count(count)
print(count)
count = reset()
count = show_count(count)
print(count)


# 문제 18
def get_best(x):
    bt = get_average(list(x.values())[0])
    for i in x:
        if get_average(x[i]) > bt:
            bt = get_average(x[i])
            st = i
        else:
            list(x.values())[0]
            st = list(x.keys())[0]
    return st


def print_report(x):
    tot = 0
    print("===== 성적표 =====")
    for i in x:
        print(f"{i}  {get_average(x[i])} ")
        tot += get_average(x[i])
    print("-" * 20)

    print(f"전체 평균 : {round(tot / len(x), 1)}")
    print(f"최고 득점 : {get_best(x)}")


class_scores = {
    "김철수": [90, 85, 100],
    "이영희": [70, 95, 70],
    "박민수": [80, 85, 90],
    "최지은": [55, 70, 63],
}

print("-" * 20, "\n문제 18 답변\n" + "-" * 20)
print_report(class_scores)


# 문제 19
def total_spent(x):
    tot = 0
    for i in records:
        tot += i["금액"]
    return tot


def spent_by_category(x):
    dic = {}
    for i in records:
        if i["분류"] not in dic:
            dic[i["분류"]] = i["금액"]
        else:
            dic[i["분류"]] += i["금액"]
    return dic


def biggest_category(x):
    dic = {}
    for i, j in spent_by_category(x).items():
        dic[j] = i
    return dic[max(spent_by_category(x).values())]


def over_budget(x, y):
    return y >= x, y - x


def make_bar(amt, unit):
    return "■" * (amt // unit)


records = [
    {"항목": "점심", "분류": "식비", "금액": 45000},
    {"항목": "지하철", "분류": "교통", "금액": 45000},
    {"항목": "저녁", "분류": "식비", "금액": 75000},
    {"항목": "옷", "분류": "쇼핑", "금액": 90000},
    {"항목": "영화", "분류": "문화", "금액": 30000},
]
BUDGET = 250000

tot = total_spent(records)
cat = spent_by_category(records)

print("-" * 20, "\n문제 19 답변\n" + "-" * 20)
print(f"총 지출 : {tot}")
print("[카테고리별]")
for i in cat:
    print(
        f"{i.ljust(7, ' ')}{str(cat[i]).ljust(10, ' ')}",
        make_bar(cat[i], 10000),
    )
print(f"가장 많이 쓴 곳 : {biggest_category(records)}")
if over_budget(tot, BUDGET)[0]:
    print(f"예산 {BUDGET}원 -> 남은 돈 {over_budget(tot, BUDGET)[1]}원")
else:
    print(f"예산 {BUDGET}원 -> {over_budget(tot, BUDGET)[1] * -1}원 초과!")


# 문제 20
tasks = {}


def add_task(x, y):
    if y not in x:
        x[y] = True


def done_task(x, y):
    if y in x:
        x[y] = False
    else:
        print(f"{y}은(는) 목록에 없습니다.")


def count_done(x):
    return list(x.values()).count(False)


def show_tasks(x):
    for i in x:
        if not x[i]:
            print(f"[v]     {i}")
        else:
            print(f"[ ]     {i}")
    print(f"완료 : {count_done(x)} / {len(tasks)}")


print("-" * 20, "\n문제 20 답변\n" + "-" * 20)
# print(count_done(tasks))
while True:
    q = int(input("to-do list를 작성해보아요 (1. 추가, 2. 완료, 3. 목록, 4. 종료) : "))
    if q == 1:
        add = input("추가할 할 일을 작성해주세요 : ")
        add_task(tasks, add)
    elif q == 2:
        done = input("완료한 일을 작성해주세요 : ")
        done_task(tasks, done)
    elif q == 3:
        show_tasks(tasks)
    elif q == 4:
        print("종료")
        break
    else:
        print("숫자 1,2,3,4를 입력하세요.")
