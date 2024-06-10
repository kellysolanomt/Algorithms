def partition(array, left, right):
    ## Primer elemento como pivote
    # pivot = array[left]

    ## Último elemento como pivote
    # array[left], array[right] = array[right], array[left]
    # pivot = array[left]

    ## Median of three pivote
    pivot = array[left]
    mid = (right + left) // 2
    sort = [array[left], array[mid], array[right]]
    sort.sort()
    if array[right] == sort[1]:
        array[right], array[left] = array[left], array[right]
        pivot = array[left]
    elif array[mid] == sort[1]:
        array[mid], array[left] = array[left], array[mid]
        pivot = array[left]



    i = left + 1
    for j in range(left + 1, right+1):
        if array[j] < pivot:
            array[j],array[i] = array[i], array[j]
            i += 1
    array[left],array[i-1] = array[i-1],array[left]

    return i-1

def quick_sort(array, left, right):
    num_compa = right - left
    if left < right:
        pivot = partition(array, left, right)
        compa_l = quick_sort(array, left, pivot-1)
        compa_r = quick_sort(array, pivot + 1, right)
        num_compa += compa_l + compa_r
        return num_compa
    else:
        return 0
    



array = []
with open('Algorithms\Algorithms Stanford - Coursera\Semana 3\QuickSort.txt','r') as f:
    for line in f:
        array.append(int(line.strip()))

print(f"El número de comparaciones es: {quick_sort(array, 0, len(array)-1)}")