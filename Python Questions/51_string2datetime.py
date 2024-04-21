# from datetime import datetime
# date = "Oct 14 2024 11:11AM"
# print(type(date))

# date_time = datetime.strptime(date,"%b %d %Y %I:%M%p ")
# print(date_time)

from dateutil import parser

date_time = parser.parse("May 14 2024 11:11AM")
print(date_time)