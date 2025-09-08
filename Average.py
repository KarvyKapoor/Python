# Finding Average
# Taking inputs
n=int(input("Enter total numbers of which you want average :"))
a=[]
for i in range(n):
    # Taking input
    num=int(input("Enter Number"))
    a.append(num)
sum=0
for i in range(n):
    sum=sum+a[i]

# Formula
avg=sum/n

# Output
print("avg",avg)