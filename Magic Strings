def prefix(x):
    l = len(x)
    pre = []
    for i in range(l+1):
        a = x[0:i]
        if len(a) > 0:
            pre.append(a)
    return pre

def magic(x):
    c1,c2,c3,c4,c5 = 0,0,0,0,0
    #Check whether 1 and 0 are equal
    for i in range(len(x)):
        if x[i] == "0":
            c1 += 1
        else:
            c2 += 1
    if c1 == c2:
        #Check for prefixes
        a = prefix(x)
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == "0":
                    c3 += 1
                else:
                    c4 += 1
            if c3 <= c4:
                c5 += 1
        if c5 != 0:
            return "Magic String"
        else:
            return "Not Magic String2"
    else:
        return "Not Magic String1"
            
def main():
    s = input()
    print(magic(s))

if __name__ == "__main__":
    main()
