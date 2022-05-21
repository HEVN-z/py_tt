i = 1
while i <= 10:
    print('i =',i)
    i += 1

# (start)           i = 1
# while (stop):     i <= 10    if (stop) condition is false, the loop is stop
#    (step)         i += 1

for j in range(1,11): # step is 1 as default
    print('j =',j)

for j in range(1,11,1):
    print('j =',j)

# for j in range((start),(stop),(step))
# if start < step then step
# define j = start if j < stop then j += step
#        j = 1 < 11 then j+= 1

for k in range(0,12,2): # if step = 2
    print('k =',k)

for l in range(5,-21,-1): # if step = minus
    print('\tL =',l)

#
#