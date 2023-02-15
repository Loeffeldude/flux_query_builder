from flux_query_builder.utility.time import FluxTime
from datetime import timedelta, datetime
import unittest
from unittest.mock import MagicMock
from freezegun import freeze_time


class FluxTimeTest(unittest.TestCase):
    def test_timedelta(self):
        t = FluxTime.from_timedelta(timedelta(days=1))
        t_sec = FluxTime.from_timedelta(timedelta(days=4, seconds=1))
        t_micro = FluxTime.from_timedelta(timedelta(days=4, seconds=1, microseconds=1))

        self.assertEqual(str(t), '"1d"')
        self.assertEqual(str(t_sec), '"4d1s"')
        self.assertEqual(str(t_micro), '"4d1s1us"')

    def test_datetime(self):
        date = datetime(2021, 1, 1)
        t = FluxTime.from_datetime(date)

        self.assertEqual(str(t), '"2021-01-01T00:00:00"')
    
    @freeze_time("2021-01-01")
    def test_now(self):
        t = FluxTime.now()

        self.assertEqual(str(t), f'"{datetime.now().isoformat()}"')

    def test_no_args(self):
        with self.assertRaises(ValueError):
            FluxTime()

    def test_invalid_time(self):
        with self.assertRaises(ValueError):
            FluxTime(flux_time="invalid")

    def test_invalid_duration_string(self):
        with self.assertRaises(ValueError):
            FluxTime(flux_time="1d1s1us1invalid")
    
    def test_duration(self):
        t = FluxTime(flux_time="1d1s1us")

        self.assertEqual(str(t), '"1d1s1us"')
        self.assertEqual(t.timedelta, timedelta(days=1, seconds=1, microseconds=1))

    def test_duration_no_units(self):
        with self.assertRaises(ValueError):
            t = FluxTime(flux_time="1")

    