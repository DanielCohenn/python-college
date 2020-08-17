import numpy as np
import matplotlib.pyplot as plt
import pandas


def import_data(file):
    """
    this function let us import our desired data from an xl file,
    than we split our data into 3 different arrays.
    arr1 --> L ; arr2 --> NewX ; arr3 --> NewY
    """
    arr1 = np.array(file[['L']])
    arr2 = np.array(file['NewX'])
    arr3 = np.array(file['NewY'])
    return arr1, arr2, arr3


def plot_my_data(arr1: list, arr2: list, arr3: list):
    """
    plotting our data in respect to the values in arr1, each value gives different color.
    """
    color_dict = {0: 'red', 1: 'green', 2: 'blue'}
    # extracting X and Y data from file
    split_X = np.array(file['X'])
    split_Y = np.array(file['Y'])
    f = plt.figure(figsize=(8, 8))
    # plotting our X and Y data
    plt.subplot(2, 1, 1)
    for i, val in enumerate(arr1):
        # i represents the index in arr1 and val is the value corresponding to i
        if val == 0:
            plt.scatter(split_X[i], split_Y[i], color=color_dict[0], edgecolors='black')

        elif val == 1:
            plt.scatter(split_X[i], split_Y[i], color=color_dict[1], edgecolors='black')
        else:
            plt.scatter(split_X[i], split_Y[i], color=color_dict[2], edgecolors='black')
    plt.title('X and Y scatter')
    plt.xlabel('X')
    plt.ylabel('Y')
    # plotting our New x and New Y data
    plt.subplot(2, 1, 2)
    for i, val in enumerate(arr1):
        # i represents the index in arr1 and val is the value corresponding to i
        if val == 0:
            plt.scatter(arr2[i], arr3[i], color=color_dict[0], edgecolors='black')

        elif val == 1:
            plt.scatter(arr2[i], arr3[i], color=color_dict[1], edgecolors='black')
        else:
            plt.scatter(arr2[i], arr3[i], color=color_dict[2], edgecolors='black')
    plt.title('New X and New Y scatter')
    plt.xlabel('New X')
    plt.ylabel('New Y')
    plt.tight_layout(pad=3.0)
    plt.show()

# reading our xl file with the panda.read built-in
file = pandas.read_excel('Data1.xlsx')
arr1, arr2, arr3 = import_data(file)
plot_my_data(arr1, arr2, arr3)
