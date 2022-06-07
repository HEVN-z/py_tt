import time

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

print(strf_time(tt)['hour'], strf_time(tt)['min'], strf_time(tt)['sec'])