nums = [10, 12, 11]
print(max(nums) - min(nums))
if max(nums) - min(nums) >= 5:
    print("차이가 큽니다")
else:
    print("차이가 작습니다.")

# 문제 2
scores = [60, 55, 71]
mean = round(sum(scores) / len(scores), 2)
print(f"{mean:.2f}")
if mean >= 90:
    print("A")
elif mean >= 80:
    print("B")
elif mean >= 70:
    print("C")
else:
    print("D")

# 문제 3
cart = ["사과", "우유", "빵"]
item = "계란"

if item in cart:
    print(cart)
else:
    cart.append(item)
    print(cart)
