"""
text: "fooziman" output => "FOOZIMAN"
"""

def fn_hack_1():
    text = "fooziman"
    return text.upper()

if __name__ == "__main__":
    print(fn_hack_1())