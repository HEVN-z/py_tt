try:
    print('try')
    5/0
except:
    print('Error')
# This mean try to do some statement, if it is error, then do except
# Try will do line by line til error


try:
    print('try2')
    5/0
except Exception as err:
    print(err)
# to check the error detail, use Exception as err


try:
    print('try3')
    5/0
except:
    pass
# pass is a empty statement, it will do nothing

# as some structure we cannot leave it empty we can replace it with pass

if True:
    pass
# if True, do nothing

