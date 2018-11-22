def partitions(number, k=None, cache={(0,0): 1}):
    '''define a function which returns the number of integer partitions of n'''
    if number < 0: return 0
    if k is None: k = number
    if k >= 0 and number >= 0:
        try:
            return cache[number,k]
        except KeyError:
            pass
    if number <= 1 or k == 1:
        return 1
    cache[number, k] = partitions(number, k-1) + partitions(number-k, k);
    return cache[number, k]