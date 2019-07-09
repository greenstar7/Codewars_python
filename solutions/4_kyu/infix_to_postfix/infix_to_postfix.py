""" Hrynevych Artemii
My solution for 4 kyu 'Infix to postfix converter' kata.

"""
PRIORITIES = {
    '-': 0,
    '+': 0,
    '*': 1,
    '/': 1,
    '^': 2
}


def _split_to_list(string):
    res = []
    opened_brace = False
    i = 0
    N = len(string)
    temp = ''
    while i < N:
        char = string[i]
        if char == '(':
            temp = char
            opened_brace = True
        elif opened_brace:
            temp += char
            if char == ')':
                opened_brace = False
                res.append(temp)
                temp = ''
        else:
            res.append(char)
        i += 1
    return res


def _find_highest_priority(l):
    max_priority = -1
    max_idx = 0
    for i in range(len(l)):
        prior = PRIORITIES.get(l[i], -1)
        if prior > max_priority:
            max_priority = prior
            max_idx = i
    return max_idx


def _to_postfix(op_idx, l):
    if len(l) == 3:
        left_idx = 0
    else:
        left_idx = op_idx-1
    left = l.pop(left_idx)
    op = l.pop(left_idx)
    right = l.pop(left_idx)

    if left[0] == '(':
        left = to_postfix(left[1:-1])
    if right[0] == '(':
        right = to_postfix(right[1:-1])
    
    postfix_res = ''.join((left, right, op))
    l.insert(left_idx, postfix_res)


def to_postfix(infix):
    """ Convert infix to postfix

    """
    splitted = _split_to_list(infix)
    while len(splitted) != 1:
        op_idx = _find_highest_priority(splitted)
        _to_postfix(op_idx, splitted)
    return splitted.pop()
