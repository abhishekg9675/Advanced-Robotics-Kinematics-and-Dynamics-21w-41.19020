import sympy as sym
import numpy as np

def transformation_matrix(l, delta, lmbda, d, symbolic=False):

    try:
        if symbolic == True:
            print('Symbolic')
            input = [l, delta, lmbda, d]
            l, delta, lmbda, d = sym.symbols('l δ λ d')
            l, delta, lmbda, d = l*input[0], delta*input[1], lmbda*input[2], d*input[3]

            matrix = np.array([[sym.cos(delta), -sym.sin(delta)*sym.cos(lmbda), sym.sin(delta)*sym.sin(lmbda), l*sym.cos(delta)],
                               [sym.sin(delta), sym.cos(delta)*sym.cos(lmbda), -sym.cos(delta)*sym.sin(lmbda), l*sym.sin(delta)],
                               [0, sym.sin(lmbda), sym.cos(lmbda), d],
                               [0, 0, 0, 1]])
        return matrix
    except:
        print('Numeric')
        sindelta = np.sin(delta * np.pi / 180)
        cosdelta = np.cos(delta * np.pi / 180)
        sinlmbda = np.sin(lmbda * np.pi / 180)
        coslmbda = np.cos(lmbda * np.pi / 180)
        matrix = np.array([[cosdelta, -sindelta * coslmbda, sindelta * sinlmbda, l * cosdelta],
                           [sindelta, cosdelta * coslmbda, -cosdelta * sinlmbda, l * sindelta],
                           [0, sinlmbda, coslmbda, d],
                           [0, 0, 0, 1]])
        return np.around(matrix, 4)


#print(transformation_matrix(0, 1, 0, 1,True) @ transformation_matrix(1, 0, 1, 0,True))