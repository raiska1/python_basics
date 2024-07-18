chicken_order = int(input())
fish_order = int(input())
vegan_order = int(input())

chicken_menu = 10.35
fish_menu = 12.40
vegan_menu = 8.15
# Desert = 20% from total (without delivery)
delivery = 2.50

chichen_total = chicken_order * chicken_menu
fish_total = fish_order * fish_menu
vegan_total = vegan_order * vegan_menu
total = chichen_total + fish_total + vegan_total

desert = total * 0.2

cost = total + desert + delivery

print(cost)