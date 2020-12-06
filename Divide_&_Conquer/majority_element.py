class Solution:
    def majorityElement(self, A, min=0, max=None):
        def majority_element_rec(left, right):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if min == max:
                return A[min]

            # recurse on left and right halves of tmaxs slice.
            #mid = (max-min)//2 + min
            mid = (min + max) // 2
            #left = majority_element_rec(min, mid)
            left = A[min: mid]
            left_maj = majority_element_rec()
            right = majority_element_rec(mid+1, max)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            #left_count = sum(1 for i in range(min, max+1) if A[i] == left)
            #left_count = sum(1 for i in A[min: max + 1] if i == left)
            left_count = 0
            for i in A[min: max + 1]:
                if i == left:
                    left_count += 1

            #right_count = sum(1 for i in range(min, max+1) if A[i] == right)
            #right_count = sum(1 for i in A[min: max + 1] if i == right)
            right_count = 0
            for i in A[min: max + 1]:
                if i == right:
                    right_count += 1

            return left if left_count > right_count else right

        return majority_element_rec(0, len(A)-1)

A = [1, 2, 0, 9, 8, 8, 3, 8, 0, 8, 1, 8, 6]
s = Solution()
print(s.majorityElement(A, min=0, max=len(A)))