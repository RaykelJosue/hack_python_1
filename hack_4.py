"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    text = "fooziman"
    return text[:-1] + text[-1].upper()

if __name__ == "__main__":
    print(fn_hack_4())

