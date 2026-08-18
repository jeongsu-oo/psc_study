# 문제 4
a, b, c = 4, 4, 4

# if b <= a <= c or c <= a <= b:
#     print(a)
# elif a <= b <= c or c <= b <= a:
#     print(b)
# elif a <= c <= b or b <= c <= a:
#     print(c)

lst = [a, b, c]
lst.remove(max(lst))
lst.remove(min(lst))
print(lst)


# 문제 5
todo = ["운동"]
x = "운동"

# if x not in todo:
#     print("목록에 없습니다.")
#     print(todo)
# elif [x] == todo:
#     print("할 일이 없습니다.")
#     print(todo)
# elif x in todo:
#     todo.remove(x)
#     print("삭제완료")
#     print(todo)

if x not in todo:
    print("목록에 없습니다.")
    print(todo)
elif x in todo:
    todo.remove(x)
    if todo == []:
        print("할 일이 없습니다.")
        print(todo)
    else:
        print("삭제완료")
        print(todo)

# 문제 6
sales = [10, 20, 30, 40, 50, 60]
sales = [1, 2, 2, 1]

st = sales[: int(len(sales) / 2)]
nd = sales[int(len(sales) / 2) :]

print(sum(st), sum(nd))

if sum(st) > sum(nd):
    print("전반 우세")
elif sum(st) == sum(nd):
    print("동일")
elif sum(st) < sum(nd):
    print("후반 우세")
