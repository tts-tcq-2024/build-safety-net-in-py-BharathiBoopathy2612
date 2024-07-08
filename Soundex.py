def char_to_soundex(c):
    c = c.upper()
    soundex_map = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return soundex_map.get(c, '0')

def start_soundex_key(name):
    initial_char = name[0].upper()
    return initial_char, char_to_soundex(initial_char)

def valid_code_addition(char, current_code, previous_code):
    return current_code != '0' and current_code != previous_code

def accumulate_soundex(name, soundex_key, previous_code):
    soundex_codes = [char_to_soundex(char) for char in name[1:] if valid_code_addition(char, char_to_soundex(char), previous_code)]
    return (soundex_key + ''.join(soundex_codes)[:3]).ljust(4, '0')

def pad_soundex_key(soundex_key):
    return soundex_key.ljust(4, '0')

def create_soundex(name):
    if not name:
        return ""

    soundex_key, previous_code = start_soundex_key(name)
    soundex_key = accumulate_soundex(name, soundex_key, previous_code)
    return pad_soundex_key(soundex_key)
