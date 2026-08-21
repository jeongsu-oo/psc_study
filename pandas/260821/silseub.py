# 1단계
students = [
    {"이름": "김철수", "반": "A", "국어": 90, "영어": 85, "수학": 100},
    {"이름": "이영희", "반": "A", "국어": 70, "영어": 95, "수학": 70},
    {"이름": "박민수", "반": "B", "국어": 55, "영어": 70, "수학": 63},
    {"이름": "최지은", "반": "A", "국어": 80, "영어": 85, "수학": 90},
    {"이름": "정하늘", "반": "B", "국어": 95, "영어": 92, "수학": 88},
    {"이름": "강동원", "반": "B", "국어": 60, "영어": 45, "수학": 72},
    {"이름": "윤서연", "반": "A", "국어": 88, "영어": 91, "수학": 79},
    {"이름": "임재현", "반": "B", "국어": 45, "영어": 58, "수학": 51},
]

SUBJECTS = ["국어", "영어", "수학"]


def get_total(stu):
    return stu["국어"] + stu["영어"] + stu["수학"]


def get_average(stu):
    return round(get_total(stu) / 3, 1)


def get_grade(avg):
    if avg >= 90:
        return "A"
    if avg >= 80:
        return "B"
    if avg >= 70:
        return "C"
    if avg >= 60:
        return "D"
    return "F"


print("\n------ 1단계 ------")
for s in [students[0], students[1], students[7]]:
    avg = get_average(s)
    print(f"{s['이름']}  총점 {get_total(s)}  평균 {avg}  등급 {get_grade(avg)}")

# for i in students:
#     print(
#         f"{i['이름']}  총점 {get_total(i)}  평균 {get_average(i)}  등급 {get_grade(get_average(i))}"
#     )


# 2단계
def print_report(students):
    print("이름     반  국어  영어  수학   총점   평균  등급")
    print("-------------------------------------------------")
    for i in students:
        avg = get_average(i)
        print(
            f"{i['이름']}   {i['반']}    {i['국어']}    {i['영어']}   {i['수학']}    {get_total(i)}    {avg}    {get_grade(avg)}"
        )


print("\n------ 2단계 ------")
print_report(students)


# 3단계
def subject_average(stu, sub):
    tot = 0
    for i in stu:
        tot += i[sub]
    return round(tot / len(stu), 1)


def subject_max(stu, sub):
    mx = stu[0][sub]
    for i in stu:
        if mx <= i[sub]:
            mx = i[sub]
            st = i["이름"]
    return st, mx


def print_subject_stats(stu):
    print("[과목별 평균]")
    print(
        f"국어  평균 {subject_average(stu, '국어')}  최고 - {subject_max(stu, '국어')[0]}({subject_max(stu, '국어')[1]})"
    )
    print(
        f"영어  평균 {subject_average(stu, '영어')}  최고 - {subject_max(stu, '영어')[0]}({subject_max(stu, '영어')[1]})"
    )
    print(
        f"수학  평균 {subject_average(stu, '수학')}  최고 - {subject_max(stu, '수학')[0]}({subject_max(stu, '수학')[1]})"
    )


print("\n------ 3단계 ------")
print_subject_stats(students)


# 4단계
def get_rank(stu, nm):
    lst = []
    for i in range(len(stu)):
        lst.append(stu[i]["이름"])
    if nm not in lst:
        return
    dic = {}
    for i in stu:
        dic[i["이름"]] = get_average(i)
    tp = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    rank = []
    rk = 0
    before = 0
    for i in tp:
        rk += 1
        # if before != i[1]:
        #     rk += 1
        rank.append((rk, i))
        before = i[1]
    for i in range(len(rank)):
        if nm == rank[i][1][0]:
            return rank[i][0]


def print_ranking(stu):
    print("[전체 등수]")
    for i in range(len(stu)):
        print(
            f"{get_rank(stu, stu[i]['이름'])}등  {stu[i]['이름']}  {get_average(stu[i])}"
        )


print("\n------ 4단계 ------")
print_ranking(students)
print("김철수의 등수:", get_rank(students, "김철수"))
print("없는사람의 등수:", get_rank(students, "없는사람"))


# 5단계
def group_by_class(stu):
    a_stu = []
    b_stu = []
    for i in stu:
        if i["반"] == "A":
            a_stu.append(i["이름"])
        if i["반"] == "B":
            b_stu.append(i["이름"])
    dic = {
        "A": a_stu,
        "B": b_stu,
    }
    return dic


def print_class_stats(stu):
    dic = group_by_class(stu)

    cls = {}
    for i in stu:
        cls[i["이름"]] = get_average(i)

    tp = sorted(cls.items(), key=lambda x: x[1], reverse=True)
    tp_a = []
    tp_b = []
    for i in tp:
        if i[0] in dic["A"]:
            tp_a.append(i)
        else:
            tp_b.append(i)
    avg = {
        "A": tp_a,
        "B": tp_b,
    }
    # print(avg)
    print("[반별 통계]")
    for i in dic:
        cls_avg = round(sum(stus[1] for stus in avg[i]) / len(dic[i]), 1)
        tp = avg[i][0]
        print(f"{i}반  {len(dic[i])}명  평균 {cls_avg}  최고 {tp[0]}({tp[1]})")


print("\n------ 5단계 ------")
print_class_stats(students)


# 6단계
def find_by_grade(stu, grade):
    lst = []
    for i in stu:
        tier = get_grade(get_average(i))
        if tier == grade:
            lst.append(i["이름"])
    return lst


def find_failed(stu, cutoff=60):
    lst = []
    for i in stu:
        sub = []
        if i["국어"] < cutoff:
            sub.append("국어")
        if i["영어"] < cutoff:
            sub.append("영어")
        if i["수학"] < cutoff:
            sub.append("수학")
        if sub:
            lst.append((i["이름"], sub))
    return lst


def print_warning(stu):
    print("[과락 경고]")
    lst = find_failed(stu)
    if not lst:
        print("과락자 없음")
        return
    # print(lst)
    for i, j in lst:
        student = next(k for k in stu if k["이름"] == i)
        # print(student)
        scr = []
        for k in j:
            sub = student[k]
            scr.append(f"{k}({sub})")
            print(f"{i}  {', '.join(scr)}")


print("\n------ 6단계 ------")
print("A등급:", find_by_grade(students, "A"))
print("F등급:", find_by_grade(students, "F"))
print()
print_warning(students)


# 7단계
def add_student(stu, nm, cls, kr, en, mt):
    lst = [i["이름"] for i in stu]
    if nm in lst:
        print(f"이미 있는 학생 : {nm}")
        return stu
    stu.append({"이름": nm, "반": cls, "국어": kr, "영어": en, "수학": mt})
    return stu


def update_score(stu, nm, sub, scr):
    lst = [i["이름"] for i in stu]
    if nm not in lst:
        print(f"없는 학생 : {nm}")
        return stu
    if scr > 100 or scr < 0:
        print(f"잘못된 점수 : {scr}")
        return stu
    for i in stu:
        if i["이름"] == nm:
            i[sub] = scr
    return stu


def remove_student(stu, nm):
    lst = [i["이름"] for i in stu]
    if nm not in lst:
        print(f"없는 학생 : {nm}")
        return
    lst2 = []
    for i in stu:
        if i["이름"] == nm:
            continue
        else:
            lst2.append(i)
    return lst2


print("\n------ 7단계 ------")
new_list = add_student(students, "한지민", "A", 85, 90, 88)
print(f"추가 후 인원: {len(new_list)}명")
new_list = add_student(new_list, "김철수", "A", 50, 50, 50)
new_list = update_score(new_list, "김철수", "수학", 150)
new_list = update_score(new_list, "홍길동", "수학", 90)
new_list = update_score(new_list, "김철수", "수학", 95)

for s in new_list:
    if s["이름"] == "김철수":
        print("김철수 수학:", s["수학"])
for s in students:
    if s["이름"] == "김철수":
        print("원본 김철수 수학:", s["수학"])

new_list = remove_student(new_list, "한지민")
print(f"삭제 후 인원: {len(new_list)}명")


# 8단계
def print_full_report(stu):
    print("=" * 50)
    print("                 성적 종합 리포트")
    print("=" * 50)
    print("\n(성적표)")
    print_report(students)
    print("\n(과목별 통계)")
    print_subject_stats(students)
    print("\n(반별 통계)")
    print_class_stats(students)
    print("\n(전체 등수)")
    print_ranking(students)
    print("")
    print_warning(students)


print("\n------ 8단계 ------")
print_full_report(students)
