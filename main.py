# python3
# 221RDB265
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next,i+1))
            # Process opening bracket, write your code here
            pass

        if next in ")]}":
            bracket = Bracket(next,i+1)
            if len(opening_brackets_stack) > 0 :
                last_bracket = opening_brackets_stack[-1]
                answer = are_matching(last_bracket.char, next)
                if (answer == False) : return i+1
                opening_brackets_stack.pop()
            else: 
                return i+1
            pass
        
    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[0].position
    else: 
        return "Success"

def main():
    mode = input()
    print(mode)
    text = input()
    print(text)
    if (mode == "I"):
        if len(text) > 10**5 : return
        mismatch = find_mismatch(text)
        print(mismatch)
        # Printing answer, write your code here


if __name__ == "__main__":
    main()
