def sort(array):
    aux = array[:]
    sort_half(array, aux, 0, len(array) - 1)


def sort_half(array, aux, start, end):
    if start >= end:
        return
    middle = (start + end) // 2

    sort_half(array, aux, start, middle)
    sort_half(array, aux, middle + 1, end)

    merge(array, aux, start, end)


def merge(array, aux, start, end):
    left = start
    left_end = (start + end) // 2

    right = left_end + 1
    right_end = end

    for position in range(start, end + 1):
        if left > left_end:
            aux[position] = array[right]
            right += 1

        elif right > right_end:
            aux[position] = array[left]
            left += 1

        elif array[left] < array[right]:
            aux[position] = array[left]
            left += 1

        else:
            aux[position] = array[right]
            right += 1

    for k in range(start, end + 1):
        array[k] = aux[k]


def is_anagram(first_string, second_string):
    try:
        pass
    except TypeError:
        return False
