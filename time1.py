def time2s(x,y,z):
    x=x+z*3600+y*60
    return x

s=int(input('secend:'))
m=int(input('minute:'))
h=int(input('hour:'))

result=time2s(s,m,h)
print('seconds is:',result)