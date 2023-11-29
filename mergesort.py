

def merge_sort(lst):

    if len(lst) > 1:

        left_lst = lst[:len(lst)//2]
        right_lst = lst[len(lst)//2:]

        merge_sort(left_lst)
        merge_sort(right_lst)

        
        i = 0 #left
        j = 0 #right
        k = 0 #merged

        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] < right_lst[i]:
                lst[k] = left_lst[i]
                i +=1
                k +=1
            else:
                lst[k] =  right_lst[j]
                j += 1 
                k += 1

        
        while i < len(left_lst):
            arr[k] = left_lst[i]
            i +=1
            k+=1

        while j < len(right_lst):
            arr[k] = right_lst[j]
            j += 1
            k+=1

        
        return lst
