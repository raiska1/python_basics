pages = int(input())
pages_per_hour = int(input())
days_to_read = int(input())

pages_per_day = pages / days_to_read
hours = pages_per_day / pages_per_hour

print(int(hours))