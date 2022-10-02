def compare(s, t):
    t = list(t)
    try:
        for elem in s:
            t.remove(elem)
    except ValueError:
        return False
    return not t
