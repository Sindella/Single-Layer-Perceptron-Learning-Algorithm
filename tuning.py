def tune(lenght):
    ask2 = int(input("Do you want to tune your model?\nType 1 - Tune\nType 2 - Use default settings\n"))
    weights = []
    if ask2 ==1:
        wei_init=float(input("What is your model's weights' initial value? (Default: 0.1) "))
        for i in range(0,lenght):
            weights.append(wei_init)
        lea_rate=float(input("What is your model's learning rate? (Default:0.01) "))
        ite_number=int(input("What is your model's max iteration number? (Default:100) "))
        error_tol= float(input("What is your model's error tolerance? (Default:0.001) "))
        with open("model.txt", "w") as data:
            data.write(str(lea_rate) + " " +  str(ite_number) + " " + str(error_tol)) 
            j=0
            for i in weights:
                j+=1
                data.write("\nweight" + str(j) + ": " + str(i))
        print("Model is tuned!\n")
    else:
        print("Model is not changed.\n")
    return 0