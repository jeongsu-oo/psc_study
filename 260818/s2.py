#
# 클래스(class) - 데이터와 기능 묶기
#
# 데이터가 함수를 따라 다닌다
#
def make_account(owner, balance):
    """계좌를 딕셔너리로 만듭니다."""
    return {"owner": owner, "balance": balance}


def deposit(account, amount):
    """입금하고 바뀐 계좌를 돌려줍니다."""
    account["balance"] = account["balance"] + amount
    return account


def withdraw(account, amount):
    """출금하고 바뀐 계좌를 돌려줍니다."""
    if amount > account["balance"]:
        print("잔액 부족")
        return account
    account["balance"] = account["balance"] - amount
    return account


def show(account):
    """계좌 정보를 출력합니다."""
    print(f"{account['owner']}님의 잔액 : {account['balance']:,}원")


acc = make_account("김철수", 10000)
acc = deposit(acc, 5000)
acc = withdraw(acc, 3000)
show(acc)

# 데이터(account)와 기능(함수)이 항상 붙어 다니는데
# 따로 떨어져 있어서 매번 같이 넣어야 한다.

acc2 = make_account("이영희", 10000)
show(acc2)
acc2["balance"] = -99999  # 함수 없이 직접 변경
show(acc2)

# withdraw 함수에 잔액 확인 로직을 넣어도
# 딕셔너리를 직접 건드리면 소용이 없다.


#
# 해결책 - 데이터와 기능을 한 덩어리로
#

# 클래스는 이 문제를 이렇게 해결
# "계좌"라는 게 뭔지 설계도를 만들어 둔다
# 거기에 데이터(주인, 잔액)와 기능(입금, 출굼)을 같이 넣자
# 그러면 함수를 부를 때 계좌를 매번 넘길 필요가 없다
# 함수가 이미 자기 계좌를 알고 있다


class Account:
    """은행 계좌"""

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액 부족")
            return
        self.balance = self.balance - amount

    def show(self):
        print(f"{self.owner}님의 잔액 : {self.balance:,}원")


# 써보기
my_acc = Account("김철수", 10000)
my_acc.deposit(5000)
my_acc.withdraw(3000)
my_acc.show()


# 모든 걸 클래스로 만들 필요는 없다.
# 아래 조건에 해당하면 클래스를 고려하라.

# 1) 데이터와 기능이 항상 붙어 다닌다.
#    계좌 + 입출금, 학생 + 성적계산, 장바구니 + 담기/빼기

# 2) 같은 종류를 여러 개 만들어야 한다.
#    계좌 100개, 학생 30명

# 3) 값이 계속 변한다. (상태를 가진다.)
#    잔액이 늘었다 줄었다, 재고가 들어왔다 나갔다

# 반대로 이럴 땐 함수로 충분합니다.
# - 값을 넣으면 결과만 나오는 단순 계산
#   예) 평균 구하기, 부가세 계산, 문자열 뒤집기
# - 한 번 쓰고 마는 작업

# 지금까지 만든 my_tools.py 함수
# to_int, get_average, make_bar
# 이건 클래스로 만들 이유가 없다. 값을 넣으면 결과만 나오니까


#
# 기본 문법
#

# 클래스는 설계도, 객체는 실제 물건

# 가장 흔한 비유
# 클래스 >> 붕어빵 틀 (하나만 있으면 됨)
# 객체 >> 붕어빵 (여러 개 가능)

# [용어 정리]
# 클래스(class) - 설계도
# 객체(object) - 설계도로 만든 실제 물건
# 인스턴스(instance) - 객체와 거의 같은 말
#                   "Account 클래스의 인스턴스"처럼 사용
# 속성(attribute) - 객체가 가진 데이터 (owner, balance)
# 매서드(method) - 객체가 가진 기능 (deposit, withdraw)

# 매서드는 그냥 '클래스 안에 있는 함수'
# 이름만 다를 뿐 함수와 같음

a = Account("김철수", 10000)
b = Account("이영희", 50000)
c = Account("박민수", 30000)
a.show()
b.show()
c.show()


#
# __init__
#
# __init__은 객체를 만들 때 자동으로 실행되는 함수

# Account('김철수',10000)

# __init__이 하는 일
# 객체가 처음 만들어 질 때 필요한 값을 채워 넣는다.


class Student:
    def __init__(self, name):
        print(f"__init__ 실행 됨. {name}학생을 만듭니다.")
        self.name = name
        self.score = []  # 빈 리스트로 시작


s1 = Student("김철수")
print(s1.name)


#
# self
#

# 클래스를 배울 떄 가장 헷갈리는 부분
# self는 '이 객체 자기 자신'을 가리킴

# [필요성]
# 계좌 100개
# deposit 매서드를 부를 때 '어느 계좌에 입금할 지' 알아야 함
# a.deposit(5000) >> a에 입금

# 점 앞에 있는 게 바로 self
# a.deposit(5000)을 부르면 self 자리에 a가 들어감

# [중요 : self는 우리를 넘기지 않는다]
# def deposit(self, amount) << 정의할 때 self를 쓴다
# a.deposit(5000) << 부를 때 안 씀

# self..balance와 balance의 차이
# self.balance - 이 객체의 잔액 (객체가 계속 기억함)
# balance - 그냥 지역변수 (매서드가 끝나면 사라짐)


class Person:
    def __init__(self, name):
        self.name = name

    def who_am_i(self):
        print(f"self는 지금 {self.name}입니다.")

    def compare(self, other):
        """self와 다른 객체를 비교합니다."""
        print(f"나는 {self.name}, 상대는 {other.name}")


p1 = Person("김철수")
p2 = Person("이영희")

p1.who_am_i()
p2.who_am_i()

p1.compare(p2)


#
# self를 빼먹으면 생기는 일
#
# 실수 1) 매서드 정의할 때 self를 빼먹음
# 실수 2) 속성 앞에 self를 안 붙임


class Wrong:
    def __init__(self, value):
        value = value


class Right:
    def __init__(self, value):
        self.value = value


w = Wrong(100)
r = Right(100)

try:
    print(w.value)
except AttributeError as e:
    print(e)

print(r.value)


#
# 매서드는 클래스 안의 함수
#

# - 인자를 받을 수 있고
# - return으로 값을 돌려줄 수 있고
# - 기본값도 쓸 수 있다
# 다른 점은 첫번째 인자가 self라는 것


class ScoreBook:
    """학생 한 명의 성적을 관리합니다."""

    def __init__(self, name):
        self.name = name
        self.scores = []

    def add(self, score):
        """점수를 추가합니다."""
        self.scores.append(score)

    def avg(self):
        """평균을 계산하고 돌려줍니다."""
        if not self.scores:
            return 0
        return round(sum(self.scores) / len(self.scores), 1)

    def grade(self):
        """등급을 돌려줍니다."""
        avg = self.avg()
        if avg >= 90:
            return "A"
        if avg >= 80:
            return "B"
        if avg >= 70:
            return "C"
        return "D"

    def report(self, show_scores=True):
        """성적표를 출력합니다. (기본값 인자 사용)"""
        print(f"{self.name} 평균 : {self.avg()} / 등급: {self.grade()}")
        if show_scores:
            print(f"점수 : {self.scores}")


book = ScoreBook("김철수")
book.add(90)
book.add(85)
book.add(100)
book.report()

book2 = ScoreBook("이영희")
book2.add(70)
book2.add(75)
book2.report(show_scores=False)


#
# 속성은 바뀐다
#
# 객체가 가진 값(속성)은 계속 바뀐다.
# 이걸 '상태를 가진다'고 표현

# 함수는 부르고 나면 아무것도 남지 않는다.
# 객체는 값을 계속 기억한다.
# 이게 가장 큰 차이


class Counter:
    """숫자를 세는 도구"""

    def __init__(self):
        self.count = 0

    def up(self):
        self.count = self.count + 1

    def down(self):
        self.count = self.count - 1

    def reset(self):
        self.count = 0


c1 = Counter()
c2 = Counter()

c1.up()
c1.up()
c1.up()
c2.up()

print(c1.count)
print(c2.count)

c1.reset()
print(c1.count)


#
# 속성에 직접 접근
#
# 객체의 속성은 점으로 읽고 쓸 수 있다.

# 읽기 : print(acc.balance)
# 쓰기 : acc.balance = 5000

# 쓰기 할 떄 주의 : 매서드를 거치지 않으면 검증 로직을 건너 뜀
acc = Account("최지은", 10000)
print("읽기", acc.owner, "/", acc.balance)

# 매서드 통한 출금 (검증 됨)
acc.withdraw(50000)

# 직접 수정 (검증 안 됨)
acc.balance = -99999
print("직접", acc.balance)

"""
파이썬은 속성을 완전히 숨기는 기능은 없다.
대신 관례가 있다.
self.balance 누구나 써도 되는 값
self._balance '내부용이니 건드리지 마라' 표시
약속
"""
