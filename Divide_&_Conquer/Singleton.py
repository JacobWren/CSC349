import sys

def main(argv):
    f = open(sys.argv[1], 'r')
    # I want this string to be a list
    A = f.read()
    A = A.replace(',', '')
    A = list(A.split(" "))
    print(Singleton(A, 0, len(A) - 1))


def Singleton(A, min, max):
    mid = (max + min) // 2
    if min == max == mid: # case for n=1 or when unique element is at the end of the beginning of the list
        return A[min]

    if A[mid] != A[mid + 1] and A[mid] != A[mid - 1]:
        return A[mid]

    elif A[mid] != A[mid + 1] and (((max - min + 1) - 1) / 2) % 2 == 0:
        return Singleton(A, min, mid - 2)
    elif A[mid] != A[mid + 1] and (((max - min + 1) - 1) / 2) % 2 != 0:
        return Singleton(A, mid + 1, max)

    elif A[mid] != A[mid - 1] and (((max - min + 1) - 1) / 2) % 2 == 0:
        return Singleton(A, mid + 2, max)
    elif A[mid] != A[mid - 1] and (((max - min + 1) - 1) / 2) % 2 != 0:
        return Singleton(A, min, mid - 1)


if __name__ == "__main__":
    main(sys.argv)