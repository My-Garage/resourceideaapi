from datetime import date
from datetime import datetime
from datetime import time
from datetime import timedelta
from typing import Optional


def get_workings_hours_between_dates(start_date: date, end_date: date) -> float:
    """Get the working hours between two dates

    Args:
        start_date(date): Period start date.
        end_date(date): Period end date.

    Returns:
        Total number of working hours in the period as a float.
    """
    total_period_hours: float = 0.0

    loop_date: date = start_date
    while loop_date <= end_date:
        if loop_date.weekday() < 5:  # Date is not a weekend.
            loop_date_start: datetime = datetime.combine(loop_date, time(hour=8, minute=0, second=0))
            loop_date_end: datetime = datetime.combine(loop_date, time(hour=17, minute=0, second=0))
            loop_date_delta: timedelta = loop_date_end - loop_date_start
            loop_hours: float = (loop_date_delta.total_seconds() / 3600) - 1.0  # subtract the lunch hour

            total_period_hours += loop_hours

        loop_date = loop_date + timedelta(1)  # Go to the next date

    return total_period_hours


def get_workings_hours_between_datetimes(start_date_time: datetime, end_date_time: datetime) -> float:
    """Get the working hours between two datetimes.

    Args:
        start_date_time(datetime): Period start date and time.
        end_date_time(datetime): Period end date and time.

    Returns:
        Total number of working hours in the period as a float.
    """
    total_period_hours: float = 0.0

    loop_date: datetime = start_date_time
    while loop_date <= end_date_time:
        if loop_date.weekday() < 5:  # Date is not a weekend.
            loop_date_end: datetime = datetime.combine(loop_date.date(), time(hour=17, minute=0, second=0))
            loop_date_delta: Optional[timedelta] = None
            loop_hours: float = 0.0
            if end_date_time < loop_date_end:
                lunch_start: datetime = datetime.combine(end_date_time.date(), time(hour=13, minute=0, second=0))
                lunch_end: datetime = datetime.combine(end_date_time.date(), time(hour=14, minute=0, second=0))
                if end_date_time <= lunch_start:  # End date and time come before lunch.
                    loop_date_delta = end_date_time - loop_date
                    loop_hours = loop_date_delta.total_seconds() / 3600
                elif end_date_time > lunch_start and end_date_time <= lunch_end:  # End date and time in lunch period.
                    loop_date_delta = lunch_start - loop_date
                    loop_hours = loop_date_delta.total_seconds() / 3600
                else:  # End date and time comes after lunch.
                    loop_date_delta = end_date_time - loop_date
                    loop_hours = (loop_date_delta.total_seconds() / 3600) - 1
            else:  # Period end does happen on the date being looped
                loop_date_delta = loop_date_end - loop_date
                loop_hours = (loop_date_delta.total_seconds() / 3600) - 1

            total_period_hours += loop_hours

        loop_date = datetime.combine((loop_date.date() + timedelta(1)), time(hour=8, minute=0, second=0))

    return total_period_hours
