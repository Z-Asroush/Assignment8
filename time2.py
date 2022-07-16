def s2time(x):
    z=int(x/3600)
    b1=int(x%3600)
    y=int(b1/60)
    x=int(b1%60)
    print(z,'h',' ', y,'m',' ',x,'s')

s=int(input('secend:'))
result=s2time(s)