import time
from datetime import datetime, timedelta


class Sometime:
    def __init__(self, timestamp=0, formatting="%Y-%m-%d", verbose=False):
        self.ts=timestamp # example: 1604757486
        self.formatting="%Y-%m-%d"
        self.verbose=verbose
        self.hourglass = parse(self.ts, self.formatting, self.verbose)
        self.ts = self.hourglass.get("timestamp", 0)
    
    def timestamp(self, ts=0):
        self.ts=ts
        self.hourglass = parse(self.ts, self.formatting, self.verbose)
        return self.hourglass.get("timestamp", 0)
    
    def from_iso(self, val, f):
        # print(f"Converting {val} to UNIX timestamp...")
        try:
            dt = datetime.strptime(val, f)
            self.ts = round(time.mktime(dt.timetuple()))
            self.hourglass = parse(self.ts, self.formatting, self.verbose)
        except:
            print("Sometime Warning: Check the formatting before running again.")
        return self
    
    def moment(self):
        # get whole date information
        return self.hourglass
    
    def year(self, years=0):
        if years == 0:
            return self.hourglass.get("%Y", "")
        self.timestamp(ts=calculate(self.ts, years=years))
        return self.year()
    
    def name_of_month(self):
        return self.hourglass.get("%B", "")
    
    def month(self, months=0):
        if months == 0:
            return self.hourglass.get("%m", "")
        self.timestamp(ts=calculate(self.ts, months=months))
        return self.month()
    
    def day(self, days=0):
        if days == 0:
            return self.hourglass.get("%d", "")
        self.timestamp(ts=calculate(self.ts, days=days))
        return self.day()
    
    def hour(self, hours=0):
        if hours == 0:
            return self.hourglass.get("%H", "")
        self.timestamp(ts=calculate(self.ts, hours=hours))
        return self.hour()
    
    def minute(self, minutes=0):
        if minutes == 0:
            return self.hourglass.get("%M", "")
        self.timestamp(ts=calculate(self.ts, minutes=minutes))
        return self.minute()
    
    def second(self, seconds=0):
        if seconds == 0:
            return self.hourglass.get("%S", "")
        self.timestamp(ts=calculate(self.ts, seconds=seconds))
        return self.second()
    
    def period(self):
        return self.hourglass.get("%p", "")
    
    def day_of_week(self):
        return self.hourglass.get("%A", "")
    
    def add(self, years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
        self.timestamp(ts=calculate(self.ts, years=years, months=months, days=days, hours=hours, minutes=minutes, seconds=seconds))
        return self
    
    def yesterday(self, formatting):
        self.timestamp(ts=calculate(self.ts, days=-1))
        return self.custom(formatting)
    
    def custom(self, formatting):
        # set custom formatting
        self.formatting=formatting
        self.hourglass = parse(self.ts, self.formatting, self.verbose)
        return self.hourglass.get(formatting, "")
        
    
def parse(ts=0, formatting="%Y-%m-%d", verbose=False):
    hourglass = {}
    try:
        ## format time
        if ts == 0: ts = int(time.time())
        t = time.localtime(int(ts))
        hourglass.update({"timestamp": ts})
        hourglass.update({"%Y": time.strftime("%Y", t)})
        hourglass.update({"%B": time.strftime("%B", t)})
        hourglass.update({"%m": time.strftime("%m", t)})
        hourglass.update({"%d": time.strftime("%d", t)})
        hourglass.update({"%H": time.strftime("%H", t)})
        hourglass.update({"%M": time.strftime("%M", t)})
        hourglass.update({"%S": time.strftime("%S", t)})
        hourglass.update({"%p": time.strftime("%p", t)})
        hourglass.update({"%A": time.strftime("%A", t)})
        hourglass.update({formatting: time.strftime(formatting, t)})
    except:
        if verbose:
            print("Sometime usage: Sometime(ts=0, formatting="", verbose=False)")
    return hourglass

def calculate(ts, years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
    if years > 0: days += (years * 365.25)
    if months > 0: days += (months * (365.25 / 12))
    if hours > 0: days += (hours / 24)
    if minutes > 0: days += (minutes / (24 * 60))
    if seconds > 0: days += (seconds / (24 * 60 * 60))
    ts = int(round(int(ts) + (days * 24 * 60 * 60)))
    if len(str(ts)) >= 11:
        ts = ts / 1000
    return ts
