#8
import random
from datetime import datetime, timedelta, date

start = datetime.now()
player1 = start + timedelta(seconds=random.randint(5,20))
player2 = start + timedelta(seconds=random.randint(5,20))

print("Player 1 wins!" if player1<player2 else "Player 2 wins!" if player2<player1 else "It's a tie!")

#9

input_date = input("შეიყვანე დაბადების თარიღი (YYYY-MM-DD): ")
y,m,d = map(int,input_date.split("-"))
birthday = date(y,m,d)
todayy = date.today()
n = date(todayy.year,3,1)
if n < todayy:
    n = date(todayy.year+1,birthday.month,birthday.day)
print((n-todayy).days)

#10
from itertools import product
password = [random.randint(1,6) for _ in range(4)]

for attempt in product(range(1,7), repeat=4):
    print(attempt)
    if list(attempt) == password:
        print("Password correct, safe is open!")
        break