from datetime import datetime, timezone


class Sometime:
    """Manipulate date/time in Unix Timestamp (seconds)."""

    def __init__(self, timestamp=None, utc=False):
        if not isinstance(utc, bool):
            raise TypeError("`utc` must be True or False only.")

        self._utc = utc
        self._timestamp = _clean_timestamp(timestamp, utc)

    def __getitem__(self, key):
        if key == "timestamp":
            return int(self._timestamp)
        return self.custom(key)

    def __setitem__(self, key, value):
        if key == "timestamp":
            self._timestamp = _clean_timestamp(value, self._utc)
        raise ValueError("`key` must exactly be the word `timestamp` only.")

    def now(self):
        """Get current timestamp."""
        return _clean_timestamp()

    def timestamp(self, timestamp=None):
        """Get or set timestamp."""
        if timestamp is None:
            return int(self._timestamp)
        self._timestamp = _clean_timestamp(timestamp, self._utc)

    def year(self, years=None):
        if isinstance(years, int):
            self._timestamp = _calculate(self._timestamp, years=years)
        return self.custom("%Y")

    def name_of_month(self):
        return self.custom("%B")

    def month(self, months=None):
        if isinstance(months, int):
            self._timestamp = _calculate(self._timestamp, months=months)
        return self.custom("%m")

    def day(self, days=None):
        if isinstance(days, int):
            self._timestamp = _calculate(self._timestamp, days=days)
        return self.custom("%d")

    def hour(self, hours=None):
        if isinstance(hours, int):
            self._timestamp = _calculate(self._timestamp, hours=hours)
        return self.custom("%H")

    def minute(self, minutes=None):
        if isinstance(minutes, int):
            self._timestamp = _calculate(self._timestamp, minutes=minutes)
        return self.custom("%M")

    def second(self, seconds=None):
        if isinstance(seconds, int):
            self._timestamp = _calculate(self._timestamp, seconds=seconds)
        return self.custom("%S")

    def period(self):
        return self.custom("%p")

    def day_of_week(self):
        return self.custom("%A")

    def add(self, years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
        self._timestamp = _calculate(
            self._timestamp,
            years=years,
            months=months,
            days=days,
            hours=hours,
            minutes=minutes,
            seconds=seconds,
        )
        return self

    def yesterday(self, formatting):
        """Get yesterdays date/time in custom formatting."""
        temp = _calculate(self._timestamp, days=-1)
        return _custom(self, temp, formatting, self._utc)

    def from_iso(self, value, formatting):
        """Converting datetime to UNIX timestamp."""
        dt = datetime.strptime(value, formatting)
        if self._utc:
            self._timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
            return self
        self._timestamp = dt.timestamp()
        return self

    def custom(self, formatting):
        return _custom(self, self._timestamp, formatting, self._utc)


def _custom(self, timestamp, formatting, utc):
    """https://help.gnome.org/users/gthumb/stable/gthumb-date-formats.html.en"""
    if utc:
        return datetime.utcfromtimestamp(timestamp).strftime(formatting)
    return datetime.fromtimestamp(timestamp).strftime(formatting)


def _clean_timestamp(timestamp=None, utc=False):
    """Reformat timestamp as necessary."""
    if timestamp is None:
        if utc:
            return datetime.now(timezone.utc)
        return datetime.now()
    return float(timestamp)


def _calculate(timestamp, years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
    """Calculate arithmetic operations on timestamp."""
    days += years * 365.2425
    days += months * (365.2425 / 12)
    days += hours / 24
    days += minutes / (24 * 60)
    days += seconds / (24 * 60 * 60)
    return timestamp + (days * 24 * 60 * 60)
