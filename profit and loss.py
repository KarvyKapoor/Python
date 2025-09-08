# Profit and Loss Calculator
# Taking inputs
cp=float(input("enter cost of product :"))
sp=float(input("enter selling price of product :"))

# Formula and Output
if(cp>sp):
    loss=cp-sp
    lossperc=(loss)*100/cp
    print("loss :",loss,"percentage :",lossperc)
else:
    profit=sp-cp
    profitperc=(profit)*100/cp
    print("profit :",profit,"/npercentage :",profitperc)