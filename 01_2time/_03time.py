import time

def convert_time(t):
    lt = time.localtime(t)
    ct = {}
    ct['year'] = lt.tm_year
    ct['month'] = lt.tm_mon
    ct['day'] = lt.tm_mday
    ct['hour'] = lt.tm_hour
    ct['minute'] = lt.tm_min
    ct['second'] = lt.tm_sec
    return ct

tt = 1347517370

print(convert_time(tt)['hour'], convert_time(tt)['minute'], convert_time(tt)['second'])