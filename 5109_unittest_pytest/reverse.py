def reverse(s):
    if type(s) != str:
        raise TypeError(f'Необходим str, а получено {type(s)}')
    return s[::-1]



