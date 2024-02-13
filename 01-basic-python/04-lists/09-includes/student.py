# Write your code here

def includes(xs, ys):
    if len(ys) == 0:
        return True
    for i in ys:
        if i in xs:
            return True
    return False