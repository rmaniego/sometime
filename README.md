# sometime
Get timestamp, formatted date, and perform date/time operations.

## Official Release
**Sometime** v1.2.0

`pip install sometime -U`

## Basic Usage

```python
from sometime import Sometime
```

```python
# Default initialization
ts = Sometime()

# Custom initialization
ts = Sometime(1650614778, utc=True)

# Set timestamp in seconds
ts.timestamp(seconds)
ts["timestamp"] = seconds

# Set date/time based on date/time string
# https://help.gnome.org/users/gthumb/stable/gthumb-date-formats.html.en"
ts.from_iso("2022-04-22", "%Y-%m-%d")
print("Timestamp:", ts.timestamp())
```

# Get Unix Timestamp
```python
print("Timestamp:", ts.timestamp())
```

# Get current Unix Timestamp
```python
print("Current Timestamp:", ts.now())
```

# Add or subtract years
```python
ts = Sometime(seconds)
ts.year(years=-25)
ts.year(years=100)
print("Year:", ts.year())
print("Year:", ts["%Y"])
```

# Get name of the month
```python
ts = Sometime(seconds)
ts.name_of_month()
print("Date of the Month:", ts.name_of_month())
```

# Add or subtract months
```python
ts = Sometime(seconds)
ts.month(months=-1)
ts.month(months=12)
print("Month:", ts.month())
```

# Add or subtract days
```python
ts = Sometime(seconds)
ts.day(days=-7)
ts.day(days=14)
print("Day:", ts.day())
```

# Add or subtract hours
```python
ts = Sometime(seconds)
ts.hour(hours=-8)
ts.hour(hours=24)
hour = ts.hour()
print("Hour:", ts.hour())
```

# Add or subtract minutes
```python
ts = Sometime(seconds)
ts.minute(minutes=-5)
ts.minute(minutes=30)
minute = ts.minute()
print("Minute:", ts.minute())
```

# Add or subtract seconds
```python
ts = Sometime(seconds)
ts.second(seconds=-1)
ts.second(seconds=30)
second = ts.second()
print("Second:", ts.second())
```

# Get if AM/PM
```python
ts = Sometime(seconds)
ts.period()
print("Period:", ts.period())
```

# Get the Day of the Week
```python
ts = Sometime(seconds)
print("Day of the Week:", ts.day_of_week())
```

# Add or subtract to date/time
```python
ts = Sometime(seconds)
print("Timestamp:", ts.timestamp())
ts.add(years=1, months=2, days=3, hours=4, minutes=5, seconds=6)
print("Timestamp:", ts.timestamp())
```

# Format date/time into string representation
```python
ts = Sometime(seconds)
print("Timestamp:", ts.custom("%Y-%m-%d %H:%M:%S %p"))
```

# Get yesterday's on custom formatting
```python
ts = Sometime(seconds)
print("Yesterday:", ts.yesterday("%Y-%m-%d %H:%M:%S %p"))
```