# -*- coding: utf-8 -*-
"""Task_4.1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ICXAoZsfOMnkHSg0YRiskZIGbZ751EhM

##**Step 1: Mount Google Drive in Colab**
"""

from google.colab import drive
drive.mount('/content/drive')

"""##**Step 2: Load the dataset as a DataFrame**
The dataset is a CSV file located in my Google Drive.
"""

import pandas as pd

# Provide the path to the dataset
file_path = '/content/drive/My Drive/Asmaa_Task_4/WeatherDataset.csv'

# Load the dataset
df = pd.read_csv(file_path)

"""This step to make sure that the dataset is loaded correctly from google drive"""

df.head()

"""##**Step 3: Clean and preprocess the data**"""

# Separate numeric and non-numeric columns
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
non_numeric_cols = df.select_dtypes(exclude=['float64', 'int64']).columns

# Fill missing values in numeric columns with the mean
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Handle missing values in non-numeric columns (e.g., fill with mode or drop)
# Here, we'll fill missing values in non-numeric columns with the mode
for col in non_numeric_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Example: Handle incorrect data (e.g., outliers, incorrect types) for all columns
df = df[(df['Temperature (C)'] >= -50) & (df['Temperature (C)'] <= 50)]  # Temperature range
df = df[(df['Apparent Temperature (C)'] >= -50) & (df['Apparent Temperature (C)'] <= 50)]  # Apparent Temperature range
df = df[(df['Humidity'] >= 0) & (df['Humidity'] <= 100)]  # Humidity range
df = df[(df['Wind Speed (km/h)'] >= 0) & (df['Wind Speed (km/h)'] <= 200)]  # Wind Speed range
df = df[(df['Wind Bearing (degrees)'] >= 0) & (df['Wind Bearing (degrees)'] <= 360)]  # Wind Bearing range
df = df[(df['Visibility (km)'] >= 0) & (df['Visibility (km)'] <= 50)]  # Visibility range
df = df[(df['Pressure (millibars)'] >= 800) & (df['Pressure (millibars)'] <= 1200)]  # Pressure range

# Handle incorrect data for non-numeric columns
valid_precip_types = ['rain', 'snow']
valid_summaries = [
    'Partly Cloudy', 'Mostly Cloudy', 'Overcast', 'Foggy', 'Clear',
    'Breezy and Mostly Cloudy', 'Breezy and Overcast', 'Breezy and Partly Cloudy',
    'Windy and Partly Cloudy', 'Windy and Overcast', 'Light Rain', 'Drizzle', 'Rain'
]
valid_daily_summaries = [
    'Partly cloudy throughout the day.', 'Mostly cloudy throughout the day.',
    'Overcast throughout the day.', 'Foggy in the morning and evening.',
    'Clear throughout the day.', 'Breezy in the afternoon and mostly cloudy starting in the afternoon, continuing until evening.',
    'Breezy in the afternoon and overcast starting in the afternoon.', 'Breezy in the afternoon and partly cloudy starting in the afternoon, continuing until evening.',
    'Windy in the afternoon and partly cloudy starting in the afternoon, continuing until evening.', 'Windy in the afternoon and overcast starting in the afternoon.',
    'Light rain throughout the day.', 'Drizzle in the morning and afternoon.', 'Rain throughout the day.'
]

df = df[df['Precip Type'].isin(valid_precip_types)]
df = df[df['Summary'].isin(valid_summaries)]
df = df[df['Daily Summary'].isin(valid_daily_summaries)]

"""##**Step 4: Plot temperature over time**"""

import matplotlib.pyplot as plt
import seaborn as sns

# Convert 'Formatted Date' to datetime with UTC conversion
df['Formatted Date'] = pd.to_datetime(df['Formatted Date'], utc=True)

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Formatted Date', y='Temperature (C)')
plt.title('Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (C)')
plt.show()

"""##**Step 5: Create a histogram of temperature distribution**"""

plt.figure(figsize=(10, 6))
sns.histplot(df['Temperature (C)'], bins=30, kde=True)
plt.title('Temperature Distribution')
plt.xlabel('Temperature (C)')
plt.ylabel('Frequency')
plt.show()

"""##**Step 6: Plot a scatter plot of temperature vs. humidity**"""

plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='Temperature (C)', y='Humidity')
plt.title('Temperature vs. Humidity')
plt.xlabel('Temperature (C)')
plt.ylabel('Humidity')
plt.show()

"""##**Step 7: Generate a correlation heatmap**"""

plt.figure(figsize=(10, 6))

# Select only numeric columns for the correlation matrix
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
correlation_matrix = df[numeric_cols].corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

"""# **Correlation Heatmap Explanation**


---


####**The correlation heatmap displays the correlation coefficients between different features in the dataset. The correlation coefficient ranges from -1 to 1, where:**

- 1 indicates a perfect positive correlation: as one variable increases, the other also increases.
- -1 indicates a perfect negative correlation: as one variable increases, the other decreases.
- 0 indicates no correlation: the variables do not have any linear relationship.

###**In the heatmap:**
- Darker colors represent stronger correlations (positive or negative).

"""