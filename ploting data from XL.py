import numpy as np
import matplotlib.pyplot as plt
import pandas

def import_data(file):
    arr1 = np.array(file[['L']])
    arr2 = np.array(file[['X','Y']])
    arr3 = np.array([file['NewX'], file['NewY']])
    return arr1, arr2, arr3


def plot_my_data(arr1, arr2, arr3):
    color_dict = {0: 'red', 1: 'green', 2: 'blue'}
    #lets split arr2 to two different arrays with x values and y values
    split_X = np.array(file['X'])
    split_Y = np.array(file['Y'])
    for i, val in enumerate(arr1):
        if val == 0:
            plt.scatter(split_X[i], split_Y[i], color=color_dict[0], edgecolors='black')
        elif val == 1:
            plt.scatter(split_X[i], split_Y[i], color=color_dict[1], edgecolors='black')
        else:
            plt.scatter(split_X[i], split_Y[i], color=color_dict[2], edgecolors='black')
    plt.show()

file = pandas.read_excel('Data1.xlsx')
arr1, arr2, arr3 = import_data(file)
plot_my_data(arr1, arr2, arr3)