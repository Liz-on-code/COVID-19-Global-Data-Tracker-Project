# Step 2: Data Loading & Exploration
import pandas as pd

# Load the dataset
df = pd.read_csv("owid-covid-data.csv")

# Check the columns and the first few rows of the dataset
print(df.columns)  # To see the column names
print(df.head())   # Preview the first few rows

# Check for missing values
print(df.isnull().sum())  # Check missing values in each column
