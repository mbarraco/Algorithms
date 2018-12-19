from math import floor, ceil


def merge_and_count(A: list, i: int , j: int, k: int):
    """Merge and count inversion A[m] > A[n] with m < n, in subarray A[i:k].

    Args:
        A (list):  A[i:j] and A[j+1,k] are sorted.
    """
    ind_left = 0
    ind_right =  1
    pivot_array = []
    inversion_count = 0


    while i + ind_left <= j and j + ind_right <= k:
        if A[j + ind_right] < A[i + ind_left]:
            pivot_array.append(A[j + ind_right])
            ind_right += 1

            if i == j:
                inversion_count += 1
            else:
                inversion_count += j - (i + ind_left) + 1 if j - (i + ind_left) > 0 else 0

        else:
            pivot_array.append(A[i + ind_left])
            ind_left += 1

    if j + ind_right <= k:
        while j + ind_right <= k:
            pivot_array.append(A[j + ind_right])
            ind_right += 1

            inversion_count += j - (i + ind_left) + 1 if j - (i + ind_left) > 0 else 0

    else:
        while i + ind_left <= j:
            pivot_array.append(A[i + ind_left])
            ind_left += 1

    for ind in range(k, i-1, -1):
        A[ind] = pivot_array.pop()
    return inversion_count


def count_and_sort(A: list, lower_bound: list, upper_bound: list):
    """Count inversions by piggybacking mergesort"""

    if lower_bound < upper_bound:
        middle = floor((lower_bound + upper_bound) / 2)
        left_count = count_and_sort(A, lower_bound, middle)
        right_count = count_and_sort(A, middle + 1, upper_bound)
        split_count = merge_and_count(A, lower_bound, middle, upper_bound)
        return left_count + right_count + split_count
    else:
        return 0


def test_inversion_count():
    """TODO: write a proper test considering cornercases"""
    print("Testing inversion count")
    A = [1,2,3,4,1,6,7,0]
    inversion_count = count_and_sort(A, lower_bound=0, upper_bound=len(A)-1)
    print(f"Inversion count = {inversion_count}")

if __name__ == "__main__":
    test_inversion_count()