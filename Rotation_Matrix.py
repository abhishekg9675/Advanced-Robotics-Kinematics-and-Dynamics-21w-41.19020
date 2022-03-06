import numpy as np
import sympy as sym

def rotation_matrix(axis, angle=0, symbolic=False):

    try:
        print('Symbolic')
        if symbolic == True:
            angle = sym.symbols(u'θ')
            if axis == 'x':
                angle = sym.symbols(u'α')
                matrix = np.array([[1, 0, 0],
                                   [0, sym.cos(angle), -sym.sin(angle)],
                                   [0, sym.sin(angle), sym.cos(angle)]])
            elif axis == 'y':
                angle = sym.symbols(u'β')
                matrix = np.array([[sym.cos(angle), 0, sym.sin(angle)],
                                   [0, 1, 0],
                                   [-sym.sin(angle), 0, sym.cos(angle)]])
            elif axis == 'z':
                angle = sym.symbols(u'γ')
                matrix = np.array([[sym.cos(angle), -sym.sin(angle), 0],
                                   [sym.sin(angle), sym.cos(angle), 0],
                                   [0, 0, 1]])
            return matrix

    except:
        print('Numeric')
        angle = angle * np.pi/180

        if axis == 'x':
            matrix = np.array([[1, 0, 0],
                           [0, np.cos(angle), -np.sin(angle)],
                           [0, np.sin(angle), np.cos(angle)]])
        elif axis == 'y':
            matrix = np.array([[np.cos(angle), 0, np.sin(angle)],
                           [0, 1, 0],
                           [-np.sin(angle), 0, np.cos(angle)]])
        elif axis == 'z':
            matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                           [np.sin(angle), np.cos(angle), 0],
                           [0, 0, 1]])
        else:
            print('Pick Correct Axis')

        return np.around(matrix, 4)

#print(rotation_matrix('x' ,0, True) @ rotation_matrix('y' ,0, True))