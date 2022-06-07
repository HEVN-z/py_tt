import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370)))

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

print(time.strftime('%H:%M:%S', time.localtime(time.time())))

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

def strf_time(t):
    ct = {}
    ct['year'] = time.strftime('%Y', time.localtime(t))
    ct['month'] = time.strftime('%m', time.localtime(t))
    ct['day'] = time.strftime('%d', time.localtime(t))
    ct['hour'] = time.strftime('%H', time.localtime(t))
    ct['min'] = time.strftime('%M', time.localtime(t))
    ct['sec'] = time.strftime('%S', time.localtime(t))
    return ct

tt = 1347517370
print(convert_time(tt)['hour'], convert_time(tt)['minute'], convert_time(tt)['second'])
print(strf_time(tt)['hour'], strf_time(tt)['min'], strf_time(tt)['sec'])