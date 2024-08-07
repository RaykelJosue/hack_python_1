"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    text = "fooziman"
    replacements = {
        'o': '0',
        'i': '1',
        'a': '@'
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text

if __name__ == "__main__":
    print(fn_hack_5())