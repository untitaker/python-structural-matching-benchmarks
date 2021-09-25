def generate_pattern_matching(i):
    code = """
def pattern_matching(x):

    match x:
"""

    for _ in range(i):
        code += """
        case int():
            return int
"""

    namespace = {}
    exec(code, namespace)

    return namespace['pattern_matching']


def generate_ifelse(i):
    code = """
def ifelse(x):
"""

    for _ in range(i):
        code += """
    if isinstance(x, int):
        return int
"""

    namespace = {}
    exec(code, namespace)

    return namespace['ifelse']



pattern_matching1 = generate_pattern_matching(1)
pattern_matching100 = generate_pattern_matching(100)
pattern_matching1000 = generate_pattern_matching(1000)

ifelse1 = generate_ifelse(1)
ifelse100 = generate_ifelse(100)
ifelse1000 = generate_ifelse(1000)
