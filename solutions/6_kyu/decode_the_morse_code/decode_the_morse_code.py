"""Hrynevych Artemii
My solution of 'Decode the Morse code' kata
https://www.codewars.com/kata/decode-the-morse-code/
"""

# not full dict for morse codes for english alphabet
# + special polish chars, numbers and some punctuation marks
MORSE_CODE = {
    'a':'._', 'b':'_...', 'c':'_._.',
    'd':'_..','e':'.','f':'.._.','g':'__.',
    'h':'....','i':'..','j':'.___','k':'._..',
    'l':'._..','m':'__','n':'_.','o':'___',
    'p':'.__.','q':'__._','r':'._.','s':'...',
    't':'_','u':'.._','v':'..._','w':'.__',
    'x':'_.._','y':'_.__','z':'__..','ń':'__.__',
    'ó':'___.','ś':'..._...','ż':'__.._.',
    'ź':'__.._','ę':'.._..','ą':'._._',
    'ł':'._.._','1':'.____','2':'..___','3':'...__',
    '4':'...._','5':'.....','6':'_....','7':'__...',
    '8':'___..','9':'____.','0':'_____',
    '.':'._._._',',':'__..__','\'':'.____.',
    '"':'._.._.','_':'..__._',':':'___...',
    ';':'_._._.','?':'..__..','!':'_._.__',
    ' ':' '
}

def decodeMorse(morse_code):
    """FUnction to decode simple Morse codes.
    Assumes that somewhere in the script is available
    dict MORSE_CODE which contains {morse_code: char value}
    for all needed morse codes.
    
    Arguments:
    morse_code -- string of dots, dashes and whitespaces,
    which represents the coded message.
    """
    res = list()
    # striping the whistespaces from the start and the end
    # splitting it by 3 whitespaces to get the list of words
    for word in morse_code.strip().split('   '):
        # adding decoded word to the result list
        res.append(''.join(MORSE_CODE[symbol] for symbol in word.split()))
    return ' '.join(res)