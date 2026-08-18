my_bag = ["낡은 검", "빨간 포션", "시민의 옷"]

item_name = input("새로 획득한 아이템 이름 : ")
item_price = int(input("새로 획득한 아이템 가격 : "))

my_bag.append(item_name)

if item_price >= 10000 or len(my_bag) == 4:
    tier = "상급 모험가"
else:
    tier = "초보 모험가"

print(f"""
판정된 모험 등급 {tier}
업데이트된 최종 가방 상태 {my_bag}
가방의 가장 첫 번째에 있는 아이템과 가장 마지막에 있는 아이템 {my_bag[0]}, {my_bag.pop()}
""")
