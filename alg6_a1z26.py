"""
    a1z26
    atefe <=> [5, 24, 9, 10, 9]

"""

def encode(plain):
    return [ord(elm) - 92 for elm in plain]


def decode(encode):
    return "".join((chr(elm + 92 ) for elm in encode))


print(encode('atefe'))
print(decode([5, 24, 9, 10, 9]))

