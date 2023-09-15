def check_permutation(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()

    if len(s1) != len(s2):
        return False

    hm = dict()
    for s in s1:
        if s in hm:
            hm[s] += 1
        else:
            hm[s] = 1
    for s in s2:
        if s in hm:
            hm[s] -= 1
        else:
            return False  # this letter not in s1 then we knew it not permutation of each other

    return all(value == 0 for value in hm.values())
