'''One-pass multi-string substitution with function dispatch'''

import re

# https://stackoverflow.com/a/15175239
def dict_replace(text, replacements):
    '''
    replacements is a dictionary which maps
    strings to strings
    and
    simple uncompiled regex (no "|" or other fancy stuff) to functions
    '''

    joined = []
    func_dispatch = {}

    for k, v in replacements.items():
        if not isinstance(v, str):
            func_dispatch[re.compile(k)] = v
            joined.append(k)
        else:
            joined.append(re.escape(k))

    regex = re.compile('|'.join(joined))

    def substitute(mo):

        s = mo.string[mo.start():mo.end()]

        if s in replacements:
            return(replacements[s])
        for r, f in func_dispatch.items():
            if r.match(s):
                return f(s)

    # For each match, look-up corresponding value in dictionary
    return regex.sub(substitute, text)
