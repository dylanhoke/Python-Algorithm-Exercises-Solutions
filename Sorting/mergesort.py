def solution(a):

    def merge(left:list[int], right:list[int]) -> list[int]:

        isSorted = []

        i = j = inversion = 0

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:

                isSorted.append(left[i])
                i += 1
            else:
                isSorted.append(right[j])
                j += 1

                inversion += len(left) - i 
        
        if i < len(left):
            isSorted += left[i:]

        if j < len(right):
            isSorted += right[j:]

        # isSorted.extend(left[i:])
        # isSorted.extend(right[j:])
        
        return isSorted, inversion
            
    def mergesort(arr:list[int]):

        if not arr:
            return []

        if len(arr) == 1:
            return arr
        
        mid = len(arr) // 2
        #math.floor(len(arr)/2)

        left = mergesort(arr[:mid])

        right = mergesort(arr[mid:])

        return merge(left, right)
    
    return mergesort(a)