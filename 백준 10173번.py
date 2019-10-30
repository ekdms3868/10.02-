nemo=[['n', 'N'], ['e', 'E'], ['m', 'M'], ['o', 'O']]
while(True):
    a=input()
    if a=="EOI":
        break
    b=0
    for i in range(0, len(a)):
        if a[i] in nemo[b]:
            b=b+1
            if b==4:
                print("Found")
                break
        else:
            b=0
    else:
        print("Missing")