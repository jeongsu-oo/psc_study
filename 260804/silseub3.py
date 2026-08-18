code_name = input("① 요원 코드명        (문자열)   예: Falcon")
secu_code = input("② 5자리 보안 코드     (정수)     예: 84269")
master_key = input('③ 마스터키 등급       (문자열)   "S" / "A" / "N" 중 하나')
now_temp = input("④ 현재 체온          (실수)     예: 36.5")
sec = input("⑤ 남은 시간(초)      (정수)     예: 200")

secu_code = int(secu_code)
now_temp = float(now_temp)
sec = int(sec)

st_secu_code = secu_code // 10000
nd_secu_code = secu_code % 10000 // 1000
rd_secu_code = secu_code % 10000 % 1000 // 100
fr_secu_code = secu_code % 10000 % 1000 % 100 // 10
fv_secu_code = secu_code % 10000 % 1000 % 100 % 10

if st_secu_code == fv_secu_code and nd_secu_code == fr_secu_code:
    print("복제된 코드 감지! 즉시 폐쇄합니다.")

else:
    case_a = (st_secu_code + nd_secu_code) >= (fr_secu_code + fv_secu_code)
    case_b = secu_code % 2 == 0 or secu_code % 3 == 0
    case_c = rd_secu_code % 2 == 1

    case2_a = case_a and case_b and case_c and master_key.upper() == "N"
    case2_b = case_a and (case_b or case_c) and master_key.upper() == "A"
    case2_c = case_a and master_key.upper() == "S"
    # if case_a and case_b and case_c and master_key.upper() != "N":
    #     print("보안 시스템 작동! 침입자를 체포하라!")
    # if case_a and (case_b or case_c) and master_key.upper() != "A":
    #     print("보안 시스템 작동! 침입자를 체포하라!")
    # if case_a and master_key.upper() != "S":
    #     print("보안 시스템 작동! 침입자를 체포하라!")
    if case2_a or case2_b or case2_c:
        print("1차 보안 통과")
        temp_gd = 36.0 <= now_temp <= 37.5
        temp_bd = 35.0 <= now_temp <= 38.5
        print("체온 확인 중")
        if temp_gd:
            status = "정상"
            print("정상")
        elif temp_bd:
            status = "주의"
            print("주의")
        else:
            status = "위독"
            print("위독")

        risk = st_secu_code * nd_secu_code / (fr_secu_code + 1)

        print("위험 상태 확인 중")
        if temp_gd:
            risk = risk
        elif temp_bd:
            risk = risk * 1.5
        else:
            risk = None

        if risk is None:
            print("생체 신호 위독! 의무실로 강제 이송합니다. (위험도: 측정 불가)")

        else:
            if risk >= 50:
                nd_sec = 180
            else:
                nd_sec = 60

            if nd_sec > sec:
                lack_sec = nd_sec - sec
                print(
                    f"시간 초과! 문이 다시 잠겼습니다. (부족한 시간: {lack_sec // 60}분 {lack_sec % 60:02d}초)"
                )
            else:
                enough_sec = sec - nd_sec
                print(
                    f"[{code_name}] 서버실 개방! 상태: {status} / 위험도: {risk:.2f} / 잔여 {enough_sec // 60}분 {enough_sec % 60:02d}초"
                )

    else:
        print("보안 시스템 작동! 침입자를 체포하라!")
