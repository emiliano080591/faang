def build_string(string: str) -> str:
    build_array = []
    for p in range(len(string)):
        if string[p] != '#':
            build_array.append(string[p])
        else:
            if len(build_array) > 0:
                build_array.pop()

    return build_array


def back_space_compare(S: str, T: str) -> bool:
    final_S = build_string(S)
    final_T = build_string(T)

    if len(final_S) != len(final_T):
        return False
    else:
        for p in range(len(final_S)):
            if final_S[p] != final_T[p]:
                return False
    return True


def back_space_compare_opt(S: str, T: str) -> bool:
    def skip_deleted(string: str, idx: int, to_delete: int) -> int:
        """Skips characters that need to be deleted, by shifting index."""
        while to_delete > 0 and idx > -1:
            idx -= 1
            to_delete -= 1
            if string[idx] == '#':
                to_delete += 2
        return idx

    string1, string2 = S, T
    idx1, idx2 = len(string1) - 1, len(string2) - 1
    while idx1 >= 0 or idx2 >= 0:
        if (string1[idx1] == '#' and idx1 >= 0 or string2[idx2] == '#' and idx2 >= 0):
            # need to 'delete' characters
            # while we have not fully traversed the string
            if string1[idx1] == '#':
                idx1 = skip_deleted(string1, idx1, 2)
            if string2[idx2] == '#':
                idx2 = skip_deleted(string2, idx2, 2)
            if idx1 < 0 and idx2 < 0:
                # both string are empty after 'deletions'
                return True
        else:
            # Now characters are not '#', so we can compare them
            if idx1 < 0 and idx2 >= 0 or idx1 >= 0 and idx2 < 0:
                # If one string is "deleted" and other is not, then
                # they are not equal
                return False
            if string1[idx1] != string2[idx2]:
                return False
            idx1 -= 1
            idx2 -= 1
    return True
