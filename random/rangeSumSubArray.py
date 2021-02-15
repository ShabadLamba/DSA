def rangeSum():
    nums = [1, 2, 3, 4]
    n = 4
    left = 1
    right = 10
    subArraySumArray = []
    for numbers in range(len(nums)):
        subarraysum = 0
        for data in nums[numbers:]:
            subarraysum += data
            subArraySumArray.append(subarraysum)

    subArraySumArray.sort()
    finaSum = 0
    if((right - left + 1) == len(subArraySumArray)):
        finaSum += sum(subArraySumArray)
    else:
        for data in range(left - 1, right):
            finaSum += subArraySumArray[data]
    finaSum = finaSum % (1000000007)
    print(finaSum)


rangeSum()
