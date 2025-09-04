#1
import itertools

word = "ABCD"
perms = list(itertools.permutations(word))
print("\n".join("".join(p) for p in perms))
print(len(perms))

#2
from datetime import date, timedelta

today = date.today()
days_ahead = (1 - today.weekday()) % 7
next_tuesday = today + timedelta(days=days_ahead)
print(next_tuesday)

#3
import calendar
myinput = int(input("შეიყვანე წელი: "))
print("ნაკიანია" if calendar.isleap(myinput) else "არ არის ნაკიანი")

#4
today = date.today()
new_year = date(today.year + 1, 1, 1)
print((new_year - today).days // 7)

#5
from itertools import combinations
print(list(combinations([1,2,3,4,5], 3)))

#6
chars = "XYZ"

for i in range(1, len(chars)+1):
    for y in combinations(chars, i):
        print("".join(y))

