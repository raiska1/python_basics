year_basketball_tax = int(input())

basketball_shoes = year_basketball_tax * 0.4
shoes = year_basketball_tax - basketball_shoes

basketball_clothing = shoes * 0.2
clothing = shoes - basketball_clothing

basketball = clothing / 4

basketball_accessories = basketball / 5

total = shoes + clothing + basketball_accessories + basketball + year_basketball_tax

print(total)
