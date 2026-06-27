# Student Performance Analysis

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load Dataset
data = pd.read_csv("student_performance.csv")


# Display Dataset Overview
print("----- Dataset Overview -----")

print("\nFirst 5 Rows:")
print(data.head())

print("\nDataset Shape:")
print(data.shape)

print("\nColumn Names:")
print(data.columns)

print("\nDataset Information:")
print(data.info())

print("\nStatistical Summary:")
print(data.describe())


# Data Cleaning

print("\n----- Data Cleaning -----")

print("\nMissing Values:")
print(data.isnull().sum())

print("\nDuplicate Rows:")
print(data.duplicated().sum())


# Remove Duplicate Values

data = data.drop_duplicates()


# Remove Unnecessary Column

data = data.drop("StudentID", axis=1)

print("\nColumns after cleaning:")
print(data.columns)


# Identify Numerical and Categorical Columns

numerical_columns = []
categorical_columns = []

for col in data.columns:
    if data[col].dtype in ['int64','float64']:
        numerical_columns.append(col)
    else:
        categorical_columns.append(col)


print("\nNumerical Columns:")
print(numerical_columns)


print("\nCategorical Columns:")
print(categorical_columns)



# Correlation Analysis

print("\n----- Correlation -----")

print(data.corr(numeric_only=True))


# Heatmap

plt.figure(figsize=(8,5))

sns.heatmap(
    data.corr(numeric_only=True),
    annot=True
)

plt.title("Correlation Heatmap")

plt.show()



# Distribution Plot

for col in numerical_columns:

    plt.figure(figsize=(6,4))

    sns.histplot(
        data[col],
        kde=True
    )

    plt.title(f"Distribution of {col}")

    plt.show()


print("\n----- Project Completed Successfully -----")

