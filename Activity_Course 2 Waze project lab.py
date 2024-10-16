#!/usr/bin/env python
# coding: utf-8

# # **Waze Churn Analysis Project**
# **Course 2 - Get Started with Python**


# In[1]:


# Import packages for data manipulation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Load dataset into dataframe
df = pd.read_csv('waze_dataset.csv')


# ### **Summary information**


# In[3]:


# Display the First Few Rows: Get a quick overview of the data
df.head(10)


# In[4]:


# Check Data Types: Ensure each column has the appropriate data type
df.info()


# In[11]:


# Isolate rows with null values
rows_with_nulls = df[df['label'].isnull()]

# Display summary stats of rows with null values
rows_with_nulls.describe()


# In[12]:


# Isolate rows without null values
rows_without_nulls = df[df['label'].notnull()]

# Display summary stats of rows without null values
rows_without_nulls.describe()


# ### **Null values - device counts**
# 


# In[49]:


# Get count of null values by device
null_counts_by_device = df[df['label'].isnull()].groupby('device').size()
null_counts_by_device


# In[4]:


# Data
devices = ['iPhone', 'Android']
counts = [447, 253]

# Plotting the bar chart
plt.figure(figsize=(7, 5))
plt.bar(devices, counts, color=['slateblue', 'lightgreen'])

# Adding title and labels
plt.title('Number of Users with Null Values')
plt.xlabel('Device')
plt.ylabel('Number of Users')

# Display the plot
plt.show()


# In[78]:


# Calculate % of iPhone nulls and Android nulls

# Filter the rows with null values in the 'label' column
rows_with_nulls = df[df['label'].isnull()]

# Calculate the percentage of rows with each device type (Android, iPhone)
device_percentage_with_nulls = rows_with_nulls['device'].value_counts(normalize=True)
device_percentage_with_nulls



# In[79]:


# Calculate % of iPhone users and Android users in full dataset
device_percentage = df['device'].value_counts(normalize=True)
device_percentage


# In[4]:


# Data
devices = ['iPhone', 'Android']
overall = [0.644843, 0.355157]
missing = [0.638571, 0.361429]

# Plotting
bar_width = 0.35
indices = np.arange(len(devices))

plt.figure(figsize=(10, 6))
plt.bar(indices, overall, bar_width, label='Overall Dataset', color='slateblue')
plt.bar(indices + bar_width, missing, bar_width, label='Missing Values', color='lightgreen')

plt.title('Comparison of Device Proportions')
plt.xlabel('Device')
plt.ylabel('Proportion')
plt.xticks(indices + bar_width / 2, devices)
plt.legend()
plt.show()


# In[83]:


# Calculate counts of churned vs. retained
label_counts = df['label'].value_counts()
print(label_counts)
print('')

label_percentages = df['label'].value_counts(normalize=True)
print(label_percentages)


# In[20]:


# Data for the pie chart
labels = ['Retained', 'Churned']
sizes = [0.822645, 0.177355]
colors = ['lightgreen', 'slateblue']  # Colors for each slice

# Plotting the pie chart
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)

# Adding a title
plt.title('Proportion of Retained vs. Churned Users')

# Display the plot
plt.show()


# In[46]:


# Calculate median values of all columns for churned and retained users
df.groupby(['label']).median()


# In[17]:


# Data preparation
labels = ['Sessions', 'Drives', 'Total Sessions', 'Days After Onboarding', 
          'Navigations Fav1', 'Navigations Fav2', 'Driven KM Drives', 
          'Duration Minutes Drives', 'Activity Days', 'Driving Days']

churned_medians = [59, 50, 164.33904, 1321, 84.5, 11, 3652.6557, 1607.1838, 8, 6]
retained_medians = [56, 47, 157.58676, 1843, 68, 9, 3464.6846, 1458.0461, 17, 14]

x = np.arange(len(labels))  # Label locations
width = 0.35  # Width of the bars

# Plotting
fig, ax = plt.subplots(figsize=(14, 7))
bars1 = ax.bar(x - width/2, churned_medians, width, label='Churned', color='slateblue')
bars2 = ax.bar(x + width/2, retained_medians, width, label='Retained', color='lightgreen')

# Adding labels and title
ax.set_xlabel('Variables')
ax.set_ylabel('Median Value')
ax.set_title('Comparison of Median Values for Churned and Retained Users')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha="right")
ax.legend()

# Adding the median values on top of the bars
for bar in bars1:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.05, round(yval, 2), ha='center', va='bottom')
for bar in bars2:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.05, round(yval, 2), ha='center', va='bottom')

plt.tight_layout()
plt.show()


# In[3]:


# Add a column to df called `km_per_drive`
df['km_per_drive'] = df['driven_km_drives'] / df['drives']

# Group by `label`, calculate the median, and isolate for km per drive
median_km_per_drive = df.groupby(['label']).median('km_per_drive')[['km_per_drive']]
median_km_per_drive


# In[4]:


# Add a column to df called `km_per_driving_day`
df['km_per_driving_day'] = df['driven_km_drives'] / df['driving_days']

# Group by `label`, calculate the median, and isolate for km per driving day
median_km_per_drive = df.groupby(['label']).median('km_per_driving_day')[['km_per_driving_day']]
median_km_per_drive


# In[8]:


# Add a column to df called `drives_per_driving_day`
df['drives_per_driving_day'] = df['drives'] / df['driving_days']

# Group by `label`, calculate the median, and isolate for drives per driving day
median_km_per_drive = df.groupby(['label']).median('drives_per_driving_day')[['drives_per_driving_day']]
median_km_per_drive


# In[9]:


# Group by `label`, calculate the median for both `km_per_driving_day` and `drives_per_driving_day`
medians = df.groupby('label').aggregate({'km_per_driving_day': 'median', 'drives_per_driving_day': 'median'})
medians


# In[7]:


# Data
labels = ['Churned', 'Retained']
km_per_drive = [74.109416, 75.014702]
km_per_driving_day = [697.541999, 289.549333]
drives_per_driving_day = [10, 4.0625]

# X locations for the groups
x = np.arange(len(labels))

# Width of bars
width = 0.8

# Create subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 6))

# First bar chart: km_per_drive
axs[0].bar(x, km_per_drive, width, color=['slateblue', 'lightgreen'])
axs[0].set_title('KM per Drive')
axs[0].set_xticks(x)
axs[0].set_xticklabels(labels)
axs[0].set_ylabel('KM per Drive')

# Second bar chart: km_per_driving_day
axs[1].bar(x, km_per_driving_day, width, color=['slateblue', 'lightgreen'])
axs[1].set_title('KM per Driving Day')
axs[1].set_xticks(x)
axs[1].set_xticklabels(labels)
axs[1].set_ylabel('KM per Driving Day')

# Third bar chart: drives_per_driving_day
axs[2].bar(x, drives_per_driving_day, width, color=['slateblue', 'lightgreen'])
axs[2].set_title('Drives per Driving Day')
axs[2].set_xticks(x)
axs[2].set_xticklabels(labels)
axs[2].set_ylabel('Drives per Driving Day')

# Adjust layout
plt.tight_layout()
# Show the plot
plt.show()


# In[77]:


# For each label, calculate the number of Android users and iPhone users
df.groupby(['label','device']).count()[['ID']]


# In[90]:


# For each label, calculate the percentage of Android users and iPhone users
df.groupby('label')['device'].value_counts(normalize=True)


# In[5]:


# Data
labels = ['iPhone', 'Android']
churned_sizes = [1645, 891]
retained_sizes = [7580, 4183]

# Colors
colors = ['slateblue', 'lightgreen']

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Pie chart for churned users
axs[0].pie(churned_sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
axs[0].set_title('Device Share for Churned Users')

# Pie chart for retained users
axs[1].pie(retained_sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
axs[1].set_title('Device Share for Retained Users')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()



# **FINDINGS**
# 
# **1. Did the data contain any missing values? How many, and which variables were affected? Was there a pattern to the missing data?** 
# 
# Yes, the dataset has missing values. Specifically, the label column has 700 missing values (14,299 non-null entries out of a total of 14,999 rows). All other columns have 14,999 non-null entries, so they do not contain any missing values.
# 
# There are no significant or alarming differences between the two populations, suggesting that the missing labels may not be systematically associated with a particular pattern or behavior in the data.
# 
# **2. What is a benefit of using the median value of a sample instead of the mean?**
# 
# The median is less sensitive to outliers and skewed data, providing a more accurate measure of central tendency for distributions that are not symmetric or contain extreme values.
# 
# **3. Did your investigation give rise to further questions that you would like to explore or ask the Waze team about?**
# 
# It would be worthwhile to gather more data on the super-drivers who churned, as perhaps the data contain a high proportion of long-haul truckers. It's possible that the reason for their driving so much is also the reason why the Waze app does not meet their specific set of needs, which may differ from the needs of a more typical driver, such as a commuter.
# 
# **4. What percentage of the users in the dataset were Android users and what percentage were iPhone users?**
# 
# The percentage of Android users is 35.5%, while the iPhone users represent 64.5% of the population. The ratio is consistent between the churned group and the retained group, suggesting that the device type does not play a significant influence.
# 
# **5. What were some distinguishing characteristics of users who churned vs. users who were retained?**
# 
# Activity Intensity: Churned users were more intense in their usage, averaging more drives, longer distances, and longer durations per day than retained users. Specifically, churned users drove about 200 kilometers and 2.5 hours more than retained users during the last month.
# 
# Usage Frequency: Retained users used the app on over twice as many days as churned users, indicating more consistent engagement, even though their individual drives were shorter in both distance and duration.
# 
# Driving Behavior: Churned users drove further and longer on the days they used the app, with each drive day involving significantly more kilometers and drives compared to retained users.
# 
# **6. Was there an appreciable difference in churn rate between iPhone users vs. Android users?**
# 
# The churn rates are very similar between Android and iPhone users (approximately 18%), with iPhone users having a slightly higher churn rate. This difference is minimal, indicating that the churn rate is relatively consistent across device types.
