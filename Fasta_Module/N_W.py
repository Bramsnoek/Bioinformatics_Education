import numpy as np
from pprint import pprint


class Needle:
    def __init__(self):
        self.pt = {'match': 1, 'mismatch': -1, 'gap': -1}

    def __match(self, seq1, seq2):
        if seq1 == seq2:
            return self.pt['match']
        elif seq1 == '-' or seq2 == '-':
            return self.pt['gap']
        else:
            return self.pt['mismatch']

    def needle(self, seq1, seq2):
        # N = Row
        # M = Column
        N, M = len(seq1), len(seq2)

        cost = np.zeros((N+1, M+1))

        for row in range(N+1):
            cost[row][0] = -1*row

        for column in range(M+1):
            cost[0][column] = -1*column

        for row in range(1, N+1):
            for column in range(1, M+1):
                #3 types of mutations: Substitution, Deletion and Insertion
                sub_cost = cost[row-1][column-1] + self.__match(seq1[row-1], seq2[column-1])
                del_cost = cost[row-1][column] + self.pt['gap']
                ins_cost = cost[row][column-1] + self.pt['gap']

                cost[row][column] = max(sub_cost, del_cost, ins_cost)

        print("cost matrix:")
        pprint(cost)

        #Traceback step
        align1, align2 = '', ''
        row, column = N, M

        while row > 0 and column > 0:
            cost_current = cost[row][column]
            cost_diag = cost[row-1][column-1]
            cost_left = cost[row][column-1]
            cost_up = cost[row-1][column]

            #Determine which way to move inside the matrix by using the 3 possibilities/functions we used before
            #But now reverse them, this way you can 'traceback' which matrix-index was used to calculate this matrix-index
            if cost_current == cost_diag + self.__match(seq1[row-1], seq2[column-1]):
                #Move diagonally up in the matrix
                aminoacid1, aminoacid2 = seq1[row-1], seq2[column-1]
                row, column = row-1, column-1
            elif cost_current == cost_up + self.pt['gap']:
                #Move up in the matrix
                aminoacid1, aminoacid2 = seq1[row-1], '-'
                row -= 1
            elif cost_current == cost_left + self.pt['gap']:
                #Move to the left in the matrix
                aminoacid1, aminoacid2 = '-', seq2[column-1]
                column -= 1

            align1 += aminoacid1
            align2 += aminoacid2

        while row > 0:
            aminoacid1, aminoacid2 = seq1[row-1], '-'
            align1 += aminoacid1
            align2 += aminoacid2
            row -= 1

        while column > 0:
            aminoacid1, aminoacid2 = '-', seq2[column-1]
            align1 += aminoacid1
            align2 += aminoacid2
            column -= 1

        align1 = align1[::-1]
        align2 = align2[::-1]
        align_length = len(align1)
        symbolic_link = ''
        seq_cost = 0
        identity_percentage = 0

        for i in range(align_length):
            aminoacid1 = align1[i]
            aminoacid2 = align2[i]

            if(aminoacid1 == aminoacid2):
                symbolic_link += '|'
                identity_percentage += 1
                seq_cost += self.__match(aminoacid1, aminoacid2)
            else:
                seq_cost += self.__match(aminoacid1, aminoacid2)
                symbolic_link += ' '

        identity_percentage = identity_percentage/align_length * 100

        print('Identity % = {} %'.format(round(identity_percentage, 2)))
        print('Seq_cost = {} \n'.format(seq_cost))
        print(align1)
        print(symbolic_link)
        print(align2)

        return round(identity_percentage, 2)