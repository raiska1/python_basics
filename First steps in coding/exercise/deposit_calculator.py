deposit_sum = float(input())
time_deposit_months = int(input())
year_leverage_percent = float(input())

levarage = deposit_sum * (year_leverage_percent / 100)
levarage_second = levarage / 12
total = deposit_sum + time_deposit_months * levarage_second

print(total)
