import currency
print("select following number for currency(ex, enter 1 for usd)")
for i in range(21):
    print(i,".",currency.names[i])
fromc=int(input("enter current currency="))
toc=int(input("enter target currency="))
amt=float(input("enter your amount="))
cc=currency.names[fromc]
tc=currency.names[toc]
t= amt / currency.currency[cc]
n= t * currency.currency[tc]
print(amt,"",cc,"is equal to",n,"",tc)
