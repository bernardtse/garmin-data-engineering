#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries 
import pandas as pd
import re
import numpy as np
import nbconvert


# In[2]:


# Load the dataset from the CSV file
df = pd.read_csv('../data/raw/Activities.csv')


# In[3]:


# Display the first few rows of the DataFrame to understand its structure
df.head()


# In[4]:


# Get a concise summary of the DataFrame, including the number of non-null values in each column
df.info()


# In[5]:


# Convert Date & Time to correct format
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S')
df.info()


# In[6]:


# Display statistical summaries of numeric columns
df.describe()


# In[7]:


def generate_alphanumeric_id(prefix, idx):
    """
    Generates an alphanumeric ID with a given prefix and index.
    
    Parameters:
    - prefix (str): The prefix for the ID.
    - idx (int): The numeric index for the ID.
    
    Returns:
    - str: An alphanumeric ID.
    """
    return f"{prefix}{idx:03d}"  # Pads the index with zeros, e.g., AT001

# Generate unique IDs for each activity type
activity_types = df['Activity Type'].unique()

# Generate Alphanumeric IDs
alphanumeric_ids = [generate_alphanumeric_id("AT", i+1) for i in range(len(activity_types))]

# Create a mapping DataFrame
activity_types_df = pd.DataFrame({
    'Activity Type ID': alphanumeric_ids,
    'Activity Type': activity_types
})


# Display the Activity Types table
activity_types_df


# In[8]:


# Export Activty Types to csv
activity_types_df.to_csv('../data/processed/activity_types.csv', encoding='utf8',index=False)


# In[9]:


# Drop columns where all values are 0
df = df.loc[:, (df != 0).any(axis=0)]

df.info()


# In[10]:


# Add an Activity ID column as a primary key
df['Activity ID'] = range(1, len(df) + 1)
df.tail()


# In[12]:


# Merge df with activity_types_df on "Activity Type" to include "Activity Type ID"
merged_df = pd.merge(df, activity_types_df, 
                         left_on='Activity Type', right_on='Activity Type', 
                         how='left')

merged_df.head(10)


# In[63]:


# Create the Activities Table - To record basic details about each activity.
activities_df = merged_df[['Activity ID','Activity Type ID', 'Date', 'Title']].copy()
activities_df.head()


# In[14]:


# Export Activty Types to csv
activities_df.to_csv('../data/processed/activities.csv', encoding='utf8',index=False)


# In[15]:


#Create Performance Metrics Table - To store specific performance metrics for deeper analysis of physical output.
performance_metrics_df = merged_df[['Activity ID','Activity Type ID', 'Distance', 'Calories', 'Time', 'Avg HR', 'Max HR', 'Aerobic TE', 'Avg Run Cadence', 'Avg Pace', 'Best Pace']]
performance_metrics_df.head(10)


# In[16]:


performance_metrics_df.info()


# In[17]:


# Use apply with a lambda function to concatenate 'Activity ID' and 'Activity Type ID' into 'Performance ID'
performance_metrics_df['Performance ID'] = performance_metrics_df.apply(lambda x: str(x['Activity ID']) + '_' + str(x['Activity Type ID']), axis=1)

# Display the first 10 rows to verify the 'Metric ID' column
performance_metrics_df.head(10)


# In[18]:


# Explicitly create a copy of the DataFrame or slice for modification
performance_metrics_df = performance_metrics_df.copy()

# Convert 'Distance', 'Calories', 'Aerobic TE', and 'Avg Run Cadence' to numeric types
performance_metrics_df['Distance'] = pd.to_numeric(performance_metrics_df['Distance'], errors='coerce')
performance_metrics_df['Calories'] = pd.to_numeric(performance_metrics_df['Calories'], errors='coerce')
performance_metrics_df['Aerobic TE'] = pd.to_numeric(performance_metrics_df['Aerobic TE'], errors='coerce')
performance_metrics_df['Avg Run Cadence'] = pd.to_numeric(performance_metrics_df['Avg Run Cadence'], errors='coerce')

# Check the DataFrame's info to confirm the conversions
performance_metrics_df.info()


# In[19]:


# Function to convert 'HH:MM:SS' to minutes
def convert_time_to_proportion(time_str):
    match = re.match(r'(\d{2}):(\d{2}):(\d{2})', time_str)
    if match:
        # Extract minutes and seconds
        hours, minutes, seconds = match.groups()
        total_seconds = int(hours) * 3600 + int(minutes) * 60 + int(seconds)
        # Convert to proportion of an hour
        return round(total_seconds /60,2)
    return None

# Apply the conversion function to the 'Time' column
performance_metrics_df['Time (minutes)'] = performance_metrics_df['Time'].apply(convert_time_to_proportion)


# In[20]:


performance_metrics_df


# In[21]:


# Function to convert 'MM:SS' to a proportion of a minute
def pace_to_proportion(pace_str):
    match = re.match(r'(\d+):(\d{2})', pace_str)
    if match:
        minutes, seconds = match.groups()
        total_seconds = int(minutes) * 60 + int(seconds)
        # Convert to proportion of a minute and round to 3 decimal places
        return round(total_seconds / 60, 2)
    return None

# Apply the conversion function to 'Avg Pace' and 'Best Pace'
performance_metrics_df['Avg Pace (min/km)'] = performance_metrics_df['Avg Pace'].apply(pace_to_proportion)
performance_metrics_df['Best Pace (min/km)'] = performance_metrics_df['Best Pace'].apply(pace_to_proportion)


# In[22]:


performance_metrics_df.info()


# In[65]:


performance_metrics_df = performance_metrics_df[['Performance ID','Activity ID', 'Activity Type ID', 'Distance','Calories', 'Time (minutes)', 'Avg HR', 'Max HR', 'Aerobic TE', 'Avg Run Cadence', 'Avg Pace (min/km)', 'Best Pace (min/km)']]
performance_metrics_df.head()


# In[25]:


# Export Performance Metrics to csv
performance_metrics_df.to_csv('../data/processed/performance_metrics.csv', encoding='utf8',index=False)


# In[32]:


# Create Lap Times and Misc Metrics Table - To provide insights into pacing, rest intervals, and overall activity duration
lap_metrics_df = merged_df[['Activity ID','Activity Type ID','Best Lap Time', 'Number of Laps', 'Distance.1', 'Moving Time', 'Elapsed Time']].copy()
lap_metrics_df.head()


# In[33]:


#Only retain metrics for AT001 and AT002 - Running and Treadmill Running 
filtered_lap_metrics_df = lap_metrics_df.loc[lap_metrics_df['Activity Type ID'].isin(['AT001', 'AT002'])]

# Display the first few rows of the filtered DataFrame
filtered_lap_metrics_df.head()


# In[35]:


# Generate a sequence of numbers starting from 1 up to the length of the DataFrame
lap_ids = range(1, len(filtered_lap_metrics_df) + 1)

# Concatenate "LAP" with the sequence of numbers to create the 'Lap ID' column
filtered_lap_metrics_df['Lap ID'] = ['LAP' + str(id) for id in lap_ids]

# If you want 'Lap ID' to be the first column, you can rearrange the columns as follows:
cols = ['Lap ID'] + [col for col in filtered_lap_metrics_df.columns if col != 'Lap ID']
filtered_lap_metrics_df = filtered_lap_metrics_df[cols]

# Display the first few rows to verify the 'Lap ID' column
filtered_lap_metrics_df.head()


# In[36]:


filtered_lap_metrics_df.info()


# In[37]:


# Convert 'Distance.1' to float
filtered_lap_metrics_df['Distance.1'] = pd.to_numeric(filtered_lap_metrics_df['Distance.1'], errors='coerce')

# Rename 'Distance.1' to 'Total Distance (km)'
filtered_lap_metrics_df.rename(columns={'Distance.1': 'Total Distance (km)'}, inplace=True)

# Create 'Lap Distance (km)' by dividing 'Total Distance (km)' by 'Number of Laps'
filtered_lap_metrics_df['Lap Distance (km)'] = filtered_lap_metrics_df['Total Distance (km)'] / lap_metrics_df['Number of Laps']

filtered_lap_metrics_df


# In[38]:


# Function to convert time strings to minutes using regex
def convert_time_str_to_minutes(time_str):
    # For 'Best Lap Time' format MM:SS.HH
    if '.' in time_str:
        match = re.match(r'(\d+):(\d{2}).(\d{2})', time_str)
        if match:
            minutes, seconds, hundredths = map(int, match.groups())
            return round(minutes + seconds / 60 + hundredths / 6000, 2)
    # For 'Moving Time' and 'Elapsed Time' format HH:MM:SS or MM:SS
    else:
        match = re.match(r'(\d+):(\d{2}):?(\d{2})?', time_str)
        if match:
            parts = match.groups()
            if len(parts) == 3 and parts[2] is not None:
                hours, minutes, seconds = map(int, parts)
                return round(hours * 60 + minutes + seconds / 60, 2)
            elif len(parts) >= 2:
                minutes, seconds = map(int, parts[:2])
                return round(minutes + seconds / 60, 2)
    return None

# Apply the conversion function
filtered_lap_metrics_df['Best Lap Time (min)'] = lap_metrics_df['Best Lap Time'].apply(convert_time_str_to_minutes)
filtered_lap_metrics_df['Moving Time (min)'] = lap_metrics_df['Moving Time'].apply(convert_time_str_to_minutes)
filtered_lap_metrics_df['Elapsed Time (min)'] = lap_metrics_df['Elapsed Time'].apply(convert_time_str_to_minutes)
filtered_lap_metrics_df.info()


# In[40]:


filtered_lap_metrics_df = filtered_lap_metrics_df[['Lap ID', 'Activity ID', 'Best Lap Time (min)', 'Number of Laps', 'Total Distance (km)', 'Lap Distance (km)','Moving Time (min)', 'Elapsed Time (min)']]
filtered_lap_metrics_df


# In[44]:


# Calculate Q1, Q3, and IQR for 'Best Lap Time (min)'
Q1 = filtered_lap_metrics_df['Best Lap Time (min)'].quantile(0.25)
Q3 = filtered_lap_metrics_df['Best Lap Time (min)'].quantile(0.75)
IQR = Q3 - Q1

# Define bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter rows where 'Best Lap Time (min)' is within the bounds
filtered_metrics_df = filtered_lap_metrics_df[(filtered_lap_metrics_df['Best Lap Time (min)'] >= lower_bound) & 
                                          (filtered_lap_metrics_df['Best Lap Time (min)'] <= upper_bound)]

# Display the shape or a sample of the filtered DataFrame to verify removal of outliers
filtered_metrics_df.info()


# In[67]:


filtered_metrics_df.head()


# In[46]:


# Export Lap Times Metrics to csv
filtered_metrics_df.to_csv('../data/processed/lap_metrics.csv',encoding='utf8',index=False)


# In[50]:


# Create the Elevation Metrics Table - To analyze how elevation impacts activity performance and effort.
elevation_metrics_df = merged_df[['Activity ID','Total Ascent', 'Total Descent', 'Min Elevation', 'Max Elevation']].copy()
elevation_metrics_df.head()


# In[51]:


# Replace '--' with np.nan in 'Total Ascent' and 'Total Descent' columns
elevation_metrics_df['Total Ascent'] = elevation_metrics_df['Total Ascent'].replace('--', np.nan)
elevation_metrics_df['Total Descent'] = elevation_metrics_df['Total Descent'].replace('--', np.nan)

# Drop rows where either 'Total Ascent' or 'Total Descent' is np.nan
elevation_metrics_df = elevation_metrics_df.dropna(subset=['Total Ascent', 'Total Descent'])

# Display the first few rows to verify that rows with '--' have been removed
elevation_metrics_df.head()


# In[52]:


# Reset the index of the DataFrame
elevation_metrics_df.reset_index(drop=True, inplace=True)

# Generate an alphanumeric primary key for each row
# The primary key will be in the format "EM" (for Elevation Metrics) followed by the new index number
elevation_metrics_df['Elevation Metric ID'] = elevation_metrics_df.index.to_series().apply(lambda x: f"EM{x+1}")

# If you want 'Elevation Metric ID' to be the first column, you can rearrange the columns
cols = ['Elevation Metric ID'] + [col for col in elevation_metrics_df.columns if col != 'Elevation Metric ID']
elevation_metrics_df = elevation_metrics_df[cols]

# Display the first few rows to verify the new 'Elevation Metric ID' column
elevation_metrics_df.head()


# In[53]:


elevation_metrics_df.info()


# In[56]:


# Then convert the column to float before converting to int64 to handle NaN values (pandas stores NaN as float)
elevation_metrics_df['Total Ascent'] = pd.to_numeric(elevation_metrics_df['Total Ascent'], errors='coerce').astype('Int64')
elevation_metrics_df['Total Descent'] = pd.to_numeric(elevation_metrics_df['Total Descent'], errors='coerce').astype('Int64')
elevation_metrics_df['Min Elevation'] = pd.to_numeric(elevation_metrics_df['Min Elevation'], errors='coerce').astype('Int64')
elevation_metrics_df['Max Elevation'] = pd.to_numeric(elevation_metrics_df['Max Elevation'], errors='coerce').astype('Int64')

# Display the DataFrame's info to verify the conversion
elevation_metrics_df.info()


# In[57]:


elevation_metrics_df


# In[58]:


# Export Elevation Metrics to csv
elevation_metrics_df.to_csv('../data/processed/elevation_metrics.csv',encoding='utf8',index=False)


# Tables below seem to have incomplete information - can be explored at a future date. 

# In[48]:


# Create the Swimming Metrics Table - Dedicated to swimming activities, capturing strokes and efficiency.
swimming_metrics_df = merged_df[['Activity ID','Total Strokes', 'Avg. Swolf', 'Avg Stroke Rate', 'Dive Time']].copy()
swimming_metrics_df.head()


# In[ ]:


#Use nbconvert to export noteboook to transform.py in the etl directory 
get_ipython().system('jupyter nbconvert --to script etl_test.ipynb --output-dir ../etl --output transform.py')

