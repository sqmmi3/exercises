# Write your code here

def median(ns):
    ns = sorted(ns)
    if len(ns) % 2 == 0:
        middle1 = ns[len(ns) // 2 - 1]
        middle2 = ns[len(ns) // 2]
        return (middle1 + middle2) / 2
    
    else:
        return ns[len(ns) // 2]
