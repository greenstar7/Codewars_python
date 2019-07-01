""" Artemii Hrynevych
 My solution for 4 Kyu kata 'Next smaller number with the same digits'

"""


def next_bigger(number: int) -> int:
    str_number = str(number)
    answer = -1
    # if only one digit or digits already sorted descending
    # it is already the smallest
    if (len(str_number) != 1 and 
            str_number != ''.join(sorted(str_number, reverse=True))):
        # going from second-to-last to the left and looking for number
        # that is less then the right one
        for i in range(len(str_number)-2, -1, -1):
            if str_number[i] < str_number[i+1]:
                list_number = list(str_number)
                # left size stays as it is
                left = list_number[:i]
                el = str_number[i]
                # finding min number from right side that is greater
                # then our number
                temp = [x for x in list_number[i+1:] if x > el]
                right_min = min(temp)
                # swapping them
                list_number[i] = right_min
                min_index = str_number.rfind(right_min)
                list_number[min_index] = el
                # sort right side ascending
                list_number[i+1:] = sorted(list_number[i+1:])
                answer = int(''.join(list_number))
                break
    return answer

