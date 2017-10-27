def qsort(i):
    if len(i) in (0, 1):
        return i

    p = i[-1]
    l = [x for x in i[:-1] if x <= p]
    r = [x for x in i[:-1] if x >  p]

    return qsort(l) + [p] + qsort(r)


q_list = [1,4,2,5,3]
