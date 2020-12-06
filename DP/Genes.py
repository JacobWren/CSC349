import sys

'''
def main(argv):
    # reads in file
    X = []
    i = 0
    file_in = open(sys.argv[1], "r", newline="")
    for line in file_in:
        X.append(line.split(', '))
        X[i][0] = X[i][0].rstrip('\n')
        X[i][0] = X[i][0].split(" ")
        i += 1
    print(X)
    #print(type(X[0][0][0]))
'''

X = [[['ATAGCC']],
     [['TGCTG']],
     [['x', 'A', 'C', 'G', 'T', '-']],
     [['A', '4', '7', '2', '1', '1']],
     [['C', '1', '4', '1', '2', '2']],
     [['G', '2', '1', '4', '1', '3']],
     [['T', '1', '2', '1', '4', '4']],
     [['-', '0', '0', '0', '0', '5']]]

#Y = X[2:]


Y = [
     [['x', 'A', 'C', 'G', 'T', '-']],
     [['A', '4', '1', '2', '1', '0']],
     [['C', '1', '4', '1', '2', '0']],
     [['G', '2', '1', '4', '1', '0']],
     [['T', '1', '2', '1', '4', '0']],
     [['-', '0', '0', '0', '0', '0']]]



a = []
for k in range(1, 5): # row
    for l in range(0, 5): # col
        #print(Y[k][0][0], Y[0][0][l + 1])
        a.append((Y[k][0][0] + Y[0][0][l + 1], int(Y[k][0][l + 1])))

dictionary = dict(a)
#print(dictionary)

#print(dictionary['AA'])



# 5 choose 2 = 10


def Alignment():
    n = len(X[0][0][0])
    m = len(X[1][0][0])
    rows, cols = (n + 1, m + 1)
    G = [[None for i in range(cols)] for j in range(rows)]
    R = [[['', ''] for i in range(cols)] for j in range(rows)]
    G[0][0] = 0
    R[0][0] = ['', '']

    for i in range(0, n):
        if X[0][0][0][i] == 'A':
            G[i + 1][0] = dictionary['A-'] + G[i][0]
        elif X[0][0][0][i] == 'C':
            G[i + 1][0] = dictionary['C-'] + G[i][0]
        elif X[0][0][0][i] == 'G':
            G[i + 1][0] = dictionary['G-'] + G[i][0]
        elif X[0][0][0][i] == 'T':
            G[i + 1][0] = dictionary['T-'] + G[i][0]

    for i in range(0, m):
        if X[1][0][0][i] == 'A':
            G[0][i + 1] = dictionary['A-'] + G[0][i]
        elif X[1][0][0][i] == 'C':
            G[0][i + 1] = dictionary['C-'] + G[0][i]
        elif X[1][0][0][i] == 'G':
            G[0][i + 1] = dictionary['G-'] + G[0][i]
        elif X[1][0][0][i] == 'T':
            G[0][i + 1] = dictionary['T-'] + G[0][i]


    for i in range(0, n):
        if X[0][0][0][i] == 'A':
            R[i + 1][0] = [R[i][0][0] + 'A', R[i][0][1]+ '-']
        elif X[0][0][0][i] == 'C':
            R[i + 1][0] = [R[i][0][0] + 'C', R[i][0][1]+ '-']
        elif X[0][0][0][i] == 'G':
            R[i + 1][0] = [R[i][0][0] + 'G', R[i][0][1]+ '-']
        elif X[0][0][0][i] == 'T':
            R[i + 1][0] = [R[i][0][0] + 'T', R[i][0][1]+ '-']

    for i in range(0, m):
        if X[1][0][0][i] == 'A':
            R[0][i + 1] = [R[0][i][0]+ '-', R[0][i][1] + 'A']
        elif X[1][0][0][i] == 'C':
            R[0][i + 1] = [R[0][i][0]+ '-', R[0][i][1] + 'C']
        elif X[1][0][0][i] == 'G':
            R[0][i + 1] = [R[0][i][0]+ '-', R[0][i][1] + 'G']
        elif X[1][0][0][i] == 'T':
            R[0][i + 1] = [R[0][i][0]+ '-', R[0][i][1] + 'T']

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            case_1 = G[i - 1][j - 1] + dictionary[X[0][0][0][i- 1] + X[1][0][0][j-1]]

            case_2 = G[i - 1][j] + dictionary[X[0][0][0][i - 1] + '-']

            case_3 = G[i][j - 1] + dictionary[X[1][0][0][j - 1] + '-']

            G[i][j] = max(case_1, case_2, case_3)

            if case_1 > case_2 and case_1 > case_3:
                R[i][j] = [R[i - 1][j - 1][0] + X[0][0][0][i - 1], R[i - 1][j - 1][1] + X[1][0][0][j - 1]]
            elif case_2 > case_3:
                R[i][j] = [R[i - 1][j][0] + X[0][0][0][i - 1], R[i - 1][j][1] + '-']
            else:
                R[i][j] = [R[i][j - 1][0] + '-', R[i][j - 1][1] + X[1][0][0][j - 1]]


    print('x: ', end='')
    for i in R[n][m][0]:
        print(i + ' ', end='')
    print()
    print('y: ', end='')
    for i in R[n][m][1]:
        print(i + ' ', end='')
    print()
    print('Score: ' + str(G[n][m]))

Alignment()




# command line to run:
# python Genes.py Genome.txt

'''
if __name__ == "__main__":
    main(sys.argv)
'''