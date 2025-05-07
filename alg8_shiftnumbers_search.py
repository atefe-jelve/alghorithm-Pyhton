nums = [1000, 1100, 1200, 1300, 1400]

def find(num):
    if num < nums[0]:
        return nums[0]
    elif num > nums[-1]:
        return nums[-1]

    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == num:
            return nums[mid-1]
        elif nums[mid] < num:
            low = mid + 1
        else:
            high = mid - 1

    return nums[high]

print(find(1150))