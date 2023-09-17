L= [14, 12, 21, 23, 56, 78, 45, 29, 28]
def returnSum(f, L):
    sum = 0
    for i in L:
        if f(i):
            sum+=i
    return sum
    
x= lambda x: x%2==0
y= lambda x: x%2!=0
z= lambda x: x%3==0
print(returnSum(x, L))
print(returnSum(y, L))
print(returnSum(z, L))