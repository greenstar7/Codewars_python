from collections import Counter


def mix(s1, s2):
    s1 = ''.join(((char for char in s1 if char.islower())))
    s2 = ''.join(((char for char in s2 if char.islower())))
    s1_counter = Counter(s1)
    s2_counter = Counter(s2)
    res_list = []
    for key, key_s1_count in s1_counter.items():
        key_s2_count = s2_counter.get(key, None)
        if key_s2_count:
            if key_s1_count > key_s2_count:
                which_has_max = '1'
                max_count = key_s1_count
            elif key_s1_count < key_s2_count:
                which_has_max = '2'
                max_count = key_s2_count
            else:
                which_has_max = '='
                max_count = key_s1_count
            del s2_counter[key]
        else:
            which_has_max = '1'
            max_count = key_s1_count
        if max_count != 1:
            res_list.append('{}:{}'.format(which_has_max, key*max_count))
    for key, count in s2_counter.items():
        if count != 1:
            res_list.append('2:{}'.format(key*count))
    res_list = sorted(res_list)
    res_list = sorted(res_list, key=lambda x: len(x), reverse=True)
    return '/'.join(res_list)
