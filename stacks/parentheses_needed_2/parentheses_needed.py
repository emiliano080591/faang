def min_remove_to_make_valid(string: str) -> str:
    # convert string into array
    res = list(string)

    # initialize stack data model using array
    stack = []

    for i in range(len(res)):
        # check if we see the left bracket
        if (res[i] == '('):
            # store, bracket in the stack data model
            stack.append(i)

        # check if we see the right bracket and stack has value inside of it
        elif (res[i] == ')' and len(stack)):
            # remove, the last bracket from stack
            stack.pop()

        # check if we see the right bracket
        elif (res[i] == ')'):
            # update the value of that character to be empty string
            res[i] = ''

    # if stack has value inside of data model
    while (len(stack)):
        # remove the last value from the stack
        curIdx = stack.pop()
        # update value of current index/character to empty string
        res[curIdx] = ''

    # convert array into string
    return ''.join(res)
