# -*- coding: utf-8 -*-
"""
env:python3
author:Jiashuai Liu
to choose from 3 types by 5 characters
"""
import numpy as np

# Random consistency index
RI_dict = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}

# The weight is obtained and calculated by sum method
def get_w(array):
    row = array.shape[0]  # Calculate the order
    a_axis_0_sum = array.sum(axis=0)
    # print(a_axis_0_sum)
    New = array / a_axis_0_sum
    # print(b)
    b_axis_0_sum = New.sum(axis=0)  # sum by column， not used behind
    b_axis_1_sum = New.sum(axis=1)  # added according to the rows, get eigenvectors of each row
    # print(b_axis_1_sum)
    w = b_axis_1_sum / row  # normalization(eigenvectors)
    AW = (w * array).sum(axis=1)
    # print(AW)
    max_max = sum(AW / (row * w))  # Maximum eigenvalue
    # print(max_max)
    CI = (max_max - row) / (row - 1)
    CR = CI / RI_dict[row]
    if CR < 0.1:
        # print(round(CR, 3))
        # print('meet the consistency')
        # print(np.max(w))
        # print(sorted(w,reverse=True))
        # print('the Maximum eigenvalue is ',max_max)
        # print('eigenvector is :%s' % w)
        return w
    else:
        print(round(CR, 3))  # Rounding, followed by decimal places
        print('Do not meet the consistency, please modify')


def main(array):
    if type(array) is np.ndarray:
        return get_w(array)
    else:
        print('Please enter numpy object')

# define the first layer, the shape is 5*5
if __name__ == '__main__':
    e = np.array([[1, 2, 7, 5, 5], [1 / 2, 1, 4, 3, 3], [1 / 7, 1 / 4, 1, 1 / 2, 1 / 3], [1 / 5, 1 / 3, 2, 1, 1],
                  [1 / 5, 1 / 3, 3, 1, 1]])
    print("the shape of e is", e.shape)
    # the follow 5 matrix define the second layer, the shape of them is 3*3
    a = np.array([[1, 1 / 3, 1 / 8], [3, 1, 1 / 3], [8, 3, 1]])
    b = np.array([[1, 2, 5], [1 / 2, 1, 2], [1 / 5, 1 / 2, 1]])
    c = np.array([[1, 1, 3], [1, 1, 3], [1 / 3, 1 / 3, 1]])
    d = np.array([[1, 3, 4], [1 / 3, 1, 1], [1 / 4, 1, 1]])
    f = np.array([[1, 4, 1 / 2], [1 / 4, 1, 1 / 4], [2, 4, 1]])
    e = main(e)
    a = main(a)
    b = main(b)
    c = main(c)
    d = main(d)
    f = main(f)
    try:
        res = np.array([a, b, c, d, f])
        # print(res)
        ret = (np.transpose(res) * e).sum(axis=1)
        print(ret)
    except TypeError:
        print('Data error, may not meet the consistency, please modify')
