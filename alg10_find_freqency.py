"""
    this function give list of integer
    return elements that number of frequency be more than half of primary list

"""
max_frq = []
dict_nums = {}

def get_list(nums):
    for i in nums:
        if i not in dict_nums:
            dict_nums[i] = 1
        else:
            dict_nums[i] += 1

    for i in dict_nums:
      if dict_nums[i] > len(nums)//2:
          max_frq.append(i)
    return max_frq

print(get_list([1,1,2,2,2]))
