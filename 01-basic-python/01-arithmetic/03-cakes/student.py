# Write your code here

def cakes(eggs, butter, flour):
    amt1 = eggs // 5
    amt2 = butter // 250
    amt3 = flour // 250

    return min(amt1, amt2, amt3)