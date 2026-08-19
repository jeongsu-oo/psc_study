class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.treat = 0

    def bark(self):
        print(f"멍멍! 나는 {self.name}(이)야.")

    def eat(self, count):
        self.treat = self.treat + count
        print(f"{self.name}(이)가 간식 {count}개를 먹었다. (총 {self.treat}개)")

    def birthday(self):
        self.age = self.age + 1
        print(f"{self.name}의 생일! 이제 {self.age}살")

    def is_puppy(self):
        # if self.age <= 2:
        #     return True
        # return False
        return self.age <= 2

    def show(self):
        if self.is_puppy():
            print(f"{self.name} ({self.age}살, 강아지)  간식 {self.treat}개")
        print(f"{self.name} ({self.age}살, 성견)  간식 {self.treat}개")


print("\n1번 출력")
d1 = Dog("초코", 3)
d1.show()
d1.bark()
d1.eat(2)
d1.eat(3)
d1.birthday()
d1.show()

print()

d2 = Dog("콩이", 1)
d2.show()
print("콩이는 강아지인가?", d2.is_puppy())


class Report:
    def __init__(self, name):
        self.name = name
        self.score = {}

    def add(self, subject, score):
        if 0 <= score <= 100:
            self.score[subject] = score
            print(f"{subject} {score}점 등록")
            return
        print(f"잘못된 점수 : {score}")

    def average(self):
        if self.score:
            return round(sum(self.score.values()) / len(self.score), 1)
        return 0

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        if avg >= 80:
            return "B"
        if avg >= 70:
            return "C"
        return "D"

    def best(self):
        if self.score:
            bt_sc = max(self.score.values())
            for i, j in self.score.items():
                if j == bt_sc:
                    return i, j
        return

    def show(self):
        print(f"[{self.name} 성적표]")
        for i, j in self.score.items():
            print(f"    {i} {j}점")
        print(f"평균 {self.average()} ({self.grade()})")
        if self.best() is not None:
            print(f"최고 과목 : {self.best()[0]} {self.best()[1]}점")
        else:
            print("최고 과목 : 없음")


print("\n2번 출력")
r = Report("김철수")
r.add("국어", 90)
r.add("영어", 85)
r.add("과학", 150)
r.add("수학", 100)
r.show()

print()

r2 = Report("이영희")
r2.show()


class VendingMachine:
    def __init__(self):
        self.money = 0
        self.stock = {
            "콜라": {"가격": 1500, "재고": 3},
            "사이다": {"가격": 1300, "재고": 2},
            "물": {"가격": 1800, "재고": 5},
        }

    def insert(self, money):
        """돈을 넣습니다."""
        self.money = self.money + money
        print(f"{money:,}원 투입 (총 {self.money:,}원)")

    def buy(self, name):
        """음료를 삽니다."""
        if name not in self.stock:
            print(f"그런 음료는 없습니다. >> {name}")
            return
        if self.stock[name]["재고"] == 0:
            print(f"품절입니다. >> {name}")
            return
        if self.money <= self.stock[name]["가격"]:
            print(
                f"금액이 부족합니다. (부족액 {self.stock[name]['가격'] - self.money}원)"
            )
            return
        print(f"{name} 나왔습니다 (거스름돈 {self.money - self.stock[name]['가격']}원)")
        self.stock[name]["재고"] -= 1
        self.money = 0

    def show(self):
        print("[자판기]")
        for i in self.stock:
            print(
                f"    {i} {self.stock[i]['가격']:,}원 (재고 {self.stock[i]['재고']}개)"
            )
        print(f"투입 금액 : {self.money}원")


print("\n3번 출력")
v = VendingMachine()
v.show()
v.insert(1000)
v.buy("콜라")
v.insert(1000)
v.buy("콜라")
v.buy("커피")
v.show()


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_loan = True
        self.ln_nm = ""
        self.ln_cnt = 0

    def borrow(self, who):
        if not self.is_loan:
            print(f"이미 대출 중입니다. (대출자 : {self.ln_nm})")
            return
        self.ln_nm = who
        self.ln_cnt += 1
        self.is_loan = False
        print(f"{self.title} 대출 완료 (대출자 : {who})")

    def give_back(self):
        if self.is_loan:
            print("대출 중이 아닙니다.")
            return
        print(f"{self.title} 반납 완료 (반납자 : {self.ln_nm})")
        self.ln_nm = ""
        self.is_loan = True

    def show(self):
        if self.is_loan:
            print(f"{self.title} / {self.author} / 대출 가능 / 누적 {self.ln_cnt}회")
            return
        print(
            f"{self.title} / {self.author} / 대출 중 ({self.ln_nm}) / 누적 {self.ln_cnt}회"
        )


print("\n4번 출력")
b = Book("사피엔스", "유발 하라리")
b.show()
b.give_back()
b.borrow("김철수")
b.show()
b.borrow("이영희")
b.give_back()
b.borrow("박민수")
b.show()


class Employee:
    def __init__(self, name, base_pay, years):
        self.nm = name
        self.bp = base_pay
        self.yr = years

    def get_position(self):
        return "사원"

    def bonus_rate(self):
        return 0.1

    def bonus(self):
        return int(self.bp * self.bonus_rate() + 100000 * self.yr)

    def get_total(self):
        return self.bp + self.bonus()

    def show(self):
        print(
            f"{self.nm} ({self.get_position()}, {self.yr}년)  기본급 {self.bp:,}원  보너스 {self.bonus():,}원  실수령 {self.get_total():,}원"
        )


class Manager(Employee):
    def get_position(self):
        return "팀장"

    def bonus_rate(self):
        return 0.3


print("\n5번 출력")
e1 = Employee("김철수", 3000000, 3)
e1.show()

m1 = Manager("이영희", 3000000, 7)
m1.show()

print()
print("[전체 명단]")
staff = [e1, m1, Employee("박민수", 2500000, 1)]

total = 0
best = staff[0]
for s in staff:
    s.show()
    total = total + s.get_total()
    if s.get_total() > best.get_total():
        best = s

print(f"총 인건비: {total:,}원")
print(f"최고 실수령: {best.nm}")


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        self.trans = []

    def deposit(self, amount):
        if amount <= 0:
            print("입금액은 0보다 커야합니다.")
            return
        self._balance += amount
        print(f"{amount:,}원 입금 (잔액{self._balance:,}원)")
        self.trans.append(f"입금 {amount}")

    def withdraw(self, amount):
        if amount > self._balance:
            print(f"잔액 부족 (현재 {self._balance:,}원)")
            return
        self._balance -= amount
        print(f"{amount:,}원 출금 (잔액 {self._balance:,}원)")
        self.trans.append(f"출금 {amount}")

    def history(self):
        print("[거래 내역]")
        for i in range(len(self.trans)):
            print(f"{i + 1}. {self.trans[i]}")

    def show(self):
        print(
            f"{self.owner}님 계좌  잔액 {self._balance:,}원  거래 {len(self.trans)}건"
        )


class SavingsAccount(Account):
    def __init__(self, owner, balance, rate):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        interest = int(self._balance * self.rate)
        self._balance += interest
        print(f"이자 {interest:,}원 지급")
        print(f"{interest:,}원 입금 (잔액 {self._balance:,}원)")
        self.trans.append(f"입금 {interest}")

    def withdraw(self, amount):
        if amount + 1000 > self._balance:
            print(f"잔액 부족 (현재 {self._balance:,}원)")
            return
        self._balance -= amount - 1000
        print("출금 수수료 1,000원")
        print(f"{amount:,}원 출금 (잔액 {self._balance:,}원)")
        self.trans.append(f"출금 {amount}")


print("\n6번 출력")
a = Account("김철수", 50000)
a.show()
a.deposit(10000)
a.deposit(-5000)
a.withdraw(20000)
a.withdraw(999999)
a.show()
a.history()

print()

s = SavingsAccount("이영희", 100000, 0.05)
s.show()
s.add_interest()
s.withdraw(20000)
s.show()
