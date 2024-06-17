import datetime


def get_week_info(date_str: str) -> dict|Exception:
    '''Calculate monday and friday of the week which contains the given day.

    :param date_str: a string object in format `year-month-day`.
    :Return: a dict object in format
        {
            monday = date of monday
            friday = date of friday
        } 
    '''
    date_str_components = date_str.split('-')
    if len(date_str_components) != 3:
        return Exception(f'`{date_str}` is not in format `year-month-day`')
    
    year_str, month_str, day_str = date_str_components
    try:
        date_obj = datetime.datetime(
            year=int(year_str),
            month=int(month_str),
            day=int(day_str)
        )
        weekday = date_obj.weekday()
        monday = date_obj - datetime.timedelta(days=weekday)
        friday = monday + datetime.timedelta(days=4)
        week_info = {
            'monday': monday.strftime('%Y-%m-%d'),
            'friday': friday.strftime('%Y-%m-%d')
        }
        return week_info
    
    except Exception as ex:
        return Exception(f'fail to get week info: {ex}')