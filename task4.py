import datetime
import utils
from sys import argv
date = datetime.datetime(year=2022, month=4, day=7)
date.strftime("%Y-%M-%d")
print(utils.currency_rates(input(argv[1:])), date)