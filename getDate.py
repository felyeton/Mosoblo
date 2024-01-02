from datetime import datetime

iso_begin = "2023-12-04 00:00:00"
iso_end = "2023-12-04 23:59:59"
dt_begin = datetime.fromisoformat(iso_begin)
dt_end = datetime.fromisoformat(iso_end)

print(iso_begin, iso_end)

print(dt_begin, dt_end, datetime.timestamp(dt_begin)*1000, (1+datetime.timestamp(dt_end))*1000-1)

print(datetime.fromtimestamp(1701723600.000))






