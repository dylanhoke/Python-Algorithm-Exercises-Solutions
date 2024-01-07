def solution(nums):
    countList = []
    for i in range(len(nums)):
        count = 0
        for j in range(i+1,len(nums)):
            
            if nums[j] < nums[i]:
                count += 1
                
        countList.append(count)
    
    return sum(countList)

# def solution(nums):
#     def merge_sort(arr, indices):
#         if len(arr) <= 1:
#             return arr, indices

#         mid = len(arr) // 2
#         left, left_indices = merge_sort(arr[:mid], indices[:mid])
#         right, right_indices = merge_sort(arr[mid:], indices[mid:])
#         merged, merge_indices = merge(left, right, left_indices, right_indices)

#         return merged, merge_indices

#     def merge(left, right, left_indices, right_indices):
#         merged = []
#         inversions = 0
#         i = j = 0

#         while i < len(left) and j < len(right):
#             if left[i] <= right[j]:
#                 merged.append(left[i])
#                 left_indices[i] += inversions
#                 i += 1
#             else:
#                 merged.append(right[j])
#                 right_indices[j] += len(left) - i
#                 j += 1
#                 inversions += 1

#         merged.extend(left[i:])
#         left_indices[i:] = [idx + inversions for idx in left_indices[i:]]
#         merged.extend(right[j:])
#         right_indices[j:] = [idx + inversions for idx in right_indices[j:]]

#         return merged, left_indices + right_indices

#     _, result = merge_sort(nums, list(range(len(nums))))
#     return sum(result)