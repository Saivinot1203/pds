# Import required libraries
import pandas as pd

# Load the dataset from the specified path
data_file_path = '/content/Frailty_Data.csv'  # Update with your file path
data = pd.read_csv("/content/raw_frailty_dataa.csv"))

# Show the initial rows of the dataset
print(data.head())

# Check for missing entries
print(data.isnull().sum())

# Data Cleaning
# Map 'Frailty' values to numerical format
data['Frailty'] = data['Frailty'].map({'N': 0, 'Y': 1})

# Verify the data types
print(data.dtypes)

# Save the cleaned dataset to a new file
cleaned_data_file_path = '/content/r"/content/raw_frailty_dataa.csv")'  # Update with your file path
data.to_csv(cleaned_data_file_path, index=False)