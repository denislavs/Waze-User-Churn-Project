**Waze Churn Analysis Project**

**1. Introduction**
The Waze Churn Analysis Project focuses on understanding user churn, aiming to identify patterns and behaviors that contribute to users discontinuing the use of the Waze app. Churn analysis is crucial to improve retention, understand user needs, and ultimately provide a better user experience. This project, part of a data analytics course, involves the inspection, cleaning, and analysis of Waze user data to extract meaningful insights about churn.

The primary objectives of this project include:

• Cleaning and preparing Waze user data for analysis.
• Exploring and analyzing data to answer key business questions about user churn.
• Visualizing trends and behavior patterns related to user churn to provide actionable insights.

**2. Methodology**
The project follows a systematic approach to data analysis:

Tools and Libraries
• Python: The programming language used to manipulate and analyze data.
• Jupyter Notebook: For interactive analysis and documentation.

Python Libraries
• Pandas: Used for data cleaning, filtering, and transformation.
• Matplotlib and Seaborn: For creating visualizations such as charts, graphs, and plots.
• NumPy: For numerical computations and operations.
• SciPy: Applied in performing statistical analysis.

Analytical Approach:
• Data Cleaning: 
The dataset was inspected for missing or inconsistent values, and necessary steps were taken to ensure it was suitable for analysis.
• Exploratory Data Analysis (EDA): 
Key aspects of the data were explored, and descriptive statistics were applied to uncover relationships between user engagement, device types, and churn rates. The analysis helped answer the following questions:
  • What are the key factors that correlate with user churn?
  • How do different user behaviors (such as app usage frequency and engagement) relate to churn?
  • Visualization: A set of visualizations was created to highlight trends and patterns in the dataset, particularly focusing on user behavior differences between retained and churned users.

**3. Findings**
The analysis yielded important insights into the behavior patterns of churned and retained users. Below are the key findings, supported by various visualizations.

3.1. User Engagement and Churn
Users with lower engagement, specifically those who used the app less frequently, showed higher churn rates. The proportion of churned users was significantly higher among users who had fewer driving days, shorter trip durations, and fewer kilometers per driving day.

3.2. Device Type and Churn
There was a notable difference in churn behavior between iPhone and Android users. The analysis showed that iPhone users constituted a larger share of both the overall user base and the users with missing values.

The number of users with missing data is higher among iPhone users than Android users, as shown in the bar chart below:
![output_24_0](https://github.com/user-attachments/assets/e424c213-b3b6-48f4-a4fe-c503d683e2be)

The comparison of device proportions for the overall dataset and users with missing values indicates that iPhone users are more prevalent in both categories.
![output_30_0](https://github.com/user-attachments/assets/3cd86b85-0ed3-4717-a33c-501ea6bf75e2)

3.3. Churned vs. Retained Users
The overall churn rate was 17.7%, with 82.3% of users being retained. This is highlighted in the pie chart below:
![output_34_0](https://github.com/user-attachments/assets/d6c3e677-7c3b-4bab-b10f-e9544451e712)

3.4. Comparison of User Behaviors Between Churned and Retained Users
When comparing the median values of various metrics such as kilometers per drive, driving days, and duration per trip, churned users exhibited lower engagement. For instance, churned users had a lower number of drives per driving day and fewer kilometers per driving day. This was visualized using bar plots.

Comparison of median values for key variables between churned and retained users:
![output_46_0](https://github.com/user-attachments/assets/fb4c238d-e036-4ed3-896e-489c3bbb452e)

Detailed bar charts comparing key driving metrics, such as kilometers per drive, kilometers per driving day, and drives per driving day:
![output_37_0](https://github.com/user-attachments/assets/09acf8f9-d1d5-43c0-b8f3-dd49e1e433dd)

3.5. Device Share Analysis
The analysis of device share among churned and retained users showed that iPhone users comprised the majority in both cases, although the proportion of Android users was slightly higher among churned users.

Device share comparison between churned and retained users:
![output_52_0](https://github.com/user-attachments/assets/f6c1d37e-6b54-456b-a288-af8f91cddd89)

These findings suggest that user engagement, as measured by driving frequency and app usage metrics, is a strong indicator of churn. Additionally, the prevalence of iPhone users in the dataset provides an interesting opportunity for targeted user retention strategies based on device type.

**4. Conclusion**
The Waze Churn Analysis Project successfully met its objectives of cleaning, analyzing, and visualizing Waze user data to understand churn patterns. By applying Python libraries and statistical methods, we were able to identify key factors contributing to churn, such as user engagement and device type.

Summary:
• Objective: To analyze user behavior and identify patterns related to user churn.
• Methods: Data cleaning, exploratory data analysis, and visualization using Python and its associated libraries.
Key Findings:
  • Lower user engagement correlates strongly with higher churn rates.
  • iPhone users make up a majority of both the churned and retained user bases.
  • Significant behavioral differences exist between churned and retained users, particularly in driving frequency and duration.

These insights can be used to inform future retention strategies and improve the overall user experience for Waze.
