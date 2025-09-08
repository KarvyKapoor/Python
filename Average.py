n=int(input("Enter total numbers of which you want average :"))
a=[]
for i in range(n):
    num=int(input("Enter Number"))
    a.append(num)
sum=0
for i in range(n):
    sum=sum+a[i]
avg=sum/n
print("avg",avg)