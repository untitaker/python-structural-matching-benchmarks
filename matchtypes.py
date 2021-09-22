def pattern_matching(x):
    match x:
        case int():
            return int
        case str():
            return str
        case bool():
            return bool
        case list():
            return list
        case dict():
            return dict

def ifelse(x):
    if isinstance(x, int):
        return int
    elif isinstance(x, str):
        return str
    elif isinstance(x, bool):
        return bool
    elif isinstance(x, list):
        return list
    elif isinstance(x, dict):
        return dict


assert pattern_matching(42) == ifelse(42) == int
assert pattern_matching({}) == ifelse({}) == dict
