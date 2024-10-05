# Import pandas
import pandas as pd

# Load the dataset (ensure the correct path to your CSV file)
df = pd.read_csv('/Users/shainazsultana/Downloads/Titanic.csv')  # Use the correct path

# Display the first few rows of the dataset
print("Initial Data:")
print(df.head())

# Data Cleaning
# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Drop rows with missing values in 'Age' and 'Embarked' columns
df_cleaned = df.dropna(subset=['Age', 'Embarked'])

# Verify missing values after cleaning
print("\nMissing values after cleaning:")
print(df_cleaned.isnull().sum())

# Analyze Metrics
# Total number of passengers
total_passengers = df_cleaned.shape[0]
print(f"\nTotal number of passengers: {total_passengers}")

# Percentage of survivors
total_survivors = df_cleaned['Survived'].sum()
percentage_survivors = (total_survivors / total_passengers) * 100
print(f"Percentage of survivors: {percentage_survivors:.2f}%")

# Average fare by survival status
average_fare = df_cleaned.groupby('Survived')['Fare'].mean()
print("\nAverage fare by survival status:")
print(average_fare)
