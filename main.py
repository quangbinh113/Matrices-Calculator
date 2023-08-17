import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Matrix_Calculator import Matrix_Calculator

if __name__ == '__main__':
    x = int(input('Enter size of matrix: '))
    mat = []
    for i in range(x):
        arr = list(map(int, input().split()[:x]))
        mat.append(arr)
    
    m = Matrix_Calculator()
    print(m.determinant(mat))