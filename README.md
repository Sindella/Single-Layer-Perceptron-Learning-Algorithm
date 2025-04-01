# Frank-Rosenblatt-s-Perceptron-Learning-Algorithm
The basic perceptron learning algorithm that explains how artificial neurons work

This repository implements a Perceptron Learning Algorithm to classify and predict data. It includes generating training and testing data, training a Perceptron model, tuning hyperparameters, and evaluating model performance using Mean Absolute Error (MAE).

The model is specifically designed to predict watermelon prices based on various attributes such as weight, juiciness, and external damage. The synthetic data generated simulates different watermelon characteristics, and the trained model uses these attributes to estimate the price. At the end of the process, the trained model allows users to input their own watermelon characteristics and receive a predicted price.

## 📌 Perceptron Learning Algorithm Overview

The **Perceptron** is a type of artificial neural network that is used for binary classification problems. It operates using a simple learning rule:

1. Initialize weights randomly.
2. For each data point in the training set:
   - Compute the weighted sum of inputs.
   - Apply an activation function (usually a step function).
   - Update weights using the learning rule:
     
     ![image](https://github.com/user-attachments/assets/09ea43b5-6f0a-45bf-beb2-e07da35c8922)

     
     where:
     - w is the weight vector,
     - r is the learning rate,
     - y is the actual label,
     - f_w_t (x) is the predicted output,
     - x is the input vector.
3. Repeat until convergence or for a fixed number of iterations.

---

## 📂 Repository Structure

```
├── data_generator.py      # Generates synthetic training and testing data
├── tuning.py              # Allows users to set hyperparameters
├── perceptron.py          # Trains the Perceptron model
├── test_model.py          # Evaluates the trained model
├── README.md              # This documentation
```

---

## 🚀 How to Run the Project

### 1️⃣ Install Dependencies
Make sure you have Python installed along with NumPy and scikit-learn:
```bash
pip install numpy scikit-learn
```

### 2️⃣ Generate Data or use Custom Data
Run `perceptron.py`
```bash
python perceptron.py
```

Type 1 to the question to create synthetic training and testing datasets:
```bash
Do you want to use your own data or generate new one for training data?
Type 1 - Generate
Type 2 - Don't generate

Do you want to use your own data or generate new one for testing data?
Type 1 - Generate
Type 2 - Don't generate
```
This will generate `data_train.txt` and `data_test.txt` files.

### 3️⃣ Set Hyperparameters
Type 1 to the question to define the learning rate, iteration count, and error tolerance:
```bash
Do you want to tune your model?
Type 1 - Tune
Type 2 - Use default settings
```

### 4️⃣ Test the Model

Model will be tested automatically to evaluate model performance:

This will compute the **Mean Absolute Error (MAE)** for predictions.

![image](https://github.com/user-attachments/assets/83619ca6-bd21-4c79-971a-a848e6744bc0)
(default settings)

And finally: 
![image](https://github.com/user-attachments/assets/0bb3da53-af24-4b1d-b3eb-487cd7c4446f)


---

## 📊 Model Evaluation
We use **Mean Absolute Error (MAE)** to measure the model’s performance:
```python
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_true, y_pred)
```
- **Lower MAE** indicates better predictions.
- If MAE is **close to zero**, the model is highly accurate.

---

## 📜 License
This project is open-source and available under the **MIT License**.

