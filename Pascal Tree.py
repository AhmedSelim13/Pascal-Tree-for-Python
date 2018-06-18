limit = input("To what step you want to learn Pascal Tree: ")
elist = [1]
print(elist)
elist.append(1)
for z in range(x):
    print(elist)
    y = 0
    alist = []
    while len(alist) + 1 < len(elist):
        b = elist[y] + elist[y + 1]
        alist.append(b)
        y = y + 1
    alist.append(1)
    alist.insert(0,1)
    elist = alist.copy()
