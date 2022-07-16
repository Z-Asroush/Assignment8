def sum(x,y):
    result={}
    result['Re']=x['Re']+y['Re']
    result['Im']=x['Im']+y['Im']
    return result

def sub(x,y):
    result={}
    result['Re']=x['Re']-y['Re']
    result['Im']=x['Im']-y['Im']
    return result

def mul(x,y):
    result={}
    result['Re']=(x['Re']*y['Re'])-(x['Im']*y['Im'])
    result['Im']=(x['Re']*y['Im'])+(x['Im']*y['Re'])
    return result
    
a={'Re':-1, 'Im':5}
b={'Re':8, 'Im':24}

c=sum(a,b)
print('sum=',c)

d=sub(a,b)
print('subtraction=',d)

e=mul(a,b)
print('mul=',e)