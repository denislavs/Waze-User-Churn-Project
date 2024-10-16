#!/usr/bin/env python
# coding: utf-8

# # **Waze Churn Analysis Project**
# **Course 2 - Get Started with Python**

# Welcome to the Waze Project!
# 
# Your Waze data analytics team is still in the early stages of their user churn project. Previously, you were asked to complete a project proposal by your supervisor, May Santner. You have received notice that your project proposal has been approved and that your team has been given access to Waze's user data. To get clear insights, the user data must be inspected and prepared for the upcoming process of exploratory data analysis (EDA).
# 
# A Python notebook has been prepared to guide you through this project. Answer the questions and create an executive summary for the Waze data team.

# # **Course 2 End-of-course project: Inspect and analyze data**
# 
# In this activity, you will examine data provided and prepare it for analysis. This activity will help ensure the information is,
# 
# 1.   Ready to answer questions and yield insights
# 
# 2.   Ready for visualizations
# 
# 3.   Ready for future hypothesis testing and statistical methods
# <br/>
# 
# **The purpose** of this project is to investigate and understand the data provided.
# 
# **The goal** is to use a dataframe contructed within Python, perform a cursory inspection of the provided dataset, and inform team members of your findings.
# <br/>
# 
# *This activity has three parts:*
# 
# **Part 1:** Understand the situation
# * How can you best prepare to understand and organize the provided information?
# 
# **Part 2:** Understand the data
# 
# * Create a pandas dataframe for data learning, future exploratory data analysis (EDA), and statistical activities
# 
# * Compile summary information about the data to inform next steps
# 
# **Part 3:** Understand the variables
# 
# * Use insights from your examination of the summary data to guide deeper investigation into variables
# 
# 
# <br/>
# 
# Follow the instructions and answer the following questions to complete the activity. Then, you will complete an Executive Summary using the questions listed on the PACE Strategy Document.
# 
# Be sure to complete this activity before moving on. The next course item will provide you with a completed exemplar to compare to your own work.
# 
# 

# # **Identify data types and compile summary information**
# 

# <img src="images/Pace.png" width="100" height="100" align=left>
# 
# # **PACE stages**

# Throughout these project notebooks, you'll see references to the problem-solving framework, PACE. The following notebook components are labeled with the respective PACE stages: Plan, Analyze, Construct, and Execute.

# <img src="images/Plan.png" width="100" height="100" align=left>
# 
# 
# ## **PACE: Plan**
# 
# Consider the questions in your PACE Strategy Document and those below to craft your response:

# ### **Task 1. Understand the situation**
# 
# *   How can you best prepare to understand and organize the provided driver data?
# 
# 
# *Begin by exploring your dataset and consider reviewing the Data Dictionary.*

#         Step 1: Familiarize Yourself with the Data Dictionary
#     Review the data dictionary to understand the purpose and description of each column. This provides context and helps in interpreting the data correctly.
# 
#         Step 2: Load the Data into a Pandas DataFrame
#     Read the dataset into a pandas DataFrame for ease of manipulation and analysis.
# 
#         Step 3: Perform Initial Data Inspection
#     Display the First Few Rows: Get a quick overview of the data.
#     Check Data Types: Ensure each column has the appropriate data type.
#     Check for Missing Values: Identify any columns with missing data.
#     Generate Descriptive Statistics: Summarize the central tendency, dispersion, and shape of the dataset’s distribution.
# 
#         Step 4: Visualize Key Metrics
#     Histograms: To understand the distribution of numerical variables.
#     Box Plots: To identify outliers and understand the spread of the data.
#     Scatter Plots: To explore relationships between numerical variables.
#     Correlation Heatmap: To visualize correlations between different metrics.
#     Bar Charts: To understand the distribution of categorical variables like verified_status.
# 
#         Step 5: Clean and Prepare Data
#     Handle Missing Values: Decide on strategies for dealing with missing data (e.g., imputation, removal).
#     Handle Outliers: Identify and decide how to handle outliers.
#     Feature Engineering: Create new features if necessary for better analysis and modeling.
# 
#         Step 6: Document Findings
#     Summarize Initial Observations: Document insights and observations from the initial data inspection.
#     Prepare for Further Analysis: Outline the next steps for more in-depth EDA, hypothesis testing, and statistical analysis.

# <img src="images/Analyze.png" width="100" height="100" align=left>
# 
# ## **PACE: Analyze**
# 
# Consider the questions in your PACE Strategy Document to reflect on the Analyze stage.

# ### **Task 2a. Imports and data loading**
# 
# Start by importing the packages that you will need to load and explore the dataset. Make sure to use the following import statements:
# 
# *   `import pandas as pd`
# 
# *   `import numpy as np`
# 

# In[1]:


# Import packages for data manipulation
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Then, load the dataset into a dataframe. Creating a dataframe will help you conduct data manipulation, exploratory data analysis (EDA), and statistical activities.
# 
# **Note:** As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

# In[2]:


# Load dataset into dataframe
df = pd.read_csv('waze_dataset.csv')


# ### **Task 2b. Summary information**
# 
# View and inspect summary information about the dataframe by **coding the following:**
# 
# 1.   df.head(10)
# 2.   df.info()
# 
# *Consider the following questions:*
# 
# 1. When reviewing the `df.head()` output, are there any variables that have missing values?
# 
# 2. When reviewing the `df.info()` output, what are the data types? How many rows and columns do you have?
# 
# 3. Does the dataset have any missing values?

# In[3]:


# Display the First Few Rows: Get a quick overview of the data
df.head(10)


# In[4]:


# Check Data Types: Ensure each column has the appropriate data type
df.info()


# **Task 2b**
# 
# **Question 1** When reviewing the df.head() output, are there any variables that have missing values?
# 
#     Based on the df.head() output shown in the image, there do not appear to be any missing values in the first few rows of the dataset. All columns seem to have values filled in for each of the displayed rows.
# 
#     However, to confirm whether any columns have missing values across the entire dataset, you would typically use the 
#     df.isnull().sum() method in Pandas, which provides a count of missing values in each column.
# 
# **Question 2** When reviewing the df.info() output, what are the data types? How many rows and columns do you have?
# 
#     There are 14,999 row entries and 13 columns: float64(3), int64(8), object(2).
# 
# **Question 3** Does the dataset have any missing values?
# 
#     Yes, the dataset has missing values. Specifically, the label column has 700 missing values (14,299 non-null entries out of a total of 14,999 rows). All other columns have 14,999 non-null entries, so they do not contain any missing values.
#     

# ### **Task 2c. Null values and summary statistics**
# 
# Compare the summary statistics of the 700 rows that are missing labels with summary statistics of the rows that are not missing any values.
# 
# **Question:** Is there a discernible difference between the two populations?
# 

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


# **Task 2c**
# 
# **Question:** Is there a discernible difference between the two populations?
# 
#     There are no significant or alarming differences between the two populations, suggesting that the missing labels may not be systematically associated with a particular pattern or behavior in the data. 
#     
#     >>> Slight differences in the mean and maximum values for certain metrics (e.g., total_sessions, driven_km_drives) could be further explored to determine if they have any meaningful impact.
# 

# ### **Task 2d. Null values - device counts**
# 
# Next, check the two populations with respect to the `device` variable.
# 
# **Question:** How many iPhone users had null values and how many Android users had null values?

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


# **Answer**: 447 iPhone users and 253 Android users had null values.

# Now, of the rows with null values, calculate the percentage with each device&mdash;Android and iPhone. You can do this directly with the [`value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html) function.

# In[78]:


# Calculate % of iPhone nulls and Android nulls

# Filter the rows with null values in the 'label' column
rows_with_nulls = df[df['label'].isnull()]

# Calculate the percentage of rows with each device type (Android, iPhone)
device_percentage_with_nulls = rows_with_nulls['device'].value_counts(normalize=True)
device_percentage_with_nulls


# How does this compare to the device ratio in the full dataset?

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


# The percentage of missing values by each device is consistent with their representation in the data overall.
# 
# There is nothing to suggest a non-random cause of the missing data.

# Examine the counts and percentages of users who churned vs. those who were retained. How many of each group are represented in the data?

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


# This dataset contains 82% retained users and 18% churned users.
# 
# Next, compare the medians of each variable for churned and retained users. The reason for calculating the median and not the mean is that you don't want outliers to unduly affect the portrayal of a typical user. Notice, for example, that the maximum value in the `driven_km_drives` column is 21,183 km. That's more than half the circumference of the earth!

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


# This offers an interesting snapshot of the two groups, churned vs. retained:
# 
# Users who churned averaged ~3 more drives in the last month than retained users, but retained users used the app on over twice as many days as churned users in the same time period.
# 
# The median churned user drove ~200 more kilometers and 2.5 more hours during the last month than the median retained user.
# 
# It seems that churned users had more drives in fewer days, and their trips were farther and longer in duration. Perhaps this is suggestive of a user profile. Continue exploring!

# Calculate the median kilometers per drive in the last month for both retained and churned users.
# 
# Begin by dividing the `driven_km_drives` column by the `drives` column. Then, group the results by churned/retained and calculate the median km/drive of each group.

# In[3]:


# Add a column to df called `km_per_drive`
df['km_per_drive'] = df['driven_km_drives'] / df['drives']

# Group by `label`, calculate the median, and isolate for km per drive
median_km_per_drive = df.groupby(['label']).median('km_per_drive')[['km_per_drive']]
median_km_per_drive


# The median retained user drove about one more kilometer per drive than the median churned user. How many kilometers per driving day was this?
# 
# To calculate this statistic, repeat the steps above using `driving_days` instead of `drives`.

# In[4]:


# Add a column to df called `km_per_driving_day`
df['km_per_driving_day'] = df['driven_km_drives'] / df['driving_days']

# Group by `label`, calculate the median, and isolate for km per driving day
median_km_per_drive = df.groupby(['label']).median('km_per_driving_day')[['km_per_driving_day']]
median_km_per_drive


# Now, calculate the median number of drives per driving day for each group.

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


# The median user who churned drove 698 kilometers each day they drove last month, which is almost ~240% the per-drive-day distance of retained users. The median churned user had a similarly disproporionate number of drives per drive day compared to retained users.
# 
# It is clear from these figures that, regardless of whether a user churned or not, the users represented in this data are serious drivers! It would probably be safe to assume that this data does not represent typical drivers at large. Perhaps the data&mdash;and in particular the sample of churned users&mdash;contains a high proportion of long-haul truckers.
# 
# In consideration of how much these users drive, it would be worthwhile to recommend to Waze that they **gather more data on these super-drivers**. It's possible that the reason for their driving so much is also the reason why the Waze app does not meet their specific set of needs, which may differ from the needs of a more typical driver, such as a commuter.

# Finally, examine whether there is an imbalance in how many users churned by device type.
# 
# Begin by getting the overall counts of each device type for each group, churned and retained.

# In[77]:


# For each label, calculate the number of Android users and iPhone users
df.groupby(['label','device']).count()[['ID']]


# Now, within each group, churned and retained, calculate what percent was Android and what percent was iPhone.

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


# The ratio of iPhone users and Android users is consistent between the churned group and the retained group, and those ratios are both consistent with the ratio found in the overall dataset.

# <img src="images/Construct.png" width="100" height="100" align=left>
# 
# ## **PACE: Construct**
# 
# **Note**: The Construct stage does not apply to this workflow. The PACE framework can be adapted to fit the specific requirements of any project.
# 
# 

# <img src="images/Execute.png" width="100" height="100" align=left>
# 
# ## **PACE: Execute**
# 
# Consider the questions in your PACE Strategy Document and those below to craft your response:

# ### **Task 3. Conclusion**
# 
# Recall that your supervisor, May Santer, asked you to share your findings with the data team in an executive summary. Consider the following questions as you prepare to write your summary. Think about key points you may want to share with the team, and what information is most relevant to the user churn project.
# 
# **Questions:**
# 
# 1. Did the data contain any missing values? How many, and which variables were affected? Was there a pattern to the missing data?
# 
# 2. What is a benefit of using the median value of a sample instead of the mean?
# 
# 3. Did your investigation give rise to further questions that you would like to explore or ask the Waze team about?
# 
# 4. What percentage of the users in the dataset were Android users and what percentage were iPhone users?
# 
# 5. What were some distinguishing characteristics of users who churned vs. users who were retained?
# 
# 6. Was there an appreciable difference in churn rate between iPhone users vs. Android users?
# 
# 
# 
# 

# **CONCLUSION**
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

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
