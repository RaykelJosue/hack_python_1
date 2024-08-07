"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    text = "fooziman"
    replacements = {
        'f': 'F',
        'o': '0',
        'i': '1',
        'a': '@',
        'z': 'Z',
        'm': 'M',
        'n': 'N'
    }
    
    result = []
    for char in text:
        if char in replacements:
            result.append(replacements[char])
        else:
            result.append(char)
    return result

if __name__ == "__main__":
    print(fn_hack_10())