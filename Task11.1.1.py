import datetime


class Date:

    @staticmethod
    def date():
        date = datetime.datetime(day=5, month=6, year=2022)
        date.strftime('%d-%m-%Y')
        return date

    @classmethod
    def date_1(cls):
        list_1 = []
        date = datetime.datetime(day=5, month=6, year=2022)
        date.strftime('%d-%m-%Y')
        year_int = int(date.strftime('%Y'))
        month_int = int(date.strftime('%m'))
        day_int = int(date.strftime('%d'))
        return f'{day_int}, {month_int}, {year_int}'
print(Date.date())
print(Date.date_1())
