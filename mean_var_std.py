# Author: Ghomren Victor Oghenetega
# Date: 20-11-2024
# Language used: Python
# Description: To calculate mean, standard deviation, variance, min, max and sum of a 3x3 numpy array

import numpy as np

def calculate(list):

    # Catching Errors
    if len(list) < 9:
        raise ValueError("List must contain nine numbers")
            
    
    new_nd_array = np.array(list).reshape(3,3)

    calculations = {}

    # Mean
    mean_axis_0 = np.mean(new_nd_array, axis = 0).tolist()
    mean_axis_1 = np.mean(new_nd_array, axis = 1).tolist()
    mean = float(np.mean(new_nd_array))
    calculations["mean"] = [mean_axis_0, mean_axis_1, mean]

    # Variance
    var_axis_0 = np.var(new_nd_array, axis = 0).tolist()
    var_axis_1 = np.var(new_nd_array, axis = 1).tolist()
    variance = float(np.var(new_nd_array))
    calculations['variance'] = [var_axis_0, var_axis_1, variance]
    
    # Standard Deviation
    std_axis_0 = np.std(new_nd_array, axis = 0).tolist()
    std_axis_1 = np.std(new_nd_array, axis = 1).tolist()
    std = float(np.std(new_nd_array))
    calculations["standard deviation"] = [std_axis_0, std_axis_1, std]

    # Minimum Value
    min_axis_0 = np.min(new_nd_array, axis = 0).tolist()
    min_axis_1 = np.min(new_nd_array, axis = 1).tolist()
    minimum = float(np.min(new_nd_array))
    calculations["min"] = [min_axis_0, min_axis_1, minimum]

    # Maximum Value
    max_axis_0 = np.max(new_nd_array, axis = 0).tolist()
    max_axis_1 = np.max(new_nd_array, axis = 1).tolist()
    maximum = float(np.max(new_nd_array))
    calculations["max"] = [max_axis_0, max_axis_1, maximum]

    # Sum
    sum_axis_0 = np.sum(new_nd_array, axis = 0).tolist()
    sum_axis_1 = np.sum(new_nd_array, axis = 1).tolist()
    total = float(np.sum(new_nd_array))
    calculations["sum"] = [sum_axis_0, sum_axis_1, total]
    
    return calculations

print(calculate([0,1,2,3,4,5,6,7,8]))