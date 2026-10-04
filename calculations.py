

def calc(a):
    s = 0
    for x in a:
        s = s + x
    return s / len(a)


def mx(a):
    m = -float('inf')
    for x in a:
        m = max(m, x)
    return m


def countpos(a):
    c = 0
    for x in a:
        if x > 0:
            c = c + 1
    return c
