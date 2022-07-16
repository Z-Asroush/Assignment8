
from unittest import result


def sum(x,y):
      result={}
      i=int((x['s']+y['s'])/60)
      m=int((x['m']+y['m']+i)/60)
      result['h']=x['h']+y['h']+m
      result['m']=(x['m']+y['m']+i)%60
      result['s']=(x['s']+y['s'])%60
      return result

def subtraction(x,y):
      result={}
      h1=x['h']
      m1=x['m']
      s1=x['s']
      h2=y['h']
      m2=y['m']
      s2=y['s']
      s1=s1+h1*3600+m1*60
      s2=s2+h2*3600+m2*60
      s=s1-s2
      result['h']=int(s/3600)
      b1=int(s%3600)
      result['m']=int(b1/60)
      result['s']=int(b1%60)
      return result

def show(x):
      print(x['h'],':',x['m'],':',x['s'])

# hour=int(input('enter Hour:'))
# min=int(input('enter minute:'))
# second=int(input('enter second:'))
a={'h':5, 'm':51 , 's':25}
b={'h':2, 'm':52 , 's':35}

c=sum(a,b)
show(c)

d=subtraction(a,b)
show(d)