protective_layer_needed = int(input())
paint_needed = int(input())
paint_thinner_needed = int(input())
hours_of_work = int(input())

protective_layer_price = 1.50
paint_price = 14.50
paint_thinner_price = 5
paper_bag = 0.40
# Total paint + 10% and 2 m2 paint and 0.40 for paper bag
# 1 hour = Workers take 30% from all materials

total_protective_layer_price = (protective_layer_needed + 2) * protective_layer_price

total_paint_price = paint_needed * paint_price
total_pain_extra = total_paint_price * 0.1
total_paint = total_paint_price + total_pain_extra

total_paint_thinner = paint_thinner_needed * paint_thinner_price

total = total_protective_layer_price + total_paint + total_paint_thinner + paper_bag

workers_payment = total * 0.3
total_workers_payment = workers_payment * hours_of_work

absolute_total = total_workers_payment + total

print(absolute_total)
