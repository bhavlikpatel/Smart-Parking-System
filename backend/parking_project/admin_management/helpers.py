from datetime import datetime, timedelta, date
from dateutil import parser
from typing import Tuple


def manage_start_end_date(start_date, end_date, duration=15) -> Tuple[date, date]:
    """
    Function which accepts two dates and returns appropriate dates as per current date
    """

    today = date.today()

    if type(start_date) is str and type(end_date) is str:
        try:
            start_date = parser.parse(start_date).date()
            end_date = parser.parse(end_date).date()
        except parser.ParserError as pe:
            start_date = None
            end_date = None

    if type(start_date) is not date or type(end_date) is not date:
        end_date = today
        start_date = end_date - timedelta(days=duration)

    if not start_date and not end_date:
        end_date = today
        start_date = end_date - timedelta(days=duration)

    elif start_date > end_date:
        start_date, end_date = end_date, start_date

    elif not start_date and end_date:
        if end_date > today:
            end_date = today
        start_date = end_date - timedelta(days=duration)

    elif start_date and not end_date:
        if start_date > today:
            end_date = today
            start_date = end_date - timedelta(days=duration)
        else:
            end_date = start_date + timedelta(days=duration)

    return start_date, end_date
