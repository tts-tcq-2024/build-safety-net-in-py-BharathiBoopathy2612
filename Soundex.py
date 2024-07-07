def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters


def generate_soundex(name):
    if not name:
        return ""

    # Start with the first letter (capitalized)
    soundex = name[0].upper()
    prev_code = get_soundex_code(soundex)

    for char in name[1:]:
        code = get_soundex_code(char)
        if code != '0' and code != prev_code:
            soundex += code
            prev_code = code
        if len(soundex) == 4:
            break

    # Pad with zeros if necessary
    soundex = soundex.ljust(4, '0')

    return soundex


def test_generate_soundex():
    test_cases = [
        {"name": "Smith", "expected": "S530"},
        {"name": "Babbitt", "expected": "B130"},
        {"name": "Jackson", "expected": "J250"},
        {"name": "Li", "expected": "L000"},
        {"name": "O'Brien", "expected": "O165"},
        {"name": "Ellis", "expected": "E420"},
        {"name": "Knight", "expected": "K523"},
    ]

    for i, test in enumerate(test_cases, start=1):
        result = generate_soundex(test["name"])
        assert result == test["expected"], f"Test case {i} failed: {test['name']} -> {result} (expected {test['expected']})"
        print(f"Test case {i} passed: {test['name']} -> {result}")

# Run the tests
test_generate_soundex()
