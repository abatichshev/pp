from datetime import datetime, timedelta

current_date = datetime.now()
five_days_ago = current_date - timedelta(days=5)
print("Current date:", current_date)
print("Five days ago:", five_days_ago)



from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", today.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))



from datetime import datetime

current_datetime = datetime.now()
datetime_without_microseconds = current_datetime.replace(microsecond=0)
print("Original datetime:", current_datetime)
print("Datetime without microseconds:", datetime_without_microseconds)


from datetime import datetime

date1 = datetime(2023, 6, 15, 12, 30, 45)
date2 = datetime(2023, 6, 20, 8, 15, 30)

difference = abs((date2 - date1).total_seconds())
print("Difference between the two dates in seconds:", difference)
