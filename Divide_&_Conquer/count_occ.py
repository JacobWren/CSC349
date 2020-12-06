def freq(A, x):
    start_ = start(A, x, 0, len(A) - 1)
    if start_ == -1:
        return 0
    else:
        end_ = end(A, x, start_, len(A) - 1)
    if end_ == -1:
        return 1
    else:
        return end_ - start_ + 1

def start(A, x, min, max):
    if min == 0 and max == len(A) - 1 and x > A[len(A)-1]:
        return -1
    elif min == 0 and max == len(A) - 1 and x < A[0]:
        return -1
    else:
        if min > max:
            return -1
        mid = (min + max) // 2
        if mid == 0 and A[mid] == x: # base case
            return mid
        if (x > A[mid - 1]) and A[mid] == x:
            return mid
        elif x > A[mid]:
            return start(A, x, (mid + 1), max)
        else:
            return start(A, x, min, (mid - 1))
#print(start([2, 3, 7, 8, 9], 1, 0, 4))

def end(A, x, min, max):
    if min == 0 and max == len(A) - 1 and x > A[len(A)-1]:
        return -1
    elif min == 0 and max == len(A) - 1 and x < A[0]:
        return -1
    else:
        if min > max:
            return -1
        mid = (min + max) // 2
        if mid == len(A) - 1 and A[mid] == x:
            return mid
        if (x < A[mid + 1]) and A[mid] == x:
            return mid
        elif x < A[mid]:
            return end(A, x, min, (mid - 1))
        else:
            return end(A, x, (mid + 1), max)
#print(end([2, 3, 7, 8, 9], 7, 0, 4))

A = [-1, -1, 0, 2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 6]
print(freq(A, 17))