import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class MatrixCalculator(object):
    def __init__(self, mat):
        self.mat = mat
        self.row_echelon = None
        self.transpose = None
        self.inverse = None
        self.determinant = None
    '''
    Operations:

    '''
    def add(self, mat1, mat2):
        res = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
        return res

    def substraction(self, mat1, mat2):
        res = [[mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
        return res
    
    def multiply(self, mat1, mat2):
        if len(mat1[0]) != len(mat2):
            print('Shape not compatible for multiplication')
            return None
        else:
            res = [[sum(a*b for a,b in zip(mat1_row, mat2_col)) for mat2_col in zip(*mat2)] for mat1_row in mat1]
            return res

    '''
    Matrix Algorithms:

    '''
    def row_echelon_form(self, mat):
        for k in range(len(mat[0])):
            mat[0][k] = mat[0][k] / mat[0][0]
        for i in range(1, len(mat)):
            ratio = mat[0][0] / mat[i][0] 
            for j in range(len(mat[0])):
                mat[i][j] = ratio*mat[i][j] - mat[0][j]
        self.row_echelon = mat
        return mat  

    def transpose(self, mat):
        res = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
        self.transpose = res
        return res
    
    def minor(self, mat, i, j):
        res = [row[:j] + row[j+1:] for row in (mat[:i]+mat[i+1:])]
        return res
    
    def determinant(self, mat):
        '''
        to compute the determinant of a matrix
        Args:
            mat (list: []): input list of elements
        Return:
            determinant (float): determinant of the matrix
        '''
        if len(mat) == 1:
            return mat[0][0]   
        elif len(mat) == 2:
            det = mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
            return det
        else:
            det = 0
            for i in range(len(mat)):
                det += ((-1)**i)*mat[0][i]*self.determinant(self.minor(mat, 0, i))
            return det

    def inverse(self, mat):
        det = self.determinant(mat)
        if det == 0:
            print('Inverse does not exist')
            return None
        else:
            res = [[0 for i in range(len(mat))] for j in range(len(mat))]
            for i in range(len(mat)):
                for j in range(len(mat)):
                    res[i][j] = ((-1)**(i+j))*self.determinant(self.minor(mat, i, j))
            res = np.array(res)
            res = res.T
            res = res/det
            return res

    def display_matrix(self, mat):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                print(round(mat[i][j], 2), end=' ')
            print()


