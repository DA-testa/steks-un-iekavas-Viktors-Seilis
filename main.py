# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):

        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))

        if next in ")]}":
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                return i+1
            opening_brackets_stack.pop()

    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    return "Success"


def main():
    type = input()

    if "F" in type:
        print("Files input option is not described in the task, therefore not implemented")

    elif "I" in type:
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)

    else:
        print("Invalid input type")

if __name__ == "__main__":
    main()