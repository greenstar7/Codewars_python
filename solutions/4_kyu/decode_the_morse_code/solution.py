""" Artemii Hrynevych - 'Decode the Morse code, advanced' kata solution """

O = {
    1: '.',
    3: '-'
}
Z = {
    1: ' ',
    3: '   ',
    7: '       '
}

def decodeBits(bits):
    print(bits)
    res = ''
    temp = ''
    splitted = []
    for char in bits.strip('0'):
        if temp == '' or char == temp[-1]:
            temp += char
        elif char != temp[-1]:
            splitted.append(temp)
            temp = char
    splitted.append(temp)
    unit_length = len(min(splitted, key=lambda x: len(x)))
    for el in splitted:
        el_len = len(el) / unit_length
        if '0' in el:
            res += Z[el_len]
        else:
            res += O[el_len]
    return res

def decodeMorse(morseCode):
    morseCode = morseCode.split(Z[7])
    res = ' '.join([''.join([MORSE_CODE[x.replace(' ', '')] for x in w.split(Z[3])]) for w in morseCode])
    return res
