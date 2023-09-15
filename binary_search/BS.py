import bisect


def bs_iterative(data, target):
    i = 0
    j = len(data) - 1
    while i <= j:
        mid_point = (i + j) // 2
        if data[mid_point] == target:
            return mid_point
        elif data[mid_point] > target:
            j = mid_point - 1
        else:
            i = mid_point + 1
    return None


def bs_recursive(data, target):
    def _bs_recursive(data, target, low, hight):
        if low > hight:
            return None
        else:
            mid = (low + hight) // 2
            if data[mid] == target:
                return mid
            elif data[mid] > target:
                return _bs_recursive(data, target, low, mid - 1)
            else:
                return _bs_recursive(data, target, mid + 1, hight)

    return _bs_recursive(data, target, 0, len(data) - 1)


def find_closest_number(data, target):
    """find the unit difference and the element closest target in data"""
    i = 0
    j = len(data) - 1
    min_diff = min_diff_left = min_diff_right = float('inf')
    closest_number = None

    if len(data) == 0:
        return None
    if len(data) == 1:
        return data[0]
    while i <= j:
        mid = (i + j) // 2
        if mid > 0:  # make sure not ran out of the range
            min_diff_left = abs(data[mid - 1] - target)
        if mid + 1 < len(data):  # make sure not ran out of the range
            min_diff_right = abs(data[mid + 1] - target)

        #  find the least difference
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_number = data[mid - 1]
        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_number = data[mid + 1]

        # Move mid pointer
        if data[mid] < target:
            i = mid + 1
        elif data[mid] > target:
            j = mid - 1
            if j < 0:
                return data[mid]
        else:
            print(f"the least difference: 0")
            return data[mid]  # A[mid] itself is the closest element
    print(f"the least difference: {min_diff}")
    return closest_number


def binary_search_insertion(nums: list[int], target: int) -> int:
    """二分查找插入点（存在重复元素）"""
    i, j = 0, len(nums) - 1  # 初始化双闭区间 [0, n-1]
    while i <= j:
        m = (i + j) // 2  # 计算中点索引 m
        if nums[m] < target:
            i = m + 1  # target 在区间 [m+1, j] 中
        elif nums[m] > target:
            j = m - 1  # target 在区间 [i, m-1] 中
        else:
            j = m - 1  # 首个小于 target 的元素在区间 [i, m-1] 中
    # 返回插入点 i leftmost
    return i


def find_fixed_point(nums):
    """find the fixed point in array: nums[i] == i"""
    i = 0
    j = len(nums) - 1
    while i <= j:
        md = (i + j) // 2
        if nums[md] < md:
            i = md + 1
        elif nums[md] > md:
            j = md - 1
        else:
            return nums[md]
    return None


def find_highest_number(nums):
    """Find Bitonic Peak"""
    i = 0
    j = len(nums) - 1
    while i <= j:
        mid = (i + j) // 2
        mid_left = nums[mid - 1] if mid - 1 > 0 else float('-inf')
        mid_right = nums[mid + 1] if mid + 1 < len(nums) else float('inf')
        if mid_left < nums[mid] < mid_right:
            i = mid + 1
        elif mid_left > nums[mid] > mid_right:
            j = mid - 1
        elif mid_left < nums[mid] > mid_right:
            return nums[mid]
    return None


def find(nums, target):
    """This function equivalent with bisect_right built-in python"""
    i = 0
    j = len(nums) - 1
    while i <= j:
        # divide by two halve
        mid = (i + j) // 2
        if nums[mid] > target:
            j = mid - 1
        elif nums[mid] < target:
            i = mid + 1
        # the case when nums[mid] == target
        else:
            if mid + 1 > len(nums):  # we get the first occurrence
                return mid
            if nums[mid + 1] != target:  # we get the first occurrence
                return mid
            j = mid - 1  # the case when it not the first occurrence
    return None


def find_nums(nums):
    i = 0
    j = len(nums) - 1
    while i <= j:
        mid = (i + j) // 2
        if nums[mid] > nums[j]:
            i = mid + 1
        elif nums[mid] < nums[j]:
            j = mid

    return i


def integer_square_root(k):
    i = 0
    j = k // 2
    res = 0
    while i <= j:
        m = (i + j) // 2
        if m ** 2 > k:
            j = m - 1
        elif m ** 2 <= k:
            i = m + 1
            res = max(m, res)
        else:
            return m
    return res


print(integer_square_root(300))
