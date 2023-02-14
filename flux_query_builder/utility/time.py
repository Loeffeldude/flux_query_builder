from typing import Union
from datetime import timedelta, datetime
import re
from dateutil.parser import isoparse
from flux_query_builder.utility import S


class InvalidDurationException(Exception):
    pass


class FluxTime:
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
    def delta_to_flux(cls, delta: timedelta) -> str:
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
        try:
            return isoparse(time)
        except ValueError:
            return cls.parse_duration(time)

    @staticmethod
    def parse_duration(dur: str) -> timedelta:
        """
        parse_duration - parse a string into a timedelta object

        :param s: string in the format of "X[unit]" where X is a number and unit is one of ns, us, ms, s, m, h, d, w, mo

        :type s: str

        :return: timedelta object

        :raises InvalidDurationError: when the input string is not in the correct format"""
        if len(dur) < 2:
            raise InvalidDurationException("Invalid duration")

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
                raise InvalidDurationException("Invalid duration")

        if not matched:
            raise InvalidDurationException("Invalid duration")

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
