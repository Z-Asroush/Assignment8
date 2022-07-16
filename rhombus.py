n= int(input('enter number of rows?'))
m= 2*n-1
j=0
for i in range(m):
    if i<n:
        print((n-i-1)*' '+(2*i+1)*'*'+(n-i-1)*' ')

    if i>=n :
        j+=1
        print((i-n+1)*' '+(2*(i-2*j)+1)*'*'+(i-n+1)*' ')