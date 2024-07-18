pens_to_buy = int(input())
sharpies_to_buy = int(input())
liters_of_cleaning_fluid = int(input())
percent_discount = int(input())

pen_price = 5.80
sharpies = 7.20
cleaning_fluid_liter = 1.20

total = (pens_to_buy * pen_price) + (sharpies_to_buy * sharpies) + (liters_of_cleaning_fluid * cleaning_fluid_liter)
total_with_discount = total * (percent_discount / 100)
discount = total - total_with_discount

print(discount)