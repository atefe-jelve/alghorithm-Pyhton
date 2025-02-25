"""
 'limit'
"""

def limit(l, min=None, max=None):
    check_min = lambda val:  True if min is None else( val >= min )
    check_max = lambda val:  True if max is None else( val <= max )

    return [val for val in l if check_min(val) and check_max(val)]

# print(limit([1,2,3,4,5],3, 3))



