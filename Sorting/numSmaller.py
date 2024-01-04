def solution(nums):
    countList = []
    for i in range(len(nums)):
        count = 0
        for j in range(i+1,len(nums)):
            
            if nums[j] < nums[i]:
                count += 1
                
        countList.append(count)
    
    return sum(countList)