def removeDuplicates(nums):
    """
    :type nums: List[int] - sorted
    :rtype: List[int]
    """
    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return nums[0: i + 1]

print(removeDuplicates([1, 1, 2, 3, 3, 3, 5]))
print(removeDuplicates([]))