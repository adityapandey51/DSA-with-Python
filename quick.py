def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        l = []
        r = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                l.append(arr[i])
            else:
                r.append(arr[i])
        return quicksort(l) + [pivot] + quicksort(r)


numbers = [5,7,2,9,1,3,0]
sorted_numbers = quicksort(numbers)
print(sorted_numbers)