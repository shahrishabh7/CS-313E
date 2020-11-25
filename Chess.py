#  File: Chess.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

import sys


class Queens(object):
    def __init__(self, n=8):
        self.board = []
        self.n = n
        self.solutions = 0
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('*')
            self.board.append(row)

    # print the board
    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=' ')
            print()
        print()

    # check if a position on the board is valid
    def is_valid(self, row, col):
        for i in range(self.n):
            if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
                return False
        for i in range(self.n):
            for j in range(self.n):
                row_diff = abs(row - i)
                col_diff = abs(col - j)
                if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
                    return False
        return True

    # do the recursive backtracking
    def recursive_solve(self, col):
        if (col == self.n):
            self.solutions += 1
        else:
            for i in range(self.n):
                if (self.is_valid(i, col)):
                    self.board[i][col] = 'Q'
                    if (self.recursive_solve(col + 1)):
                        return True
                    self.board[i][col] = '*'
            return False
    '''def recursive_solve(self, col):
        if (col == self.n):
            self.solutions += 1
        else:
            for i in range(self.n):
                if (self.is_valid(i, col)):
                    self.board[i][col] = 'Q'
                    if (self.recursive_solve(col + 1)):
                        return True
                    self.board[i][col] = '*'
            return False'''

    '''def recursive_solve(self, row, col):
        if (col == self.n):
            return True
        else:
            if (self.is_valid(row, col)):
                self.board[row][col] = 'Q'
                if (self.recursive_solve(row,col + 1)):
                    return True
                elif (self.recursive_solve(row + 1,col)):
                    return True
                self.board[row][col] = '*'
            return False'''
    '''def count_solutions(self):
        solutions = 0
        for x in range(self.n):
            if self.recursive_solve(x):
                solutions += 1
        return solutions'''
    # if the problem has a solution print the board
    def solve(self):
        for i in range(self.n):
            if (self.recursive_solve(i)):
                self.print_board()

def main():
    # read the size of the board
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create a chess board
    game = Queens(n)

    # place the queens on the board and count the solutions
    game.recursive_solve(0)

    # print the number of solutions
    print(game.solutions)

if __name__ == "__main__":
    main()