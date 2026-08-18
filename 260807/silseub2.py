data = [
    {
        "id": "B001",
        "loc": "울산",
        "line": 2,
        "eq": "P-01",
        "type": "프레스",
        "year": 2018,
        "m": {"temp": 85.2, "pres": 120.5, "vib": 1.2},
        "logs": [
            {"t": "08:00", "state": "RUN", "err": None},
            {"t": "09:00", "state": "WARN", "err": "TEMP_H"},
        ],
        "qc": {"insp": "Kim", "defect": True, "types": ["CRACK", "DENT"]},
    },
    {
        "id": "B002",
        "loc": "울산",
        "line": 1,
        "eq": "W-03",
        "type": "용접",
        "year": 2020,
        "m": {"temp": 450.5, "pres": 45.2, "vib": 0.4},
        "logs": [
            {"t": "08:00", "state": "RUN", "err": None},
            {"t": "10:00", "state": "RUN", "err": None},
        ],
        "qc": {"insp": "Lee", "defect": False, "types": []},
    },
    {
        "id": "B003",
        "loc": "창원",
        "line": 1,
        "eq": "I-02",
        "type": "사출",
        "year": 2015,
        "m": {"temp": 260.1, "pres": 230.2, "vib": 4.5},
        "logs": [
            {"t": "08:30", "state": "RUN", "err": None},
            {"t": "11:00", "state": "ERROR", "err": "PRES_L"},
            {"t": "11:15", "state": "STOP", "err": "EMER"},
        ],
        "qc": {"insp": "Park", "defect": True, "types": ["BURR"]},
    },
    {
        "id": "B004",
        "loc": "창원",
        "line": 2,
        "eq": "P-02",
        "type": "프레스",
        "year": 2019,
        "m": {"temp": 82.0, "pres": 115.0, "vib": 0.9},
        "logs": [{"t": "09:00", "state": "RUN", "err": None}],
        "qc": {"insp": "Kim", "defect": False, "types": []},
    },
    {
        "id": "B005",
        "loc": "울산",
        "line": 2,
        "eq": "I-01",
        "type": "사출",
        "year": 2021,
        "m": {"temp": 235.0, "pres": 210.0, "vib": 2.1},
        "logs": [
            {"t": "09:30", "state": "RUN", "err": None},
            {"t": "10:30", "state": "WARN", "err": "VIB_H"},
        ],
        "qc": {"insp": "Choi", "defect": True, "types": ["CRACK", "BURR"]},
    },
    {
        "id": "B006",
        "loc": "부산",
        "line": 1,
        "eq": "D-01",
        "type": "도장",
        "year": 2017,
        "m": {"temp": 60.5, "pres": 15.0, "vib": 0.2},
        "logs": [
            {"t": "07:30", "state": "RUN", "err": None},
            {"t": "12:00", "state": "ERROR", "err": "TEMP_L"},
        ],
        "qc": {"insp": "Lee", "defect": True, "types": ["SCRATCH"]},
    },
    {
        "id": "B007",
        "loc": "부산",
        "line": 2,
        "eq": "D-02",
        "type": "도장",
        "year": 2022,
        "m": {"temp": 65.0, "pres": 16.5, "vib": 0.3},
        "logs": [
            {"t": "08:00", "state": "RUN", "err": None},
            {"t": "13:00", "state": "RUN", "err": None},
        ],
        "qc": {"insp": "Park", "defect": False, "types": []},
    },
    {
        "id": "B008",
        "loc": "울산",
        "line": 1,
        "eq": "W-01",
        "type": "용접",
        "year": 2016,
        "m": {"temp": 470.2, "pres": 48.0, "vib": 0.8},
        "logs": [
            {"t": "09:00", "state": "WARN", "err": "TEMP_H"},
            {"t": "11:30", "state": "ERROR", "err": "GAS_ERR"},
        ],
        "qc": {"insp": "Choi", "defect": True, "types": ["CRACK", "HOLE"]},
    },
    {
        "id": "B009",
        "loc": "창원",
        "line": 1,
        "eq": "P-03",
        "type": "프레스",
        "year": 2020,
        "m": {"temp": 88.9, "pres": 122.0, "vib": 1.1},
        "logs": [{"t": "10:00", "state": "RUN", "err": None}],
        "qc": {"insp": "Kim", "defect": False, "types": []},
    },
    {
        "id": "B010",
        "loc": "부산",
        "line": 1,
        "eq": "I-03",
        "type": "사출",
        "year": 2019,
        "m": {"temp": 250.0, "pres": 215.5, "vib": 3.2},
        "logs": [
            {"t": "08:10", "state": "RUN", "err": None},
            {"t": "14:20", "state": "WARN", "err": "PRES_H"},
        ],
        "qc": {"insp": "Lee", "defect": True, "types": ["BURR", "DENT"]},
    },
]

# 문제 1
dic = {}
for i in data:
    dic[i["qc"]["insp"]] = 0

for i in dic:
    for j in data:
        if i == j["qc"]["insp"] and j["qc"]["defect"]:
            dic[i] += 1
        else:
            dic[i] += 0

print("1번 문제 답변 :", dic)


# 문제 2
dic = {}
rep = {}
for i in data:
    dic[i["type"]] = 0
    rep[i["type"]] = 0

# print("점검1", dic, rep)
for i in dic:
    for j in data:
        if j["year"] >= 2018 and i == j["type"]:
            for k in j["logs"]:
                if k["state"] == "ERROR":
                    dic[i] += j["m"]["vib"] * 1.2
                    rep[i] += 1
                else:
                    dic[i] += j["m"]["vib"]
                    rep[i] += 1

for i in dic:
    dic[i] = round(dic[i] / rep[i], 1)

print("2번 문제 답변 :", dic)


# 문제 3
dic = {}

for i in data:
    dic[i["id"]] = 0

for i in data:
    if i["qc"]["defect"]:
        dic[i["id"]] = 50 + 10 * len(i["qc"]["types"])
    else:
        dic[i["id"]] = 0 + 10 * len(i["qc"]["types"])
    for j in i["logs"]:
        if "ERROR" in j["state"]:
            dic[i["id"]] += 15
        elif "WARN" in j["state"]:
            dic[i["id"]] += 5

print("3번 문제 답변 :", dic)
