def cal(a,b,c):
    if b == "+":
        print(f"{a} + {c} = {a+c}")
    elif b == "-":
        print(f"{a} - {c} = {a-c}")
    elif b == "*":
        print(f"{a} * {c} = {a*c}")
    elif b == "/":
        print(f"{a} / {c} = {a/c}")
    else:
        print("Input Invalid")

cal(6,"+")