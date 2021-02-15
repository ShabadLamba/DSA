import random


def minDifference():
    nums = [6, 6, 0, 1, 1, 4, 6]
    copyOfNums = nums.copy()
    valueToChangeTo = 0
    for items in nums:
        if(items == 0):
            copyOfNums.pop(copyOfNums.index(min(copyOfNums)))

    valueToChangeTo = min(copyOfNums)
    for index in range(3):
        for number in nums:
            if(number > valueToChangeTo):
                nums[nums.index(number)] = valueToChangeTo
                break
    print(nums)
    print(max(nums) - min(nums))


minDifference()
