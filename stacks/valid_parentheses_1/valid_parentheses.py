parens = {'(': ')', '[': ']', '{': '}'}


def is_valid_parentheses(s: str) -> bool:
    if len(s) == 0:
        return True

    stack = []
    for i in range(len(s)):
        if s[i] in parens:
            stack.append(s[i])
        else:
            left_bracket = stack.pop()
            correct_bracket = parens[left_bracket]
            if s[i] != correct_bracket:
                return False
    return len(stack) == 0
