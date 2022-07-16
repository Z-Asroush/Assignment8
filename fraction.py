def sum(x,y):
      result={}
      result['s']=x['s']*y['m']+y['s']*x['m']
      result['m']=x['m']*y['m']
      return result

def mul(x,y):
    result={}
    result['s']=x['s']*y['s']
    result['m']=x['m']*y['m']
    return result

def subtraction(x,y):
    result={}
    result['s']=x['s']*y['m']-y['s']*x['m']
    result['m']=x['m']*y['m']
    return result

def division(x,y):
    result={}
    result['s']=x['s']*y['m']
    result['m']=x['m']*y['s']
    return result

def show(x):
    print(x['s'],'/',x['m'])

a={'s':2, 'm':3}
b={'s':5, 'm':4}

c=sum(a,b)
show(c)

d=mul(a,b)
show(d)

e=subtraction(a,b)
show(e)

f=division(a,b)
show(f)