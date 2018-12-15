from math import floor, ceil
from random import randint
from itertools import product

def merge(A: list, i: int , j: int, k: int):
    """Combine/Merge step of mergesort∫.
    A is an list.  A[i:j] and A[j+1,k] are sorted
    """
    ind_left = 0
    ind_right =  1
    pivot_array = []

    while i + ind_left <= j and j + ind_right <= k:
        if A[j + ind_right] < A[i + ind_left]:
            pivot_array.append(A[j + ind_right])
            ind_right += 1
        else:
            pivot_array.append(A[i + ind_left])
            ind_left += 1

    if j + ind_right <= k:
        while j + ind_right <= k:
            pivot_array.append(A[j + ind_right])
            ind_right += 1
    else:
        while i + ind_left <= j:
            pivot_array.append(A[i + ind_left])
            ind_left += 1

    for ind in range(k, i-1, -1):
        A[ind] = pivot_array.pop()

def merge_sort(A: list, lower_bound: list, upper_bound: list):
    """Naive implementation of mergesort. Code is quite straightforward∫"""

    if lower_bound < upper_bound:
        middle = floor((lower_bound + upper_bound) / 2)
        merge_sort(A, lower_bound, middle)
        merge_sort(A, middle + 1, upper_bound)
        merge(A, lower_bound, middle, upper_bound)


def pad_with_n_zeros(a_number: int, n: int):
    """Computes a_number * 10**n without performing multiplications"""
    a_number = str(a_number)
    a_number = a_number + '0' * n
    return int(a_number)

def kzb(x: int, y: int):
    """Karatzuba's multiplication algorithm for arbitray length integers"""

    X = str(x)
    Y = str(y)

    if len(X) == 1 or len(Y) == 1:
        return x * y
    else:
        nx = len(X)
        ny = len(Y)
        A = X[:floor(nx/2)]
        B = X[floor(nx/2):]
        C = Y[:floor(ny/2)]
        D = Y[floor(ny/2):]
        bd = kzb(int(B), int(D))
        bc = kzb(int(B), int(C))
        ad = kzb(int(A), int(D))
        ac = kzb(int(A), int(C))
        return  (bd +
                 pad_with_n_zeros(ad, ceil(nx/2)) +
                 pad_with_n_zeros(bc, ceil(ny/2)) +
                 pad_with_n_zeros(ac, ceil(nx/2) + ceil(ny/2)))


def test_mergesort():
    print("Testint mergesort algorithm")
    for i in range(1,11):
        A = [randint(0, 20) for _ in range(i)]
        merge_sort(A, lower_bound=0, upper_bound=len(A)-1)
        print(f"Array size = {len(A)}. Sorted: {A == sorted(A)}")

def test_karatsuba():
    print("Testing karatsuba algorithm")
    for i, j in product(range(0,4), range(0,6)):
        a = randint(10**i, 10**(i+1)-1)
        b = randint(10**j, 10**(j+1)-1)
        result = kzb(a, b)
        print(result == a*b, {'a':a, 'b':b})

if __name__ == "__main__":

    test_karatsuba()
    test_mergesort()