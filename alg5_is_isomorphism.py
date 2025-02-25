"""
    is isomorphism

"""

def is_isomorphism(s, t):
    dict_value = {}
    set_value = set()

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i] not in dict_value:
            dict_value[s[i]] = t[i]
            set_value.add(t[i])
        else:
            if dict_value[s[i]] != t[i]:
                return False
    print(dict_value)
    print(set_value)

    return True



print(is_isomorphism('foo', 'bee'))