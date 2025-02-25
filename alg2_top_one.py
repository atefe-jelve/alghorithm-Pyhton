"""
    'TOP One'
    "[1,2,1,3,4,2] => [2,1]"
"""

def top(arr):
    values_dict = {}
    results_list = []
    max_val = 0

    for i in arr:
        if i in values_dict:
            values_dict[i] += 1
        else:
            values_dict[i] = 1

    max_val = max(values_dict.values())
    for i in values_dict.keys():
        if values_dict[i] == max_val:
            results_list.append(i)
        else:
            continue

    return results_list, values_dict

print(top([1,2,1,3,4,2]))
