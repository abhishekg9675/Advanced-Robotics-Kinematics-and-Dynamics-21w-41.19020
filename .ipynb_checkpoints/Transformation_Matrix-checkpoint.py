#import sympy
import numpy as np

def transformation_matrix(l,lmbda,d,delta):
    #l = sympy.Symbol('l')
    #lmbda = sympy.Symbol('lmbda')
    #d = sympy.Symbol('d')
    #delta = sympy.Symbol('delta')
    
    sindelta = np.sin(delta * np.pi / 180)
    cosdelta = np.cos(delta * np.pi / 180)
    sinlmbda = np.sin(lmbda * np.pi / 180)
    coslmbda = np.cos(lmbda * np.pi / 180)
    matrix = np.array([[cosdelta, -sindelta*coslmbda, sindelta*sinlmbda, l*cosdelta], 
                       [sindelta, cosdelta*coslmbda, -cosdelta*sinlmbda, l*sindelta],
                       [0, sinlmbda, coslmbda, d],
                       [0, 0, 0, 1]])
    #print(matrix)
    return np.around(matrix, 4)
    