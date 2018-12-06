"""Hrynevych Artemii
My solution for 5 kyu 'Molecule to atoms' kata
https://www.codewars.com/kata/molecule-to-atoms/
A little bit complicated version, because it assumes, that
1) nested brackets can be of the same type:
    parse_molecules('K4[ON(SO3)2]2') and parse_molecules('K4(ON(SO3)2)2')
    are the same.
2) numbers after the elemen may consist of more than 1 digit
"""

START_BRACKETS = '(<[{'
END_BRACKETS = '}]>)'
BRACKETS = START_BRACKETS+END_BRACKETS
END_BRACKET_PAIR = {
    '}': '{',
    ']': '[',
    ')': '(',
    '>': '<'
}

def tokenize(formula):
    """Tokenizer to get reversed list of elements from formula:
    numbers(not single digits, but whole numbers), elements and brackets.
    """
    res = []
    temp = ''
    for char in formula:
        if char in BRACKETS:
            if temp:
                res.append(temp)
            temp = ''
            res.append(char)
        elif char.isupper():
            if temp:
                res.append(temp)
            temp = char
        elif char.islower():
            temp += char
        elif char.isdigit():
            if temp and not temp.isdigit():
                res.append(temp)
                temp = ''
            temp += char
    if temp:
        res.append(temp)
    return res[::-1]

def get_bracket_end(start, end, expression):
    """Returns index of the closing bracket of the bracket
    given at the start position
    """
    parity = 0
    bracket = expression[start]
    for i in range(start+1, end):
        if expression[i] == END_BRACKET_PAIR[bracket]:
            if parity == 0:
                return i
            else:
                parity -= 1
        elif expression[i] == bracket:
            parity += 1

def parse_molecule(formula):
    """Function to get dict of atoms used in formula given by string.
    Gets tokens from tokenizer and passes it to the hidden parser function
    """
    tokens = tokenize(formula)
    return __parse_molecule(tokens)

def __parse_molecule(tokens):
    """Hiddent function to get dict of atoms used in formula given by string.
    If closing bracket is found it recursively calls function to get dict of
    atoms from formula in the braces."""
    res = dict()
    N_tokens = len(tokens)
    i = 0
    while i < N_tokens:
        token = tokens[i]
        
        if token.isdigit():
            next_el = tokens[i+1]
            if next_el in END_BRACKETS:
                bracket_start = i+1
                bracket_end = get_bracket_end(bracket_start, N_tokens, tokens)
                temp_dict = __parse_molecule(tokens[bracket_start+1:bracket_end])
                for k in temp_dict:
                    if k in res:
                        res[k] += temp_dict[k]*int(token)
                    else:
                        res[k] = temp_dict[k]*int(token)
                # advance to the next token right after the end of the bracket section
                i = bracket_end+1
            else:
                if next_el in res:
                    res[next_el] += int(token)
                else:
                    res[next_el] = int(token)
                # advance to the next token right after the taken atom    
                i += 2
        elif token in END_BRACKETS:
                bracket_start = i
                bracket_end = get_bracket_end(bracket_start, N_tokens, tokens)
                temp_dict = __parse_molecule(tokens[bracket_start+1:bracket_end])
                for k in temp_dict:
                    if k in res:
                        res[k] += temp_dict[k]
                    else:
                        res[k] = temp_dict[k]
                # advance to the next token right after the end of the bracket section        
                i = bracket_end+1
        elif token.isalpha():
            if token in res:
                res[token] += 1
            else:
                res[token] = 1
            # advance to the next token
            i += 1
    return res