square_meters_for_greening = float(input())

price_for_greening = square_meters_for_greening * 7.61
discounted_price = price_for_greening * 0.18
discount = price_for_greening - discounted_price

print(f"The final price is: {discount} lv.")
print(f"The discount is: {discounted_price} lv.")