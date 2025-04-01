import numpy as np

#if you have your custom data, you need to convert your data to this data syntax([data number], [values], [output])

def generate_data(data_type, data_name): #Watermelon Price Estimator (you can change this area to use perceptron for your problem)
    ask = input(f"Do you want to use your own data or generate new one for {data_type}?\nType 1 - Generate\nType 2 - Don't generate\n")
    if ask == "1":
        data_list = []
        m = int(input("Amount of Watermelons: "))  
        data_list.append(list(np.random.randint(200,700,m)/100))  # watermelon weights wide (kg)
        data_list.append(list(np.random.randint(0,100,m)/100))  # juiciness level of watermelons
        data_list.append(list(np.random.randint(0,100,m)/100))  # external damage level of watermelons
        price_list = []
        for i in range(0,m):
            price_list.append(round((data_list[0][i]*1.5)+(data_list[1][i]*1.2)-(data_list[2][i]*0.7),2)) # these are my estimations to generate groundtruth values
        data_list.append(price_list)
        with open(data_name, "w") as data: 
            for i in range(0, m):
                data.write(str(i+1) + " " + str(data_list[0][i])+ " " + str(data_list[1][i]) + " " + str(data_list[2][i])+ " " + str(data_list[3][i]) + "\n")
        print("Data is generated!\n")
    else:
        print("Data is not changed or generated.\n")
    
    return 0


