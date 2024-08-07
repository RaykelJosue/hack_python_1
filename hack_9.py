"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    input_list = [1, 2, 3]
    result = []
    i = 0
    while i < len(input_list):
        result.append(input_list[i])
        result.append('@')
        i += 1
    return result

if __name__ == "__main__":
    print(fn_hack_9())
 