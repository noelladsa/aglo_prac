import random


def exchange(a_index, b_index, array):
    if a_index != b_index:
            temp = array[a_index]
            array[a_index] = array[b_index]
            array[b_index] = temp


def selection_sort(array):
    print "SELECTION", array
    for index in range(len(array)):
        j = index + 1
        small_index = index
        for j in range(j, len(array)):
            if array[small_index] > array[j]:
                small_index = j
        exchange(small_index, index, array)
    return array


def insertion_sort(array, delta_checks=1):
    print "INSERTION", array
    index = 0
    while(index < len(array)):
        check = index
        while check > 0 and array[check - delta_checks] > array[check]:
            exchange(check - delta_checks, check, array)
            check -= delta_checks
        index += delta_checks
    return array


def shell_sort(array):
    print "SHELL", array
    h = 1
    while h < (len(array)/3):
        h = 3*h + 1
    print "Ideal h", h
    while h >= 1:
        insertion_sort(array, h)
        print array, h
        h = h/3
    return array


def shuffling(array):
    print "Shuffling"
    for i in range(1, len(array)):
        rand = random.randint(0, i-1)
        exchange(rand, i, array)
    return array


def quick_sort(array, lo, hi):
    if hi <= lo:
        return
    pivot_index = lo
    old_lo = lo
    old_hi = hi
    pivot = array[pivot_index]
    while (lo < hi):
        while(array[lo] <= pivot and lo < old_hi):
            lo += 1

        while (array[hi] > pivot and hi > old_lo):
            hi -= 1

        if lo < hi:
            exchange(lo, hi, array)
    exchange(pivot_index, hi, array)
    quick_sort(array, old_lo, hi-1)
    quick_sort(array, hi+1, old_hi)


def quick_sort_part(array, lo, hi):
    if hi <= lo:
        return

    lt = lo
    i = lo + 1
    gt = hi

    while i <= gt:
        if array[lt] > array[i]:
            exchange(lt, i, array)
            lt += 1
            i += 1

        elif array[lt] < array[i]:
            exchange(gt, i, array)
            gt -= 1

        elif array[lt] == array[i]:
            i += 1

    quick_sort_part(array, lo, lt-1)
    quick_sort_part(array, gt + 1, hi)

    return array


def merge_sort(array):
    print "Merge Sort", array
    aux = [i for i in array]
    div_sort(array, aux, 0, len(array)-1)
    return array


def div_sort(array, aux, lo, hi):
    if hi <= lo:
        return
    mid = lo + int((hi - lo)/2)
    div_sort(array, aux, lo, mid)
    div_sort(array, aux, mid + 1, hi)
    merge(array, aux, lo, hi, mid)
    print "Merged Mid,lo,hi", lo, hi, array


def merge_sort_iter(array):
    print "Merging iteratively"
    aux = [i for i in array]
    size = 1
    while size < len(array):
        for j in range(0, len(array), 2 * size):
            hi = j + size + (size-1)
            hi = hi if hi < len(array) else len(array) - 1
            merge(array, aux, j, hi, j + size - 1)
        size = 2 * size
    return array


def merge(array, aux, lo, hi, mid):
    k = lo
    l = mid + 1
    for i in range(len(array)):
        aux[i] = array[i]

    for i in range(lo, hi+1):
        if k > mid:
            array[i] = aux[l]
            l += 1
        elif l > hi:
            array[i] = aux[k]
            k += 1
        else:
            if aux[k] < aux[l]:
                array[i] = aux[k]
                k += 1
            else:
                array[i] = aux[l]
                l += 1
    return array


if __name__ == "__main__":
    print selection_sort([3, 46, 2, 99, -1, 2, 32, -18, 11, 45, 43])
    print insertion_sort([3, 46, 2, 99, -1, 2, 32, -18, 11, 45, 43])
    print shell_sort([3, 46, 2, 99, -1, 2, 32, -18, 11, 45, 43, 3,
                      46, 2, 99, -1, 2, 32, -18, 11, 45, 43])
    print shuffling([3, 46, 2, 99, -1, 2, 32, -18, 11, 45, 43])
    print shuffling([3, 46, 2, 99, -1, 2, 32, -18, 11, 45, 43])
    print merge_sort([3, 46, 2, 99, -1, 2, 32, -18, 11, 45, 43])
    print merge_sort_iter([3, 46, 2, 99, -1, 2, 32, -18, 11, 45, 43])
    print quick_sort([3, 46, 2, 99, -1, 2, 32, -18, 11, 45, 43], 0, 9)
    print quick_sort_part([3, 46, 2, 99, -1, 2, 32, -18, 11, 45, 43], 0, 10)
