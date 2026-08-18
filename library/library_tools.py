import datetime as dt

LOAN_DAYS = 14
FEE_PER_DAY = 100
MAX_BOOKS = 5


def get_due_date(x=LOAN_DAYS):
    """
    오늘부터 days 일 뒤의 날짜를 돌려줍니다.
    default = 14
    """
    return dt.date.today() - dt.timedelta(days=x)


def get_late_fee(late_days, per_day=FEE_PER_DAY):
    """
    연체료를 계산해서 돌려줍니다.
    (연체일 * 하루 요금)
    하루 요금 default = 100
    """
    return late_days * per_day


if __name__ == "__main__":
    print("library_tools 자체 테스트")
    print("[1] get_due_date() 함수 테스트")
    print(get_due_date())
    print(get_due_date(5))
    print(get_late_fee(10))
    print(get_late_fee(10, 1000))
