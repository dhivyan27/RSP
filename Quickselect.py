def partition(arr,l,h):

    pivot = arr[h]

    i = l - 1

    for j in range(l,h):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1



def quickselect(arr,l,h,k):

    if l == h:
        return arr[l]
    
    pivot_index = partition(arr,l,h)

    left_elems = pivot_index - l


    if k < left_elems:
        return quickselect(arr, l, pivot_index-1, k)
    
    elif k > left_elems:
        return quickselect(arr, pivot_index + 1, h, k - left_elems - 1)
    
    else:
        return arr[pivot_index]