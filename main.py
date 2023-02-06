# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            bracket = Bracket(next,i+1)
            opening_brackets_stack.append(next)
            # Process opening bracket, write your code here
            pass

        if next in ")]}":
            bracket = Bracket(next,i+1)
            if len(opening_brackets_stack) > 0 :
                last_bracket = opening_brackets_stack[-1]
                answer = are_matching(last_bracket, next)
                if (answer == False) : return bracket
                opening_brackets_stack.pop()
            else: 
                return bracket
            pass
    return "Success"

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)
    # Printing answer, write your code here


if __name__ == "__main__":
    main()
