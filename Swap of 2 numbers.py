a=int(input("Enter number :"))
b=int(input("Enter number :"))
if(a>b or b>a):
    a,b=b,a
print(a,b)