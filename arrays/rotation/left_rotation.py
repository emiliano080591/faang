def rotLeft(a: [int], rot: int) -> [int]:
    rot = rot % len(a)
    l1 = a[0:rot]
    l2 = a[rot:len(a)]

    final = l2 + l1

    return final
