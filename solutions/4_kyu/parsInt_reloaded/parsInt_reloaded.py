""" Hrynevych Artemii
My solution for parseInt() reloaded kata
https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5
"""

numbers = {word: value for value, word in enumerate('''zero one two
three four five six seven eight nine ten eleven twelve thirteen
fourteen fifteen sixteen seventeen eighteen nineteen'''.split())}

numbers.update({word: 10 * value for value, word in enumerate('''twenty
thirty forty fifty sixty seventy eighty ninety'''.split(), start=2)})

muls = {'hundred': 100, 'thousand': 1000, 'million':10**6}

def parse_int(string):
    num = [0]
    # getting rid of 'and', '-' and storing the words in list
    string = [subword for word in string.lower().split() 
              for subword in word.split('-') if word != 'and']
    for word in string:
        if word in numbers:
            num.append(num.pop() + numbers[word])
        else:
            s = 0
            while len(num) > 0 and num[-1] < muls[word]:
                s += num.pop()
            num.append(s * muls[word])
            num.append(0)
    num = sum(num)
    return num