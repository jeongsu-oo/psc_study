print("""
      VIP 통합 무인 키오스크 시스템
      --------------------------------------
      """)

# movie = input("영화 1인 관람료를 입력하세요 (예 : 14000) : ")
# people = input("예매할 총 인원 수를 입력하세요 (예 : 3) : ")
# popcorn = input("팝콘 세트 1개 가격을 입력하세요 (예 : 9000) : ")
# popset = input("구매할 팝콘 세트 수를 입력하세요 (예 : 2) : ")
# vip = input("VIP 회원입니까? (y/n) : ")
# cash = input("보유한 현금 총액을 입력하세요 (예 : 60000) : ")

# movie_tot = int(movie) * int(people)
# popcorn_tot = int(popcorn) * int(popset)
# # total = round(movie_tot + popcorn_tot, -1)
# total = (movie_tot + popcorn_tot) // 10 * 10
# upto_vip = int(total * 0.2)
# is_vip = bool(vip.lower() == "y")
# is_pay = bool(int(cash) > total - upto_vip)

# print(f"""
#       ======================================
#                [최종 정산 및 영수증]
#       ======================================
#       * 영화 관람료 합계    : {movie_tot}원
#       * 팝콘 세트 합계      : {popcorn_tot}원
#       * 총 주문 금액       : {total}원
#       * VIP 할인 적용      : -{upto_vip}원 (회원 여부 : {is_vip})
#       * 10원 단위 절사     : 적용 완료
#       --------------------------------------
#       * 최종 결제 금액      : {total - upto_vip}원
#       * 보유 현금 총액      : {int(cash)}원
#       * 거스름돈           : {int(cash) - (total - upto_vip)}원
#       --------------------------------------
#       정상 예매 승인        : {is_pay}
#       ======================================
#       스파이더멘 : 브랜드 뉴 데이
#       """)
