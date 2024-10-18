# Final Project

## Project Description
The telecom operator Interconnect would like to be able to forecast their churn of clients. If it's discovered that a user is planning to leave, they will be offered promotional codes and special plan options. Interconnect's marketing team has collected some of their clientele's personal data, including information about their plans and contracts.

## Interconnect's Services
Interconnect mainly provides two types of services:
1) Landline communication. The telephone can be connected to several lines simultaneously.
2) Internet. The network can be set up via a telephone line (DSL, _digital subscriber line_) or through a fiber optic cable.

Some other services the company provides include:
- Internet security: antivirus software (DeviceProtection) and a malicious website blocker (OnlineSecurity)
- A dedicated technical support line (TechSupport)
- Cloud file storage and data backup (OnlineBackup)
- TV streaming (StreamingTV) and a movie directory (StreamingMovies)
The clients can choose either a monthly payment or sign a 1- or 2-year contract. They can use various payment methods and receive an electronic invoice after a transaction.

## Data Description
The data consists of files obtained from different sources:
- `contract.csv` — contract information
- `personal.csv` — the client's personal data
- `internet.csv` — information about Internet services
- `phone.csv` — information about telephone services

In each file, the column **customerID** contains a unique code assigned to each client.

The contract information is valid as of February 1, 2020.

## Work Plan
**A) Initialization:** Import necessary libraries such as Pandas, NumPy, Matplotlib, Seaborn for data manipulation and visualization, and Scikit-learn for model building.

**B) Load Data:** Load all four CSV files (`contract.csv`, `personal.csv`, `internet.csv`, `phone.csv`) into separate DataFrames. Ensure that the data types are appropriate for analysis.

**C) Data Preprocessing:**
- Check for missing values and fill or drop them as necessary.
- Identify and remove duplicate rows.
- Convert any inappropriate data types to the correct format (e.g., dates, categorical variables).

**D) Exploratory Data Analysis:**
- Use visualizations (bar plots, histograms, box plots) to identify trends and relationships between customer attributes and churn rates.
- Look for correlations between features and the target variable.

**E) Model Training Preparation:**
- Split the dataset into training, validation and test sets.
- Encode categorical variables using techniques like one-hot encoding or label encoding as appropriate.
- Handle class imbalance through appropriate means.

**F) Model Training:**
- Select a variety of classification algorithms (e.g., Logistic Regression, Random Forest, Gradient Boosting).
- Use cross-validation to tune hyperparameters and select the best-performing model based on the AUC-ROC score.

**G) Model Analysis & Test:**
- Analyze the performance of each model using AUC-ROC and accuracy metrics.
- Choose the best model and retrain it on the entire training set, then evaluate it on the test set.
