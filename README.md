# Frank-Rosenblatt-s-Perceptron-Learning-Algorithm
The basic perceptron learning algorithm that explains how artificial neurons work

This repository implements a Perceptron Learning Algorithm to classify and predict data. It includes generating training and testing data, training a Perceptron model, tuning hyperparameters, and evaluating model performance using Mean Absolute Error (MAE).

## 📌 Perceptron Learning Algorithm Overview

The **Perceptron** is a type of artificial neural network that is used for binary classification problems. It operates using a simple learning rule:

1. Initialize weights randomly.
2. For each data point in the training set:
   - Compute the weighted sum of inputs.
   - Apply an activation function (usually a step function).
   - Update weights using the learning rule:
     
     \[ w_{new} = w_{old} + \eta (y_{true} - y_{pred}) x \]
     
     where:
     - \(w\) is the weight vector,
     - \(\eta\) is the learning rate,
     - \(y_{true}\) is the actual label,
     - \(y_{pred}\) is the predicted output,
     - \(x\) is the input vector.
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

### 4️⃣ Train the Perceptron Model
Run `perceptron.py` to train the model using the data:
```bash
python perceptron.py
```
The trained model is saved in `trained_model.txt`.

### 5️⃣ Test the Model
Model will be tested automatically to evaluate model performance:

This will compute the **Mean Absolute Error (MAE)** for predictions.

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

