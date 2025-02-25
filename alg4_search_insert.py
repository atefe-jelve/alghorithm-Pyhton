"""
    search_insert
        [1, 3, 5, 6] , 3 => 1
        [1, 3, 5, 6] , 4 => 2
        [1, 3, 5, 6] , 4 => 4
        [1, 3, 5, 6] , 0 => 0

"""

def search_insert(arr, num):
    low = 0
    high = len(arr) -1 #3
    mid = high // 2 #1

    while low <= high:
        if num > arr[mid]:
            mid += 1
            low = mid
        else:
            mid -= 1
            high = mid

        return low
print(search_insert([1, 3, 5, 6] , 4))