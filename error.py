class a(Exception):
    pass
for c in [a]:
    try: raise c
    except a: print("error")
