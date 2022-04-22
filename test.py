from sometime import Sometime

print("\nDefault initialization")
dt = Sometime()

print("\nCustom initialization")
seconds = 1650614778
milliseconds = seconds * 1000

dt = Sometime(seconds)
dt = Sometime(milliseconds)

print("\nSet timestamp in seconds or milliseconds")
dt.timestamp(seconds)

print("\nSet date/time based on date/time string")
print("\nhttps://help.gnome.org/users/gthumb/stable/gthumb-date-formats.html.en")
dt.from_iso("2022-04-22", "%Y-%m-%d")
print("Timestamp:", dt.timestamp())

print("\nGet current Unix Timestamp in milliseconds")
print("Current Timestamp:", dt.now())

print("\nGet Unix Timestamp in milliseconds")
print("Timestamp:", dt.timestamp())

print("\nAdd or subtract years")
dt = Sometime(seconds)
dt.year(years=-25)
dt.year(years=100)
print("Year:", dt.year())

print("\nGet name of the month")
dt = Sometime(seconds)
dt.name_of_month()
print("Date of the Month:", dt.name_of_month())

print("\nAdd or subtract months")
dt = Sometime(seconds)
dt.month(months=-1)
dt.month(months=12)
print("Month:", dt.month())

print("\nAdd or subtract days")
dt = Sometime(seconds)
dt.day(days=-7)
dt.day(days=14)
print("Day:", dt.day())

print("\nAdd or subtract hours")
dt = Sometime(seconds)
dt.hour(hours=-8)
dt.hour(hours=24)
hour = dt.hour()
print("Hour:", dt.hour())

print("\nAdd or subtract minutes")
dt = Sometime(seconds)
dt.minute(minutes=-5)
dt.minute(minutes=30)
minute = dt.minute()
print("Minute:", dt.minute())

print("\nAdd or subtract seconds")
dt = Sometime(seconds)
dt.second(seconds=-1)
dt.second(seconds=30)
second = dt.second()
print("Second:", dt.second())

print("\nGet if AM/PM")
dt = Sometime(seconds)
dt.period()
print("Period:", dt.period())

print("\nGet the Day of the Week")
dt = Sometime(seconds)
print("Day of the Week:", dt.day_of_week())

print("\nAdd or subtract to date/time")
dt = Sometime(seconds)
print("Timestamp:", dt.timestamp())
dt.add(years=1, months=2, days=3, hours=4, minutes=5, seconds=6)
print("Timestamp:", dt.timestamp())

print("\nFormat date/time into string representation")
dt = Sometime(seconds)
print("Timestamp:", dt.custom("%Y-%m-%d %H:%M:%S %p"))

print("\nGet yestderday on custom formatting")
dt = Sometime(seconds)
print("Yesterday:", dt.yesterday("%Y-%m-%d %H:%M:%S %p"))

# more tests
print("\nMore tests...")
ts = 1508198400000
dt = Sometime(timestamp=ts)
print("Timestamp:", dt.timestamp())
dt.add(days=90)
print("Timestamp:", dt.timestamp())