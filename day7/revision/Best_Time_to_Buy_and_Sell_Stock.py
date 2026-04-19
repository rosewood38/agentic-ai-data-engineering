def maxprofit(nums:List[int])->int:
    minprice=float(inf)
    maxprofit=0
    for i in nums:
        if i<minprice:
            minprice=i
        else:
            profit=i-minprice
            maxprofit=max(maxprofit,profit)
    return maxprofit