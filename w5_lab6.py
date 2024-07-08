def frq_count(d):
    d2 = {}
    for value in d.values():
        if value not in d2:
            d2[value] = 1
        else:
            d2[value] += 1
    return d2

d = {1: 10, 2: 10, 3: 40, 4: 20, 5: 70,6:80,9:40,10:20}
print(frq_count(d))
