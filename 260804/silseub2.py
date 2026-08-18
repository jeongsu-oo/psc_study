name = input("이름을 입력하세요. :")
level = input("레벨을 입력하세요. :")
attack = input("공격력을 입력하세요. :")
shield = input("방패 소지 여부를 입력하세요. (y/n) :")

level = int(level)
attack = int(attack)
is_shield = bool(shield.lower() == "y")
buff = attack * 1.5

if level >= 10 and attack >= 50:
    if is_shield == True or level >= 30:
        print("전설의 버프가 발동하여 공격력이 상승합니다!")
    else:
        print("최종 결과 출력 중입니다.")
else:
    print("입장 자격 미달입니다. 더 수련하고 오세요!")

print(f"""
최종 결과 출력
=======================================
심사 결과
=======================================
모험가 이름 : {name}
레벨 : {level}
최종 전투력 : {buff if is_shield == True or level >= 30 else attack}
""")
