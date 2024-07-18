a = int(input())
b = int(input())
h = int(input())
percent = float(input())

# 1l = 1m3
lateral_surface = a * b * h
volume = lateral_surface * 0.001


# total - percent

percent_of = volume * (percent / 100)

total = volume - percent_of

print(total)