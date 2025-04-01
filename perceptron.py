import numpy as np
import data_generator
import tuning
import test_model

data_generator.generate_data("training data", "data_train.txt")  #generate random data if there is no custom data

data = []
with open("data_train.txt", "r") as file:
    for line in file:
        data.append(line.strip().split(" "))

tuning.tune(len(data[0])-2)     #tune to train better model

model = []
with open("model.txt", "r") as file: 
    for line in file:
        model.append(line.strip().split(" "))

weights=[]
for i in range(1,len(data[0])-1):
    weights.append(float(model[i][1]))

wei_arr=np.array(weights)
data = [[float(item) for item in sublist] for sublist in data]

for k in range(0,int(model[0][1])):  #perceptron training algorithm
    print("Iteration " + str(k+1))
    print(wei_arr)
    for i in range(0,len(data)):
        data_arr=np.array(data[i][1:-1])
        wei_arr_next=float(model[0][0])*(data[i][-1]-(wei_arr @ data_arr))*data_arr
        if np.linalg.norm(wei_arr_next-wei_arr)<float(model[0][2]):
            continue
        else:
            wei_arr+=wei_arr_next

weights = wei_arr.tolist()

with open("trained_model.txt", "w") as data:  #save the trained model's weights
            j=0
            for i in weights:
                j+=1
                data.write("\nweight" + str(j) + ": " + str(i))

test_model.test(weights) #testing the trained model
print("weights: ", wei_arr)

inputs= []
inputs.append(float(input("\nWeight of your watermelon(kg): ")))
inputs.append((float(input("\nJuiciness level of watermelons(0-10): ")))/10)
inputs.append((float(input("\nExternal damage level of watermelons(0-10): "))/10))
inputs = np.array(inputs)
print("\nYour watermelon's price is $", round(inputs @ wei_arr, 2), " \n")
