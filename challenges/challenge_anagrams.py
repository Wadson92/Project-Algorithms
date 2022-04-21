def sort(array):
    return sort_half(array, 0, len(array) - 1)


def sort_half(array, start, end):
    if start < end:
        middle = (start + end) // 2

        sort_half(array, start, middle)
        sort_half(array, middle + 1, end)

        merge(array, start, middle, end)


def merge(array, start, middle, end):
    aux = array[:]
    left = start
    left_end = middle + 1
    arr = start

    while arr <= end:
        if left > left_end:
            array[arr] = aux[left_end]
            left_end += 1

        elif left_end > end:
            array[arr] = aux[left]
            left += 1

        elif aux[left] <= aux[left_end]:
            array[arr] = aux[left]
            left += 1

        else:
            array[arr] = aux[left_end]
            left_end += 1

        arr += 1


def is_anagram(first_string, second_string):
    try:
        print(sort([2, 3, 9, 4]))
        print(sort(second_string))
        if first_string != second_string:
            raise TypeError
        if first_string in second_string:
            return True
    except TypeError:
        return False
