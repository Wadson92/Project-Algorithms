def is_palindrome_recursive(word, low_index, high_index):
    try:
        if word == "":
            raise TypeError
        if high_index == 0:
            return True
        else:
            low_and_high = word[low_index] == word[high_index]
            func = is_palindrome_recursive(word, low_index + 1, high_index - 1)
            return low_and_high and func
    except TypeError:
        return False
