def find_uniq(arr):
    # do the magic
    a, b, c = [set(arr[i].strip().lower()) for i in range(3)]
    if a == b or a == c:
        typicals = a
    else:
        typicals = b
    for string in arr:
        if set(string.strip().lower()) != typicals:
            return string

