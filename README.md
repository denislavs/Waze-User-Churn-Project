# Waze User Churn Analysis
______________________

## 1. Introduction 

This project is part of the Google Advanced Data Analytics Course on Coursera, focusing on user churn within Waze, a popular navigation app. The primary objective is to analyze user behavior and identify patterns contributing to user churn. The analysis involves data inspection, preparation, exploratory data analysis (EDA), and visualization to extract actionable insights for improving user retention.

The project answers key questions such as:  
• What are the distinguishing characteristics between users who churn and those who are retained?  
• How do user behaviors such as app usage frequency, drive distance, and engagement correlate with churn rates?   

## 2. Methodology

**Data Source**  
The dataset used in this analysis was provided through the Google Advanced Data Analytics Course on Coursera. It contains anonymized data on Waze users, including variables related to app usage, engagement, device type, and churn status.  

**Tools and Libraries**  
• Python: The primary language used for data manipulation, cleaning, and analysis.  
• Pandas: For handling dataframes and performing data manipulation tasks.  
• Matplotlib and Seaborn: For creating informative visualizations.  
• NumPy: For numerical computations.  
• Jupyter Notebook: For interactive analysis and documenting the code.  

**Analytical Approach**  
• Data Inspection and Cleaning:   
The dataset was inspected for missing values, data types, and outliers. Special attention was paid to the distribution of missing data, ensuring key variables (such as churn status) were ready for analysis.  
• Exploratory Data Analysis (EDA):   
Descriptive statistics and visualizations were used to uncover user behavior patterns, focusing particularly on differences between churned and retained users. Specific variables, such as driving frequency, kilometers driven, and device type, were examined in relation to churn.  
• Visualization:   
A series of visualizations were created to represent the distribution of users across devices, engagement levels, and churn status. The goal was to highlight trends and behaviors that could predict churn.   

## 3. Findings  

The Waze Churn Analysis revealed several important behavioral trends:  
• **Churned users** tend to drive more intensely but engage with the app less frequently, suggesting that Waze may not fully meet the needs of high-mileage drivers.  
• **Retained users** demonstrate more consistent, but less intense, usage patterns.  
• **Device type** does not appear to be a major factor in churn, with iPhone and Android users showing similar churn rates.  

**Users with Missing Data**  

![output_24_0](https://github.com/user-attachments/assets/cd679739-a692-479c-a3f0-135ae652f9b9)  

The dataset contains 700 missing values in the churn label column, with a greater number of iPhone users (447) than Android users (253) affected.  

**Device Proportions in Dataset vs. Missing Data**  

![output_30_0](https://github.com/user-attachments/assets/1b8b5ffb-6d19-4b1f-82d3-ff9e38b14667)  
Both device types (iPhone and Android) have a similar distribution between the overall dataset and users with missing values, suggesting that missing data is not strongly biased towards one device type.

**Churned vs. Retained Users**  

![output_34_0](https://github.com/user-attachments/assets/369b31b3-0eda-4990-8ce7-451b7c601a1c)  
The majority of users are retained (82.3%), while 17.7% have churned. This suggests that churn is notable but not overwhelming.

**Device Distribution for Churned vs. Retained Users**  

![output_52_0](https://github.com/user-attachments/assets/72708ea5-5fe0-4584-ad6c-b38d9d89dc7c)  
The device distribution between churned and retained users is almost identical, with iPhone users comprising approximately 65% of both groups. This indicates that device type alone is not a significant predictor of churn.

**Median Values Comparison**  

![output_37_0](https://github.com/user-attachments/assets/e1cc1243-f413-441b-ae49-6d065317a9b0)  
Churned users exhibited more intense driving behavior, covering significantly longer distances and engaging in more drives per day. However, they used the app less consistently, engaging with Waze on fewer days than retained users. Retained users, on the other hand, exhibited a more balanced and consistent usage pattern, driving shorter distances and spending less time per drive, but using the app on more days throughout the month.

**Kilometers and Drives per Driving Day**  

![output_46_0](https://github.com/user-attachments/assets/c34bfa57-145f-4f3b-83da-0d456c69a2b1)  
Churned users had a higher number of drives per driving day, suggesting that their app usage was concentrated into fewer, more intense sessions. This pattern of behavior suggests that the sample of churned users may include a significant proportion of long-haul truckers, whose driving habits involve longer, more demanding trips that may not align with typical Waze user patterns.

### **Key Insights of User Behavior**  
• **Churned vs. Retained Users**:   
Users who churned averaged about 3 more drives in the last month compared to retained users. However, retained users engaged with the app on twice as many days as churned users within the same period.  
• **Driving Distances**:   
The median churned user drove ~200 more kilometers and 2.5 more hours than the median retained user. This suggests that churned users had more intense driving activity but used the app less consistently.  
• **Insight into Churned User Profiles**:  
The churned users drove an average of 698 kilometers per day they used the app, which is ~240% more than the retained users. This substantial difference suggests that churned users are more likely to be long-haul drivers, such as truckers, whose specific needs may not be fully met by the Waze app.  

## 4. Business Impact

The insights derived from this analysis can play a crucial role in shaping Waze’s user retention strategies, particularly for high-mileage drivers such as long-haul truckers. By identifying the key behaviors that differentiate churned users from retained ones, Waze can take targeted actions to reduce churn and enhance the overall user experience.

• **Improving Retention**:   
Addressing the needs of churned users who drive frequently and cover longer distances can help Waze optimize the app for high-mileage drivers. Features tailored to long-haul drivers—such as enhanced trip planning or fuel efficiency tools—could potentially decrease churn among this key segment.  
• **Actionable Insights**:   
The analysis suggests that users who churn use the app in fewer, more intense sessions. Encouraging more consistent engagement through notifications or rewards for daily use could help shift churned users’ behavior toward more regular engagement, increasing retention rates.  
• **Targeted User Segmentation**:   
With churn behavior clearly linked to driving intensity and frequency, Waze can implement machine learning models to predict churn risk among specific user groups. This would allow for personalized retention campaigns, helping reduce churn by proactively addressing user needs.  

## 5. Conclusion  

The Waze Churn Analysis project, conducted as part of the Google Advanced Data Analytics Course on Coursera, successfully identified key patterns in user behavior that correlate with churn, providing valuable insights into how Waze can improve user retention. By thoroughly inspecting and preparing the dataset, performing exploratory data analysis, and using visualizations to uncover trends, we were able to draw important conclusions regarding user behavior and churn.

### Key Findings
The analysis highlighted several critical trends that distinguish churned users from retained users:  
• **Churned users** demonstrated more intense driving behaviors, covering significantly longer distances and engaging in more drives per day. However, they used the app less consistently, engaging with Waze on fewer days than retained users.  
• **Retained users**, on the other hand, exhibited a more balanced and consistent usage pattern, driving shorter distances and spending less time per drive, but using the app on more days throughout the month.  
• The analysis revealed that **churned users were likely high-mileage drivers**—potentially long-haul truckers—whose needs may not align with the features offered by the Waze app. These users exhibited disproportionately high usage on the days they engaged with the app but did not use it regularly, suggesting that their driving habits and preferences may not be fully supported by the app’s functionality.   
  
### Suggestions for Further Analysis
• **Segment Analysis**: Identify subgroups of users based on behavior patterns (e.g., long-haul drivers, commuters) and analyze churn rates within each group. This could reveal more granular insights and inform targeted retention strategies.  
• **Predictive Modeling**: Apply machine learning models (such as logistic regression or random forests) to predict churn based on user behavior data. This could help the Waze team proactively identify users at risk of churning and intervene with retention campaigns.  

These insights can inform data-driven retention strategies, enabling Waze to enhance the user experience and improve engagement.
