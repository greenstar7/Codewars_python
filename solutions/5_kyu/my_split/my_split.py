def my_very_own_split(string, delimiter = None):
    if delimiter == '':
        raise
    res = ''
    n = len(string)
    if delimiter is None:
        for i in range(n):
            if string[i].isspace():
                if res:
                    yield res
                    res = ''
            else:
                res = ''.join((res,string[i]))
    else:       
        i = 0
        n_del = len(delimiter)
        while i < n:
            j = i
            k = 0
            while j < n and k < n_del:
                if string[j] != delimiter[k]:
                    break
                j += 1
                k += 1
            if k == n_del:
                i += k
                yield res
                res = ''
            else:
                res += string[i]
                i += 1
    yield res