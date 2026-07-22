import random
coin_values=['Head','Tail']
hcount=0
tcount=0
for num in range(100):
    result=random.choice(coin_values)
    if result=="Head":
        hcount=hcount+1
    elif result=="Tail":
        tcount=tcount+1


print("Total Head Sides Count:",hcount)
print("Total Tail Sides Count:",tcount)