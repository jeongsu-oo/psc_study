#
# 상속이란
#

# 이미 만들어둔 클래스를 물려 받아 새 클래스를 만드는 것이다.

# class 자식클래스(부모클래스):

# 부모의 속성과 매서드를 그대로 물려 받고
# 필요한 것만 추가하거나 바꾸면 된다.


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


class SavingAccount(Account):
    """저축 계좌, Account를 물려 받음"""

    def __init__(self, owner, balance, rate):
        # 부모의 __init__을 먼저 실행
        super().__init__(owner, balance)
        # 저축 계좌만의 속성
        self.rate = rate  # 이자율

    def add_interest(self):
        """이자를 더한다. (저축 계좌에만 있는 기능)"""
        interest = int(self.balance * self.rate)
        self.balance = self.balance + interest
        print(f"이자{interest:,}원이 추가되었습니다.")


sa = SavingAccount("김철수", 100000, 0.03)
sa.deposit(50000)
sa.add_interest()
sa.show()

"""
SavingAccount에는 deposit과 show를 넣지 않아도 사용 가능
Account에게 물려 받았기 때문

super().__init__(owner, balance)
ㄴ> super()는 '부모 클래스'를 뜻함
ㄴ> 부모의 __init__을 먼저 실행한 후,
ㄴ> owner, balance를 셋팅하고
ㄴ> 자기만의 rate를 추가
"""


#
# 매서드 덮어쓰기 (오버라이딩)
#

# 물려 받는 매서드를 그대로 쓰지 않고
# 자식 클래스에서 다시 정의하면 그게 우선

# overriding - 덮어쓰기


class CreditAccount(Account):
    """마이너스 통장, 한도까지 마이너스 출금 가능"""

    def __init__(self, owner, balance, limit):
        super().__init__(owner, balance)
        self.limit = limit

    def withdraw(self, amount):
        """부모의 withdraw를 덮어씁니다."""
        # 부모 코드 return super().withdraw(amount)
        # 잔액 + 한도까지 출금으로 변경
        if amount > self.balance + self.limit:
            print(f"한도 초과(최대 {self.balance + self.limit:,}원)")
        self.balance = self.balance - amount

    def show(self):
        """출력 형식도 변경합니다."""
        # return super().show()
        if self.balance < 0:
            print(f"{self.owner}님의 잔액 : {self.balance:,}원 (마이너스)")
        else:
            print(f"{self.owner}님의 잔액 : {self.balance:,}원")


ca = CreditAccount("이영희", 10000, 50000)

# ca.withdraw(30000)
# ca.show()

ca.withdraw(100000)
ca.show()

# 자식 클래스에 같은 일므의 매서드가 있으면 그게 우선


#
# 같은 이름, 다른 동작
#
# 여러 종류의 계좌를 같은 방식으로 다룰 수 있다
# 각자 알아서 자기 방식대로 동작

accounts = [
    Account("김철수", 50000),
    SavingAccount("이영희", 100000, 0.03),
    CreditAccount("박민수", 10000, 30000),
]

print("전체 계좌 현황")
for acc in accounts:
    acc.show()

print("\n[모두 20000원씩 출금 시도]")
for acc in accounts:
    acc.withdraw(20000)
    acc.show()

"""
같은 종류로 세 종류의 계좌를 다뤘다.

account.withdraw(20000)
일반 계좌는 잔액 확인
마이너스 통장은 한도 확인

다형성.
"""


# 파이썬은 거의 모든 것이 객체
# '안녕'.upper() >> 문자열 객체의 매서드
# [1,2,3].append(4) >> 리스트 객체의 매서드
# Path('data').mkdir() >> Path 객채의 매서드

# 점(.)을 찍고 함수를 쓴다면
# 그건 전부 객체의 매서드


# 이미 쓰고 있던 객체들
text = "hello world"
print("  문자열 객체:", type(text).__name__)
print("    text.upper()      =", text.upper())
print("    text.split()      =", text.split())
print("    text.replace()    =", text.replace("world", "python"))

nums = [3, 1, 2]
print("\n  리스트 객체:", type(nums).__name__)

nums.append(4)
print("    append 후         =", nums)

nums.sort()
print("    sort 후           =", nums)

info = {"name": "김철수"}
print("\n  딕셔너리 객체:", type(info).__name__)
print("    info.get('name')  =", info.get("name"))
print("    info.keys()       =", list(info.keys()))

"""
전부 '객체.메서드()' 형태입니다.
누군가 str 클래스, list 클래스를 만들어 뒀고
우리는 그걸 가져다 쓰고 있었던 겁니다.
"""

#
# 처음 보는 객체를 탐색하는 법
#
# pandas, numpy를 배울 때 이런 코드를 보게 된다.

# df = pd.read_csv('파일.csv')
# df.head()
# df.groupby('부서').mean()

# type(df)      무슨 클래스인지
# dir(df)       뭘 할 수 있는지 목록
# help(df.head) 특정 매서드 설명

sa = SavingAccount("최지은", 100000, 0.05)

print(type(sa).__name__)

methods = []
for i in dir(sa):
    if not i.startswith("_"):  # 밑줄 시작은 내부용
        methods.append(i)
print(methods)

print(SavingAccount.add_interest.__doc__)  # 함수 내 설명 불러오기

"""
pandas를 배울 때도 똑같이
type(df) << DataFrame (클래스)
dir(df) << head, groupby, sum ...
help(df.groupby) << groupby 사용법
"""


#
# 클래스를 안 만들어도 쓸 수는 있다
#

# pandas나 numpy를 쓸 때
# 클래스를 만들지 않고 쓰기만 함

# df = pd.read_csv('파일.csv') << 남이 만든 클래스로 객체 생성
# df.head() << 남이 만든 매서드 사용

# 클래스 직접 못 만들어도 pandas는 사용 가능

# 다만 오늘 배운 걸 알고 있으면
# - df가 점을 찍고 부르는지
# - 왜 df.sort_values()는 원본을 안 바꾸는지
# - 왜 어떤 건 ()를 붙이고 어떤 건 안 붙이는지
# 이런 것들이 이해 될 것


#
# 속성과 매서드 구분
#

sa = SavingAccount("정하늘", 50000, 0.05)

# 속성은 괄호 없음
print("속성 (괄호 없음)")
print(sa.owner)
print(sa.balance)
print(sa.rate)

# 매서드는 괄호를 붙임
print("\n매서드 (괄호 있음)")
sa.show()


#
# 객체지향과 캡슐화
#

# 객체지향이란?

# 지금까지 배운 방식에 이름이 있다.
# 객체지향 프로그래밍

# [프로그램을 나누는 두 가지 방식]

# [절차 지향]
# '무엇을 할 것인가'를 중심으로 나눈다.
# 기능(함수) 단위로 쪼갠다.

# deposit(account, amount)
# withdraw(account, amount)
# show(account)


# [객체지향]
# '무엇이 있는가'를 중심으로 나눈다.
# 대상(객체) 단위로 쪼갠다.

# 계좌가 있다. 잔액이 포함된다.
# 입금과 출금이 가능하다.
# 데이터는 기능이 한 덩어리다.


# 어느 것이 좋은가

# 단순한 계산, 짧은 스크립트 >> 함수로 충분
# 여러 대상이 각자 상태를 가짐 >> 객체지향이 편함


# 절차지향 '무엇을 할 것인가' >> 기능(함수) 단위로 나눔
# 객체지향 '무엇이 있는가' >> 대상(객체) 단위로 나눔

# [객체지향의 네 가지 특징]
# 캡슐화 | 데이터를 안전하게 감싸기
# 상속  | 기존 것을 물려 받기
# 다형성 | 같은 이름, 다른 동작
# 추상화 | 복잡한 걸 단순하게


#
# 캡슐화
#

# acc['balance'] = -9999
# withdraw 함수에 잔액 확인 로직을 넣어도 직접 넣으면 소용 없음

# 클래스로 만들어도 같은 문제

acc = Account("김철수", 10000)

# 매서드를 통하면 검증됨
print("\n검증")
acc.withdraw(50000)
print("매서드로 출금 시도 후 잔액 : ", acc.balance)

# 속성을 직접 건드리면 검증 건너 뜀
acc.balance = -99999
print(acc.balance)

"""
withdraw 안의 잔액 확인이 소용이 없다

이걸 막는 게 캡슐화
캡슐로 감싸듯 데이터를 안에 넣고,
정해진 통로(매서드)로만 접근하게 하는 것
"""

#
# 밑줄 하나
#
# 파이썬에는 속성을 완전히 숨기진 못함
# 그래서 관례로 막음

# self.balance  누구나 쓰는 값
# self._balance 건드리지 마라는 뜻


class SafeAccount1:
    """캡슐화 1단계 - 밑줄 하나"""

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def get_balance(self):
        """잔액을 읽는 통로"""
        return self._balance

    def deposit(self, amount):
        """입금하는 통로 (검증 포함)"""
        if amount <= 0:
            print("입금액은 0보다 커야 합니다.")
            return
        self._balance = self._balance + amount

    def withdraw(self, amount):
        """출금하는 통로 (검증 포함)"""
        if amount > self._balance:
            print("잔액 부족")
            return
        self._balance = self._balance - amount


print("\n검증")
sa1 = SafeAccount1("이영희", 10000)
sa1.deposit(5000)
print("입금 후 잔액 : ", sa1.get_balance())
sa1.deposit(-3000)
print("음수 입금 시도 후 : ", sa1.get_balance())
sa1.withdraw(50000)
print("초과 출금 시도 후 : ", sa1.get_balance())

"""
밑줄 하나는 약속
"""

#
# 밑줄 둘
#
# 밑줄 2개는 파이썬이 이름을 바꿔버림
# 밖에서 원래 이름으로는 접근 불가

# self.__balance
# 이름 맹글링


class SafeAccount2:
    """캡슐화 2단계 - 밑줄 둘"""

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        """잔액을 읽는 통로"""
        return self.__balance

    def deposit(self, amount):
        """입금하는 통로 (검증 포함)"""
        if amount <= 0:
            print("입금액은 0보다 커야 합니다.")
            return
        self.__balance = self.__balance + amount

    def withdraw(self, amount):
        """출금하는 통로 (검증 포함)"""
        if amount > self.__balance:
            print("잔액 부족")
            return
        self.__balance = self.__balance - amount


print("\n검증")
sa2 = SafeAccount2("박민수", 10000)
sa2.deposit(5000)
print("정상 입금 후 : ", sa2.get_balance())
try:
    print(sa2.__balance)
except AttributeError as e:
    print("직접 접근 시도 >> 에러 발생")
    print(">>>", e)

# 이래도 이젠 안 바뀜
sa2.__balance = -999  # 새 속성만 생김
print("강제 대입한 후 : ", sa2.get_balance())

"""
밑줄 두 개를 붙이면 파이썬이 이름을 바꿈
그래서 밖에서 __balance라고 불러도 못 찾음

다만 완전한 보안 장치는 아님
방법을 알면 우회 가능

실무에선 밑줄 하나를 더 많이 쓴다
밑줄 둘은 이름 충돌을 피해야 할 때 주로 씀
"""


#
# property - 매서드를 속성처럼
#
# get_balance()처럼 매서드를 부르는 게 번거로움
# @property를 쓰면 매서드를 속성처럼 사용 가능

# @로 시작하는 것을 데코레이터라고 함
# 함수 위에 붙여서 성질을 바꾸는 표시


class SafeAccount3:
    """캡슐화 3단계 - property"""

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # 저장용   # 밑줄 있음 (진짜 값을 담는다)

    @property
    def balance(self):
        """읽을 때 실행됩니다. (괄호 없이)"""
        return self._balance  # 읽기    # 밑줄 있음 (진짜 값을 꺼냄)

    @balance.setter
    def balance(self, value):
        """쓸 때 실행됩니다. 여기서 검증할 수 있습니다."""
        if value < 0:
            print("잔액은 음수가 될 수 없습니다.")
            return
        self._balance = value

    def deposit(self, amount):
        self.balance = (
            self.balance + amount
        )  # setter를 거침   # 밑줄 없음 (통로를 지나감)

    def withdraw(self, amount):
        self.balance = self.balance - amount  # setter가 음수를 막아줌


sa3 = SafeAccount3("최지은", 10000)
print("잔액 읽기 (괄호 없이) : ", sa3.balance)
sa3.deposit(5000)
print("입금 후 : ", sa3.balance)
sa3.withdraw(50000)  # setter가 막아줌
print("초과 출금 시도 후 : ", sa3.balance)

sa3.balance = -100  # 직접 대입해도 막힘
print("음수 직접 대입 후 : ", sa3.balance)


#
# 추상화 - 복잡한 걸 단순하게
#
# 추상화는 '안이 어떻게 돌아가는지 몰라도 쓸 수 있게 하는 것'
# ex) 자동차 : 엔진 몰라도 운전 가능

# 우리가 만든 클래스도 마찬가지
# acc.deposit(5000)을 쓰는 사람은
# 안에 어떤 검증을 하는지 몰라도 됨

# 좋은 클래스는 밖에서 봤을 떄 단순
# 복잡한 건 안에 숨기고, 필요한 것만


class Coffee:
    """커피 머신, 쓰는 사람은 make()만 알면 됩니다."""

    def __init__(self):
        self._water = 1000  # 물(ml)
        self._beans = 200  # 원두(g)

    def _heat_water(self):
        """내부 동작 1 - 물 끓이기"""
        return "물을 90도로 데움"

    def _grind_beans(self):
        """내부 동작 2 - 원두 갈기"""
        return "원두를 곱게 갈음"

    def _extract(self):
        """내부 동작 3 - 추출"""
        return "9기압으로 추출"

    def make(self):
        """커피를 만듭니다."""
        steps = [self._heat_water(), self._grind_beans(), self._extract()]
        self._water = self._water - 150
        self._beans = self._beans - 18
        return steps


machine = Coffee()

print("사용자 입장")
print(machine.make())
for i in machine.make():
    print("   -", i)

"""
make()를 쓰는 사람은 _heat_water나 _extract를 몰라도 된다.
밖으로 보여줄 것과 숨길 것을 나눈다.
추상화
"""

"""
객체지향 4가지 특징

[캡슐화]
데이터를 안에 감추고 정해진 통로로만 접근
_balance, __balance, @property
>> 아무나 값을 망가뜨리지 못하게 막는다.

[상속]
기존 클래스의 기능을 물려 받아 새 클래스를 만듦
class SavingAccount(Account)
>> 중복을 없애고 확장하기 쉽게 만듦

[다형성]
같은 이름의 매서드가 클래스마다 다르게 동작
account.withdraw()가 계좌 종류마다 다름
>> 여러 종류를 같은 코드로 다룰 수 있다.

[추상화]
복잡한 내부를 숨기고 필요한 것만 보여줌
machine.make() 한 줄이면 커피가 나온다.
>> 쓰는 사람이 편해진다.

용어를 암기하려 하지 마라.
어떤 문제를 해결하는지 기억하면 됨
코드를 짜다 보면 자연스럽게 쓰면 됨
"""
