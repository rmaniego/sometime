import time
from datetime import datetime, timedelta


class Sometime:
    """ Manipulate date/time in Unix Timestamp (milliseconds). """
    def __init__(self, timestamp=None):
        self._ms = _clean_timestamp(timestamp)
    
    def now(self):
        """ Get current timestamp. """
        return _clean_timestamp(None)
    
    def timestamp(self, timestamp=None):
        """ Get or set timestamp. """
        if timestamp is None:
            return self._ms
        self._ms = _clean_timestamp(timestamp)
    
    def year(self, years=None):
        if isinstance(years, int):
            self._ms = _calculate(self._ms, years=years)
        return self.custom("%Y")
    
    def name_of_month(self):
        return self.custom("%B")
    
    def month(self, months=None):
        if isinstance(months, int):
            self._ms = _calculate(self._ms, months=months)
        return self.custom("%m")
    
    def day(self, days=None):
        if isinstance(days, int):
            self._ms = _calculate(self._ms, days=days)
        return self.custom("%d")
    
    def hour(self, hours=None):
        if isinstance(hours, int):
            self._ms = _calculate(self._ms, hours=hours)
        return self.custom("%H")
    
    def minute(self, minutes=None):
        if isinstance(minutes, int):
            self._ms = _calculate(self._ms, minutes=minutes)
        return self.custom("%M")
    
    def second(self, seconds=None):
        if isinstance(seconds, int):
            self._ms = _calculate(self._ms, seconds=seconds)
        return self.custom("%S")
    
    def period(self):
        return self.custom("%p")
    
    def day_of_week(self):
        return self.custom("%A")
    
    def add(self, years=None, months=None, days=None, hours=None, minutes=None, seconds=None):
        self._ms = _calculate(self._ms, years=years, months=months, days=days, hours=hours, minutes=minutes, seconds=seconds)
        return self
    
    def yesterday(self, formatting):
        """ Get yesterdays date/time in custom formatting. """
        temp = self._ms
        self._ms = _calculate(self._ms, days=-1)
        formatted = self.custom(formatting)
        self._ms = temp
        return formatted
    
    def from_iso(self, value, formatting):
        """ Converting datetime to UNIX timestamp. """
        try:
            dt = datetime.strptime(value, formatting)
            self._ms = int(time.mktime(dt.timetuple()) * 1000)
            return self
        except:
            print("\nSometime Warning: Invalid formatting", formatting)
    
    def custom(self, formatting):
        """ https://help.gnome.org/users/gthumb/stable/gthumb-date-formats.html.en """
        try:
            ts = time.localtime(self._ms // 1000)
            return time.strftime(formatting, ts)
        except:
            print("\nSometime Warning: Invalid formatting", formatting)

def _clean_timestamp(timestamp):
    """ Reformat timestamp as necessary. """
    if isinstance(timestamp, (int, float)):
        if len(str(int(timestamp))) == 10:
            timestamp = int(time.time() * 1000)
        if len(str(int(timestamp))) == 13:
            return int(timestamp)
    return int(time.time()*1000)

def _calculate(timestamp, years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
    """ Calculate arithmetic operations on timestamp. """
    try:
        days += (years * 365.25)
        days += (months * (365.25 / 12))
        days += (hours / 24)
        days += (minutes / (24 * 60))
        days += (seconds / (24 * 60 * 60))
        return round((timestamp + (days * 24 * 60 * 60 * 1000)))
    except Exception as e:
        print("\nSometime Warning 3: Date and time values must be numeric.")
