# 문제 1


latencies = [
    120,
    95,
    340,
    110,
    88,
    205,
    130,
    99,
    410,
    150,
    102,
    118,
    260,
    91,
    175,
    133,
    108,
    96,
    220,
    145,
]

latencies = [
    120,
    95,
    140,
    110,
    88,
    205,
    130,
    99,
    160,
    150,
    102,
    118,
    190,
    91,
    175,
    133,
    108,
    96,
    185,
    145,
]
latencies.sort()

p50 = (latencies[int(len(latencies) / 2) - 1] + latencies[int(len(latencies) / 2)]) / 2
p95 = latencies[-2]
if p95 > 300:
    slo = "SLO 위반"
elif p95 > 200:
    slo = "SLO 주의"
else:
    slo = "정상"


print(f"""
=============================
1번 문제
=============================
p50: {p50}
p95: {p95}
{slo}
""")


# 문제 2

error_rates = [0.4, 0.6, 0.5, 0.3, 0.7, 1.2, 0.9, 1.4, 1.1, 1.0]
error_rates = [3.0, 3.2, 2.8, 3.0, 3.0, 1.0, 0.9, 1.1, 1.0, 5.5]
# error_rates = [0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.1, 0.0, 0.3, 0.1]
# error_rates = [1.0, 1.2, 0.8, 1.0, 1.0, 0.9, 1.1, 1.0, 0.8, 1.2]

before = error_rates[:5]
after = error_rates[5:]

before_mean = sum(before) / len(before)
after_mean = sum(after) / len(after)

if 5.0 >= max(after):
    result = "ROLLBACK"
elif before_mean == 0:
    if after_mean > 0:
        result = "HOLD"
    else:
        result = "PROMOTE"
elif after_mean >= before_mean * 1.5:
    result = "ROLLBACK"
elif after_mean >= before_mean * 1.2:
    result = "HOLD"
else:
    result = "PROMOTE"

print(f"""
=============================
2번 문제
=============================
배포 전 평균: {before_mean:.2f}
배포 후 평균: {after_mean:.2f}
{result}
""")

# 3번 문제
logs = [
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "ERROR",
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "ERROR",
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "INFO",
    "INFO",
]

logs = [
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "ERROR",
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "INFO",
    "INFO",
    "INFO",
    "WARN",
    "INFO",
    "INFO",
    "INFO",
    "WARN",
    "ERROR",
    "ERROR",
    "ERROR",
]

if logs[-3:] == ["ERROR", "ERROR", "ERROR"]:
    tier = "CRITICAL - 연속 장애 감지"
elif logs.count("ERROR") >= 4:
    tier = "CRITICAL"
elif logs.count("ERROR") >= 2 or logs.count("WARN") >= 10:
    tier = "WARNING"
else:
    tier = "HEALTHY"

print(f"""
=============================
3번 문제
=============================
총 로그 : {len(logs)}
ERROR : {logs.count("ERROR")} / WARN : {logs.count("WARN")}
에러율 : {(logs.count("ERROR") / len(logs)) * 100:.1f}%
{tier}
""")


# 4번 문제

# items = [12000, 8500, 30000, 4500]
# grade = "GOLD"
# coupon = 5000

items = [9000, 6000]
grade = "GOLD"
coupon = 8000

# items = [9000, 6000]
# grade = "SILVER"
# coupon = 0

# items = [12000, 8500, 30000, 4500]
# grade = "NONE"
# coupon = 0

items_sum = sum(items)

if grade == "GOLD":
    grade_price = int(items_sum * 0.1)
elif grade == "SILVER":
    grade_price = int(items_sum * 0.05)
else:
    grade_price = 0

price = grade_price + coupon

if int(items_sum * 0.3) < price:
    total = int(items_sum * 0.7)
    price = int(items_sum * 0.3)
else:
    total = items_sum - price
    price = price

if total >= 30000:
    box = 0
else:
    box = 3000

pay = total + box

print(f"""
=============================
4번 문제
=============================
상품 합계 : {items_sum}
총 할인 : {price}
배송비 : {box}
최종 결제 금액 : {pay}
""")
