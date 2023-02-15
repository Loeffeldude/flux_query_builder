from typing import Union
from datetime import timedelta, datetime
import re
from dateutil.parser import isoparse
from flux_query_builder.utility import S


class FluxTime:
    """FluxTime is a wrapper around a datetime or timedelta object that can be used to convert to a flux duration string

    Raises:
        ValueError: Must provide a timedelta, flux_time, or datetime
    """
    timedelta: timedelta = None
    datetime: datetime = None

    def __init__(
        self,
        timedelta: Union[timedelta, None] = None,
        flux_time: Union[str, None] = None,
        datetime: Union[datetime, None] = None,
    ) -> None:
        if timedelta is not None:
            self.timedelta = timedelta
        elif flux_time is not None:
            self.timedelta = self.parse_time(flux_time)
        elif datetime is not None:
            self.datetime = datetime
        else:
            raise ValueError("Must provide a timedelta, flux_time, or datetime")

    @classmethod
    def now(cls) -> "FluxTime":
        """Get the current time as a FluxTime object

        Returns:
            FluxTime:The flux time now
        """
        return cls(datetime=datetime.now())
    
    @classmethod
    def from_timedelta(cls, timedelta) -> "FluxTime":
        """Create a FluxTime object from a timedelta

        Args:
            timedelta (datetime.timedelta): The timedelta to use

        Returns:
            FluxTime: The flux time object
        """
        return cls(timedelta=timedelta)
    @classmethod
    def from_datetime(cls, datetime) -> "FluxTime":
        """Create a FluxTime object from a datetime

        Args:
            datetime (datetime.datetime): The datetime to use

        Returns:
            FluxTime: The flux time object
        """
        return cls(datetime=datetime)
    @classmethod
    def delta_to_flux(cls, delta: timedelta) -> str:
        """Convert a timedelta to a flux duration string

        Args:
            delta (timedelta): The timedelta to convert

        Returns:
            str: The flux duration string
        """
        result_string = ""

        if delta.days > 0:
            result_string += f"{delta.days}d"
        if delta.seconds > 0:
            result_string += f"{delta.seconds}s"
        if delta.microseconds > 0:
            result_string += f"{delta.microseconds}us"
        if result_string == "":
            result_string = "0s"
        return result_string
    @classmethod
    def parse_time(cls, time: str) -> Union[datetime, timedelta]:
        """Parse a string into a datetime or timedelta object

        Args:
            time (str): The time string to parse

        Returns:
            Union[datetime, timedelta]: The parsed time object
        """
        try:
            return isoparse(time)
        except ValueError:
            return cls.parse_duration(time)
    @staticmethod
    def parse_duration(dur: str) -> timedelta:
        """Parse a flux duration string into a timedelta object

        Args:
            dur (str): The duration string to parse

        Raises:
            ValueError: Invalid duration

        Returns:
            timedelta: The parsed timedelta object
        """
        if len(dur) < 2:
            raise ValueError("Invalid duration")

        is_negative = False
        if dur[0] == "-":
            is_negative = True
            dur = dur[1:]

        duration = timedelta()

        matches = re.finditer(r"(\d+)([a-zA-Z]+)", dur)

        matched = False

        for match in matches:
            matched = True
            measure = int(match.group(1))
            unit = match.group(2)

            if unit == "ns":
                duration += timedelta(microseconds=measure / 1000)
            elif unit == "us" or unit == "µs":
                duration += timedelta(microseconds=measure)
            elif unit == "ms":
                duration += timedelta(milliseconds=measure)
            elif unit == "m":
                duration += timedelta(minutes=measure)
            elif unit == "s":
                duration += timedelta(seconds=measure)
            elif unit == "h":
                duration += timedelta(hours=measure)
            elif unit == "d":
                duration += timedelta(days=measure)
            elif unit == "w":
                duration += timedelta(weeks=measure)
            elif unit == "mo":
                # use real duration values
                duration += timedelta(days=measure * 30)
            elif unit == "y":
                duration += timedelta(days=measure * 365)
            else:
                raise ValueError("Invalid duration")

        if not matched:
            raise ValueError("Invalid duration")

        if is_negative:
            duration = -duration

        return duration

    def __str__(self) -> str:
        if self.timedelta is not None:
            return str(S(self.delta_to_flux(self.timedelta)))
        elif self.datetime is not None:
            return str(S(self.datetime.isoformat()))
        else:
            raise ValueError("Must provide a timedelta or datetime")
