order = input()
cup = ["s",0,0,"b"]

for o in order:
    if o == "A": cup[0],cup[1] = cup[1],cup[0]
    elif o == "B": cup[0],cup[2] = cup[2],cup[0]
    elif o == "C": cup[0],cup[3] = cup[3],cup[0]
    elif o == "D": cup[1],cup[2] = cup[2],cup[1]
    elif o == "E": cup[1],cup[3] = cup[3],cup[1]
    else: cup[2],cup[3] = cup[3],cup[2]
        
print(cup.index("s")+1)
print(cup.index("b")+1)