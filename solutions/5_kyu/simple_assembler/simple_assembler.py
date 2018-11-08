"""Hrynevych Artemii
My solution of 'Simple assembler: part 1' kata
https://www.codewars.com/kata/simple-assembler-interpreter
"""


def mov(data_dict, i, r, d):
    if d in data_dict:
        data_dict[r] = data_dict[d]
    else:
        data_dict[r] = int(d)
    i += 1
    return i
        
def inc(data_dict, i, r):
    data_dict[r] += 1
    i += 1
    return i

def dec(data_dict, i, r):
    data_dict[r] -= 1
    i += 1
    return i

def jnz(data_dict, i, c, p):
    c = data_dict[c] if c in data_dict else c
    if int(c) != 0:
        i += int(p)
    else:
        i += 1
    return i

def simple_assembler(program):
    """Function to simulate simple assembler
    Arguments:
    program -- list of instructions.
    We assume that all instruction are correct.
    """
    i = 0    
    data_dict = dict()
    instructions = {'mov': mov, 'inc': inc, 'dec': dec, 'jnz': jnz}
    try:
        while True:
            statement = program[i].split()
            print(statement)
            instruction = statement[0]
            arguments = statement[1:]
            i = instructions[instruction](data_dict, i, *arguments)
    except IndexError:
        return data_dict