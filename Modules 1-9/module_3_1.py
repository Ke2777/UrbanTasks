calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string: str):
    count_calls()
    result = (len(string), string.upper(), string.lower())
    return result


def is_contains(string: str, list_to_search: list):
    count_calls()
    for i in list_to_search:
        if i.lower() == string.lower():
            return True
    return False


print(string_info('ASdJNLZJDFNKkjmasdfkolgjm:LKSDMfg;lsdgm2384075'))
print(string_info('ASdJNLZJDsdgm2384075'))
print(string_info('ASdJNLZJmasdfkolgjm:m2384075'))
print(string_info('ASdJNLZJDFNKkjmaLKSDMfg;lsdgm'))
print(is_contains('Привет', ('Привет', 'мир')))
print(is_contains('Привет', ('привет', 'мир')))
print(is_contains('Привет', ('пока', 'мир')))
print(calls)
