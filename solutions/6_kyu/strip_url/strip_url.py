"""Hrynevych Artemii
My solution for the Codewars "Strip URL" kata
https://www.codewars.com/kata/51646de80fd67f442c000013
"""

def strip_url_params(url, params_to_strip = []):
    """Function to strip url parameters.
    Removes the duplicates (keeps the first key)
    And removes the params in params_to_srip list.
    
    Arguments:
    url -- url to strip the parameters
    params_to_strip -- list of parameters name to remove
    """
    params_set = set()
    splitted = url.split('?')
    res = ''.join(splitted[0])
    params = (''.join(splitted[1:])).split('&')
    params_str = ''
    for par_val in params:
        if par_val == '':
            break
        par, val = par_val.split('=')
        if par not in params_set and par not in params_to_strip:
            params_set.add(par)
            if params_str:
                params_str = ''.join((params_str,'&',par,'=',val))
            else:
                params_str = ''.join((params_str,par,'=',val))
    if params_str:
        res = ''.join((res,'?',params_str))
    return res