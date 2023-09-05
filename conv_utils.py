from datetime import datetime, timedelta


def dt_to_str(date):
    """
    :param date: date as Datetime obj
    :return: date as string
    """
    return date.strftime("%Y-%m-%d")


def str_to_dt(date_str):
    """
    :param date_str: date as string
    :return: Datetime obj
    """
    return datetime.strptime(date_str, "%Y-%m-%d")


def get_multiple_dt(date, days=1):
    """
    :param date: date as Datetime obj
    :param days: number of days, inclusive (always returns one day at minimum)
    :return: list, len=days+1, of Datetime obj
    """
    if days < 1:
        days = 1 # TODO: return api error, "no backdating"
    elif days > 30:
        days = 30 # TODO: return api error, "max days = 30"

    if type(days) != int:
        try:
            days = int(days)
        except:
            # TODO: return api error, "days must be an integer"
            days = 1

    list_of_dates = [date] # always return today
    for day_count in range(days):
        list_of_dates.append(
            date + timedelta(days=day_count+1) # add one day ahead for each requested
        )
    return list_of_dates


def conv_timezone(time_str, timezone):

    """
    Example sunrise-sunset api output, UNformatted (so we get tz offsets)
    {'results': {'astronomical_twilight_begin': '2023-09-15T09:03:40+00:00',
             'astronomical_twilight_end': '2023-09-16T00:38:49+00:00',
             'civil_twilight_begin': '2023-09-15T10:09:15+00:00',
             'civil_twilight_end': '2023-09-15T23:33:14+00:00',
             'day_length': 45111,
             'nautical_twilight_begin': '2023-09-15T09:36:53+00:00',
             'nautical_twilight_end': '2023-09-16T00:05:36+00:00',
             'solar_noon': '2023-09-15T16:51:15+00:00',
             'sunrise': '2023-09-15T10:35:19+00:00',
             'sunset': '2023-09-15T23:07:10+00:00'},
     'status': 'OK'}
    """
    pass