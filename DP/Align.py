import sys


def main(argv):
    # read in file containing two strings and a scoring matrix
    X = []
    i = 0
    file_in = open(sys.argv[1], "r", newline="")
    for line in file_in:
        X.append(line.split(', '))
        X[i][0] = X[i][0].rstrip('\n')
        X[i][0] = X[i][0].split(" ")
        i += 1

    Alignment(X) # call to function


def Alignment(X):
    # Make score table into dictionary where keys are concatenated, e.g., 'AT' or 'T-'
    # Order of concatenation doesn't matter since score table (matrix) is symmetric

    Y = X[2:] # start Y at 2nd element of X, ignore two words
    a = []
    for k in range(1, 5):  # row wise
        for l in range(0, 5):  # col wise
            a.append((Y[k][0][0] + Y[0][0][l + 1], int(Y[k][0][l + 1])))

    dictionary = dict(a) # This is our score table, dictionary makes for easy retrieval

    n = len(X[0][0][0])
    m = len(X[1][0][0])

    rows, cols = (n + 1, m + 1)
    G = [[None for i in range(cols)] for j in range(rows)] # DP
    R = [[['', ''] for i in range(cols)] for j in range(rows)] # Store optimal alignment

    # BASE CASES

    G[0][0] = 0
    R[0][0] = ['', '']

    # fill in first column of DP
    for i in range(0, n):
        if X[0][0][0][i] == 'A':
            G[i + 1][0] = dictionary['A-'] + G[i][0]
        elif X[0][0][0][i] == 'C':
            G[i + 1][0] = dictionary['C-'] + G[i][0]
        elif X[0][0][0][i] == 'G':
            G[i + 1][0] = dictionary['G-'] + G[i][0]
        elif X[0][0][0][i] == 'T':
            G[i + 1][0] = dictionary['T-'] + G[i][0]

    # fill in first row of DP
    for i in range(0, m):
        if X[1][0][0][i] == 'A':
            G[0][i + 1] = dictionary['A-'] + G[0][i]
        elif X[1][0][0][i] == 'C':
            G[0][i + 1] = dictionary['C-'] + G[0][i]
        elif X[1][0][0][i] == 'G':
            G[0][i + 1] = dictionary['G-'] + G[0][i]
        elif X[1][0][0][i] == 'T':
            G[0][i + 1] = dictionary['T-'] + G[0][i]

    # fill in first column of storage of optimal alignments
    for i in range(0, n):
        if X[0][0][0][i] == 'A':
            R[i + 1][0] = [R[i][0][0] + 'A', R[i][0][1]+ '-']
        elif X[0][0][0][i] == 'C':
            R[i + 1][0] = [R[i][0][0] + 'C', R[i][0][1]+ '-']
        elif X[0][0][0][i] == 'G':
            R[i + 1][0] = [R[i][0][0] + 'G', R[i][0][1]+ '-']
        elif X[0][0][0][i] == 'T':
            R[i + 1][0] = [R[i][0][0] + 'T', R[i][0][1]+ '-']

    # fill in first row of storage of optimal alignments
    for i in range(0, m):
        if X[1][0][0][i] == 'A':
            R[0][i + 1] = [R[0][i][0]+ '-', R[0][i][1] + 'A']
        elif X[1][0][0][i] == 'C':
            R[0][i + 1] = [R[0][i][0]+ '-', R[0][i][1] + 'C']
        elif X[1][0][0][i] == 'G':
            R[0][i + 1] = [R[0][i][0]+ '-', R[0][i][1] + 'G']
        elif X[1][0][0][i] == 'T':
            R[0][i + 1] = [R[0][i][0]+ '-', R[0][i][1] + 'T']

# This is the 'Formula', it drives everything
# This is just a slight twist on Levenshtein Distance...
# the twist is we have a score table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            case_1 = G[i - 1][j - 1] + dictionary[X[0][0][0][i- 1] + X[1][0][0][j-1]]

            case_2 = G[i - 1][j] + dictionary[X[0][0][0][i - 1] + '-']

            case_3 = G[i][j - 1] + dictionary[X[1][0][0][j - 1] + '-']

            G[i][j] = max(case_1, case_2, case_3)

            # Store the optimal alignment of x[1,...,i] with y[1,...,j]
            # Notice the symmetry between the optimal score and optimal alignment in terms of their formula's...
            if case_1 > case_2 and case_1 > case_3:
                R[i][j] = [R[i - 1][j - 1][0] + X[0][0][0][i - 1], R[i - 1][j - 1][1] + X[1][0][0][j - 1]]
            elif case_2 > case_3:
                R[i][j] = [R[i - 1][j][0] + X[0][0][0][i - 1], R[i - 1][j][1] + '-']
            else:
                R[i][j] = [R[i][j - 1][0] + '-', R[i][j - 1][1] + X[1][0][0][j - 1]]


    # Here is the 'Solution'
    print('x: ', end='')
    for i in R[n][m][0]:
        print(i + ' ', end='')
    print()
    print('y: ', end='')
    for i in R[n][m][1]:
        print(i + ' ', end='')
    print()
    print('Score: ' + str(G[n][m]))


if __name__ == "__main__":
    main(sys.argv)
