def two_sum(nums,target):
    dict1={}
    results = []
    for i in range(len(nums)):
        comp = target-nums[i]
        if comp in dict1:
            results.append([dict1[comp],i])
        dict1[nums[i]]=i
    return results

#if all possible solutions are needed 
#if only 1st one is need then remove results
# Time Complexity=o(n)

# 