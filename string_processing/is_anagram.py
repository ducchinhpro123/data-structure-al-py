def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    hm = dict()
    for i in s1:
        if i in hm:
            hm[i] += 1
        else:
            hm[i] = 1
    for i in s2:
        if i in hm:
            hm[i] -= 1
        else:
            hm[i] = 1
    for key in hm:
        if hm[key] != 0:
            return False
    return True