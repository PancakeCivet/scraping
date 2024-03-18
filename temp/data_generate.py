import datetime

start_date = datetime.date(2024, 3, 15)
end_date = datetime.date(2016, 1, 1)

delta = datetime.timedelta(days=-1)  # 递减的时间间隔，每次减去一天
current_date = start_date

while current_date >= end_date:
    date_string = current_date.strftime("%Y%m%d")
    with open("data.txt", "a", encoding="utf-8") as f:
        f.write(date_string + "\n")
    current_date += delta
