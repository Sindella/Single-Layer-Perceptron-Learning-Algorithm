import numpy as np
import data_generator
from sklearn.metrics import mean_absolute_error

def test(weight):
    data_generator.generate_data("testing data", "data_test.txt")

    data = []
    with open("data_test.txt", "r") as file:
        for line in file:
            data.append(line.strip().split(" "))

    ground_truth= []

    for i in range(0,len(data)):    #getting groundtruth values from testing data
        ground_truth.append(data[i][-1])
    
    y_true = np.array(ground_truth, dtype=float) #groundtruth values to test model
    y_pred = []                                  #predicted outputs from model
    weight=np.array(weight, dtype=float)

    for i in range(0,len(data)):  #generating model outputs
        data_arr=np.array(data[i][1:-1], dtype=float)
        y_pred.append(weight @ data_arr)

    mae = mean_absolute_error(y_true, y_pred)  # calculate mean absolute error
    print("Mean absolute error: ", mae)