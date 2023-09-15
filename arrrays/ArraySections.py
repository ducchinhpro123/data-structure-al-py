# Array Advance Game
def array_advance(A):
    furthest_reached = 0
    last_index = len(A) - 1
    i = 0
    while i <= furthest_reached < last_index:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    print(furthest_reached)
    return furthest_reached >= last_index


# Arbitrary Precision Increment
def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    print(A)


# A1 = [1, 4, 9]
# A2 = [9, 9, 9]
# plus_one(A1)
# plus_one(A2)


# Two Sum Problem
def two_sum(A, target):
    """Time Complexity: O(n)
    Space Complexity: O(n)"""
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(f"{ht[A[i]], A[i]}")
            return True
        else:
            ht[target - A[i]] = A[i]
    return False


def two_sum_2(A, target):
    """work with sorted araray"""
    i = 0
    j = len(A) - 1
    while i < j:
        if A[i] + A[j] == target:
            return [A[i], A[j]]
        elif A[i] + A[j] < target:
            i += 1
        else:
            j -= 1
    return []


def assigment_task(A):
    A = sorted(A)
    for i in range(len(A) // 2):
        print(f"{A[i]}, {A[~i]}")


def intersection(A, B):
    """What elements are common to A and B? note: sorted array"""
    i = 0
    j = 0
    intersection = []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersection.append(A[i])
            i += 1
            j += 1

        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection


if __name__ == "__main__":
    A = [2, 3, 3, 5, 7, 11]
    B = [3, 3, 7, 15, 31]
    print(intersection(A, B))
