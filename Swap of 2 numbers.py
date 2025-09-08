# Swapping without 3rd Variable
# Taking inputs
a=int(input("Enter number :"))
b=int(input("Enter number :"))

# Formula
if(a>b or b>a):
    a,b=b,a

# Output
print(a,b)