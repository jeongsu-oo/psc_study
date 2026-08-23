from pathlib import Path
import csv

BASE = Path(__file__).parent
DATA = BASE / "data"
DATA.mkdir(exist_ok=True)


# 1단계
class Book:
    def __init__(self, bk_id, title, author, cate):
        self.bk_id = bk_id
        self.title = title
        self.author = author
        self.cate = cate
        self.can_loan = True
        self.br_nm = ""
        self.loan_cnt = 0

    def borrow(self, who):
        if not self.can_loan:
            return False
        self.can_loan = False
        self.loan_cnt += 1
        self.br_nm = who
        return True

    def give_back(self):
        if self.can_loan:
            return False
        self.can_loan = True
        self.br_nm = ""
        return True

    def is_available(self):
        return bool(self.can_loan)

    def show(self):
        if self.can_loan:
            print(
                f"{self.bk_id}  {self.title} / {self.author} / {self.cate} / 대출가능 / 누적 {self.loan_cnt}회"
            )
            return
        print(
            f"{self.bk_id}  {self.title} / {self.author} / {self.cate} / 대출 중 ({self.br_nm}) / 누적 {self.loan_cnt}회"
        )


print("-------- 1단계 출력 --------")
b = Book("B001", "사피엔스", "유발 하라리", "인문")
b.show()
print("대출 결과:", b.borrow("김철수"))
b.show()
print("재대출 결과:", b.borrow("이영희"))
print("반납 결과:", b.give_back())
b.show()


# 2단계
class EBook(Book):
    def __init__(self, bk_id, title, author, cate, file_size):
        super().__init__(bk_id, title, author, cate)
        self.file_size = file_size

    def borrow(self, who):
        self.loan_cnt += 1
        self.can_loan = True
        return True

    def show(self):
        print(
            f"{self.bk_id}  {self.title} / {self.author} / {self.cate} / 전자책({self.file_size}MB) / 누적 {self.loan_cnt}회"
        )


print("\n-------- 2단계 출력 --------")
e = EBook("E001", "파이썬 입문", "홍길동", "IT", 15)
e.show()
print(e.borrow("김철수"))
print(e.borrow("이영희"))
print(e.borrow("박민수"))
e.show()


# 3단계
class Member:
    def __init__(self, mem_id, nm):
        self.mem_id = mem_id
        self.nm = nm
        self._bk_lst = []
        self.MX_LOAN = 3

    def can_borrow(self):
        return len(self._bk_lst) < 3

    def add_book(self, bk_id):
        self._bk_lst.append(bk_id)

    def remove_book(self, bk_id):
        if not self._bk_lst:
            return
        self._bk_lst.remove(bk_id)

    def get_books(self):
        return self._bk_lst.copy()

    def show(self):
        print(f"{self.mem_id} {self.nm} / 대출 {len(self._bk_lst)}권 / {self._bk_lst}")


print("\n-------- 3단계 출력 --------")
m = Member("M001", "김철수")
m.show()
print("빌릴 수 있나?", m.can_borrow())
m.add_book("B001")
m.add_book("B002")
m.add_book("B003")
m.show()
print("빌릴 수 있나?", m.can_borrow())

copied = m.get_books()
copied.append("B999")
print("목록 복사본 수정 후:", m.get_books())


# 4단계
class Library:
    def __init__(self, nm):
        self.nm = nm
        self.bks = {}
        self.mems = {}
        self.loan_lst = []

    def add_book(self, bk):
        if bk.bk_id in self.bks:
            return False
        self.bks[bk.bk_id] = bk
        return True

    def add_member(self, mem):
        if mem.mem_id in self.mems:
            return False
        self.mems[mem.mem_id] = mem
        return True

    def find_book(self, bk_id):
        if bk_id in self.bks:
            return self.bks[bk_id]
        return

    def find_member(self, mem_id):
        if mem_id in self.mems:
            return self.mems[mem_id]
        return

    def count(self):
        return len(self.bks), len(self.mems)

    # 5단계
    def borrow(self, mem_id, bk_id):
        if mem_id not in self.mems:
            print(f"없는 회원 : {mem_id}")
            return False

        if bk_id not in self.bks:
            print(f"없는 도서 : {bk_id}")
            return False

        member = self.mems[mem_id]
        if not member.can_borrow():
            print(f"대출 한도 초과 : {member.nm} ({len(member._bk_lst)}권)")
            return False

        book = self.bks[bk_id]
        if not book.is_available():
            print(f"이미 대출 중 : {book.title}")
            return False

        self.loan_lst.append({"구분": "대출", "회원": member.nm, "도서": book.title})
        print(f"{member.nm} -> {book.title} 대출 완료")
        book.borrow(member)
        member.add_book(bk_id)
        return True

    def give_back(self, mem_id, bk_id):
        if mem_id not in self.mems:
            print(f"없는 회원 : {mem_id}")
            return False

        if bk_id not in self.bks:
            print(f"없는 도서 : {bk_id}")
            return False

        member = self.mems[mem_id]
        book = self.bks[bk_id]
        if bk_id not in member.get_books():
            print(f"빌린 책이 아닙니다 : {book.title}")
            return False

        book.give_back()
        member.remove_book(bk_id)

        self.loan_lst.append({"구분": "반납", "회원": member.nm, "도서": book.title})
        print(f"{member.nm} -> {book.title} 반납 완료")

    # 6단계
    def list_books(self, available_only=False):
        print(f"[{self.nm} 도서 목록]")
        cnt = 0
        for i in self.bks.values():
            if available_only:
                if i.is_available:
                    i.show()
                    cnt += 1
            else:
                i.show()
                cnt += 1
        print(f"총 {cnt}권")

    def search(self, keyword):
        kw = keyword.lower()
        lst = []
        for i in self.bks.values():
            if kw in i.title.lower() or kw in i.author.lower():
                lst.append(i)
        return lst

    def by_category(self):
        dic = {}
        for i in self.bks.values():
            dic[i.cate] = dic.get(i.cate, 0) + 1
        return dic

    def most_borrowed(self, n=3):
        lst = list(self.bks.values())
        lst = sorted(lst, key=lambda x: x.loan_cnt, reverse=True)
        return lst[:n]

    # 7단계
    def save_books(self, path):
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write("도서번호,제목,저자,분류,상태,누적대출\n")
            f.writelines(
                f"{i.bk_id},{i.title},{i.author},{i.cate},{'대출가능' if i.is_available else '대출중'},{i.loan_cnt}\n"
                for i in self.bks.values()
            )
        return path

    def save_history(self, path):
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write("구분, 회원, 도서\n")
            f.writelines(
                f"{i['구분']},{i['회원']},{i['도서']}\n" for i in self.loan_lst
            )
        return path

    # 8단계
    def load_books(self, path):
        try:
            with open(path, "r", encoding="utf-8", newline="") as f:
                r = csv.reader(f)
                h = next(r)
                cnt = 0
                for i in r:
                    self.bks[i[0]] = i
                    cnt += 1
                return cnt

        except FileNotFoundError:
            print(f"파일이 없습니다 : {path.name}")
            return 0

    # 9단계
    def report(self):
        print("=" * 35)
        print(f"{self.nm} 운영 리포트")
        print("=" * 35)
        print(f"도서 {len(self.bks)}권 / 회원 {len(self.mems)}명")
        print("\n[분류별]")
        for i, j in self.by_category().items():
            print(f"{i} {j}권")
        print("\n[인기 도서]")
        cnt = 0
        for i in self.most_borrowed(2):
            cnt += 1
            print(f"{cnt}. {i.title} ({i.loan_cnt}회)")
        print("\n[회원 현황]")
        for i in self.mems:
            member = self.mems[i]
            print(f"{i} {member.nm} / 대출 {len(member._bk_lst)}권")
        print("\n[최근 기록]")
        last_5 = self.loan_lst[-5:]
        for i in last_5:
            print(f"{i['구분']} {i['회원']} -> {i['도서']}")
        print("=" * 35)


print("\n-------- 4단계 출력 --------")
lib = Library("중앙도서관")
print("도서 등록:", lib.add_book(Book("B001", "사피엔스", "유발 하라리", "인문")))
print("중복 등록:", lib.add_book(Book("B001", "다른책", "다른저자", "인문")))
lib.add_book(Book("B002", "총균쇠", "재레드 다이아몬드", "인문"))
lib.add_book(EBook("E001", "파이썬 입문", "홍길동", "IT", 15))
lib.add_member(Member("M001", "김철수"))
lib.add_member(Member("M002", "이영희"))

books, members = lib.count()
print(f"도서 수 {books}, 회원 수 {members}")
print("찾기 성공:", lib.find_book("B001").title)
print("찾기 실패:", lib.find_book("B999"))

print("\n-------- 5단계 출력 --------")
lib.borrow("M001", "B001")
lib.borrow("M002", "B001")
lib.borrow("M999", "B001")
lib.borrow("M001", "B999")
lib.borrow("M001", "E001")
lib.borrow("M002", "E001")
lib.give_back("M001", "B001")
lib.give_back("M001", "B002")

print("\n-------- 6단계 출력 --------")
lib.list_books()
print()
lib.list_books(available_only=True)
print()
print("검색 '파이썬':", [b.title for b in lib.search("파이썬")])
print("분류별:", lib.by_category())
print("인기 도서:", [(b.title, b.loan_cnt) for b in lib.most_borrowed(2)])

print("\n-------- 7단계 출력 --------")
p1 = lib.save_books(DATA / "books.csv")
print("저장 완료:", p1.name)
p2 = lib.save_history(DATA / "history.csv")
print("저장 완료:", p2.name)

with open(DATA / "books.csv", "r", encoding="utf-8-sig", newline="") as f:
    for row in csv.reader(f):
        print(row)

print("\n-------- 8단계 출력 --------")
lib2 = Library("분관")
print("불러온 도서:", lib2.load_books(DATA / "없는파일.csv"), "권")
print("불러온 도서:", lib2.load_books(DATA / "books.csv"), "권")
books, members = lib2.count()
print("새 도서관 도서 수:", books)

print("\n-------- 9단계 출력 --------")
lib.report()
