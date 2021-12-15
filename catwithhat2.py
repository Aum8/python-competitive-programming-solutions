ch={}
for i in range(1,101):
    ch[i]=False
for i in range(1,101):
    for cat,hat in ch.items():
        if cat%i==0:
            if ch[cat]:
                ch[cat]=False
            else: ch[cat]=True
for cat,hat in ch.items():
    if ch[cat]:
        print(cat)
