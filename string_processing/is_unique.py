def is_unique(input_str):
    hm = dict()
    for s in input_str:
        if s in hm:
            return False
        else:
            hm[s] = 1
    for value in hm.values():
        if value > 1:
            return False
    return True


input_str = "non"
print(is_unique(input_str))
