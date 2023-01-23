from sometime import Sometime

print("\nDefault initialization")
ts = Sometime()

print("\nCustom initialization")
seconds = 1650614778

ts = Sometime(seconds)

print("\nSet timestamp in seconds")
ts.timestamp(seconds)

print("\nSet date/time based on date/time string")
print("\nhttps://help.gnome.org/users/gthumb/stable/gthumb-date-formats.html.en")
ts.from_iso("2022-04-22", "%Y-%m-%d")
print("Timestamp:", ts.timestamp())

print("\nGet current Unix Timestamp in milliseconds")
print("Current Timestamp:", ts.now())

print("\nGet Unix Timestamp in milliseconds")
print("Timestamp:", ts.timestamp())

print("\nAdd or subtract years")
ts = Sometime(seconds)
ts.year(years=-25)
ts.year(years=100)
print("Year:", ts.year())

print("\nGet name of the month")
ts = Sometime(seconds)
ts.name_of_month()
print("Date of the Month:", ts.name_of_month())

print("\nAdd or subtract months")
ts = Sometime(seconds)
ts.month(months=-1)
ts.month(months=12)
print("Month:", ts.month())

print("\nAdd or subtract days")
ts = Sometime(seconds)
ts.day(days=-7)
ts.day(days=14)
print("Day:", ts.day())

print("\nAdd or subtract hours")
ts = Sometime(seconds)
ts.hour(hours=-8)
ts.hour(hours=24)
hour = ts.hour()
print("Hour:", ts.hour())

print("\nAdd or subtract minutes")
ts = Sometime(seconds)
ts.minute(minutes=-5)
ts.minute(minutes=30)
minute = ts.minute()
print("Minute:", ts.minute())

print("\nAdd or subtract seconds")
ts = Sometime(seconds)
ts.second(seconds=-1)
ts.second(seconds=30)
second = ts.second()
print("Second:", ts.second())

print("\nGet if AM/PM")
ts = Sometime(seconds)
ts.period()
print("Period:", ts.period())

print("\nGet the Day of the Week")
ts = Sometime(seconds)
print("Day of the Week:", ts.day_of_week())

print("\nAdd or subtract to date/time")
ts = Sometime(seconds)
print("Timestamp:", ts.timestamp())
ts.add(years=1, months=2, days=3, hours=4, minutes=5, seconds=6)
print("Timestamp:", ts.timestamp())

print("\nFormat date/time into string representation")
ts = Sometime(seconds)
print("Timestamp:", ts.custom("%Y-%m-%d %H:%M:%S %p"))

print("\nGet yestderday on custom formatting")
ts = Sometime(seconds)
print("Yesterday:", ts.yesterday("%Y-%m-%d %H:%M:%S %p"))

# more tests
print("\nMore tests...")
ts = 1508198400
ts = Sometime(timestamp=ts)
print("Timestamp:", ts.timestamp())
ts.add(days=90)
print("Timestamp:", ts.timestamp())

print("Year: " + ts["%Y"])