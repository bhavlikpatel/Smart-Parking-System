from datetime import datetime, timedelta
from .constants import FieldConstants
from django.utils import timezone


def convert_string_datetime_into_datetime(date_time_string):
    date_time = datetime.strptime(date_time_string, "%Y-%m-%dT%H:%M:%SZ")
    return date_time


def convert_date_and_time_into_datetime(date, time):
    formatted_time = datetime.strptime(str(time), '%H:%M').time()
    formatted_datetime = datetime.combine(date, formatted_time)
    return formatted_datetime


class TimeRange(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.duration = self.end - self.start

    def is_overlapped(self, time_range):
        if max(self.start, time_range.start) < min(self.end, time_range.end):
            return True
        else:
            return False

    def get_overlapped_range(self, time_range):
        if not self.is_overlapped(time_range):
            return

        if time_range.start >= self.start:
            if self.end >= time_range.end:
                return TimeRange(time_range.start, time_range.end)
            else:
                return TimeRange(time_range.start, self.end)
        elif time_range.start < self.start:
            if time_range.end >= self.end:
                return TimeRange(self.start, self.end)
            else:
                return TimeRange(self.start, time_range.end)

    def __repr__(self):
        return '{0} ------> {1}'.format(*[timezone.time.strftime('%Y-%m-%d %H:%M:%S', timezone.time.localtime(d))
                                          for d in [self.start, self.end]])
