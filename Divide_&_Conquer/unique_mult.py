'''
#import sys
#with open(sys.argv[1], 'r') as f:
    # I want this string-tuple to be a list
    #A = f.read()
    #A = A.replace('(', '').replace(')', '')
    #A = A.replace(',', '')
    #A = list(A.split(" "))


# command line to run:
# python unique_mult.py singleton.txt

A = [-4, -4, -4, -4, -2, -2, -2, -2, 5, 5, 12, 12, 67, 67, 72, 72, 72, 72, 80, 80, 91, 91, 91, 91, 92]
#A = [-2, -2, 5, 5, 12, 12, 67, 67, 72, 72, 80, 80, 99]
#A = "(-2, -2, 5, 5, 12, 12, 12, 67, 72, 72, 80, 80)"
#A = A.replace('(', '').replace(')', '')
#A = A.replace(',', '')
#A = list(A.split(" "))

def Find_Singleton(A, x = A[0], n = len(A) - 1, m = 0):
    # this is just binary search done iteratively with 1 minor adjustment - we find the last occurrence.
    # By default we would find any of the duplicates, not just the first for instance.
    # Once we find the element, x, we simply continue searching to the right of it - but of course we keep the
    # location where we first found it in case it is unique - if not we update its index, found_last.
    min = m
    max = n
    while min <= max:
        mid = (max + min) // 2
        if int(x) < int(A[mid]):
            max = mid - 1
        elif int(x) > int(A[mid]):
            min = mid + 1
        else:
            found_last = mid # we set found_last here in case there are no duplicates to the right.
            min = mid + 1 # we are moving from left to right!
    if found_last == m:
        return int(A[found_last])
    else:
        return Find_Singleton(A, x = A[found_last + 1], m = found_last + 1) # m tracks the beginning of list, but we
        # are moving from left to right.

print(Find_Singleton(A))

A = [-1, -1, 2, 2, 4, 4, 4, 4, 6]
def Singleton(A, found_last = 0, min = 0, max = len(A) -1, start = 0, x = A[0]):
    if max >= min:
        mid = (max + min) // 2
        if x < A[mid]:
            return Singleton(A, found_last, min, mid - 1, start, x)
        elif x > A[mid]:
            return Singleton(A, found_last, mid + 1, max, start, x)
        else:
            #return mid
            return Singleton(A, mid, mid + 1, len(A) -1, start, x)
    if found_last == start:
        return int(A[found_last])
    else:
        # doesn't matter what found_last is
        return Singleton(A, found_last, found_last + 1, max = len(A) - 1, start = found_last + 1, x = A[found_last + 1])



print(Singleton(A))

'''
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

A = [-1, -1, 2, 2, 3, 4, 4, 4, 4]
def Singleton(A, index = 0):
    end_ = end(A, A[index], index, len(A) - 1)
    if index == end_:
        return A[end_]
    else:
        return Singleton(A, end_ + 1)

print(Singleton(A))