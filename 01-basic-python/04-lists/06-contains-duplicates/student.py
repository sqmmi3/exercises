# Write your code here

def contains_duplicates(xs):
    xs2 = []
    for i in xs:
        if i in xs2:
            return True
        xs2.append(i)
    return False