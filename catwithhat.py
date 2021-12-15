catwithhat=[]
for i in range(1,101):
    for cat in range(1,101):
        if cat%i==0:
            if cat in catwithhat:
                catwithhat.remove(cat)
            else: catwithhat.append(cat)
print(catwithhat)
