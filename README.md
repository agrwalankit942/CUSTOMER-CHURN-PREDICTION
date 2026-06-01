# CUSTOMER-CHURN-PREDICTION
Customer churn refers to the loss of customers when they stop using a company's products or services.
# Customer Churn Prediction – Comprehensive Insights and Conclusion

## Executive Summary

This project aimed to identify customers who are likely to discontinue telecom services using machine learning techniques. Through extensive data preprocessing, exploratory data analysis (EDA), feature engineering, correlation analysis, and predictive modeling, several important patterns influencing customer churn were identified. Two classification models, Logistic Regression and Random Forest, were developed and evaluated, with Random Forest delivering the best overall performance.

---

# Key Business Insights

## 1. Overall Customer Churn Rate

The analysis revealed that approximately **26.54% of customers churned**, while **73.46% remained with the company**.

### Business Implication

Although the majority of customers remain loyal, more than one out of every four customers leaves the service. This represents a significant revenue risk and highlights the importance of proactive customer retention strategies.

---

## 2. Contract Type is a Major Driver of Churn

Contract analysis showed substantial differences in churn rates:

| Contract Type  | Churn Rate |
| -------------- | ---------- |
| Month-to-Month | 42.71%     |
| One Year       | 11.27%     |
| Two Year       | 2.83%      |

### Key Finding

Customers on month-to-month contracts are dramatically more likely to churn than customers with long-term contracts.

### Business Recommendation

* Encourage customers to migrate to annual or multi-year plans.
* Provide discounts and loyalty benefits for long-term contracts.
* Offer retention incentives before contract renewal periods.

---

## 3. Customer Tenure Strongly Influences Churn

Tenure-based analysis revealed:

| Tenure Group | Churn Rate |
| ------------ | ---------- |
| 0–12 Months  | 48.28%     |
| 12–24 Months | 29.51%     |
| 24–48 Months | 20.87%     |
| 48–60 Months | 15.00%     |
| 60–72 Months | 8.30%      |

### Key Finding

New customers are significantly more likely to leave, while long-term customers demonstrate much higher loyalty.

### Business Recommendation

* Focus retention campaigns on customers during their first year.
* Improve onboarding experiences.
* Conduct early customer satisfaction surveys.

---

## 4. Monthly Charges Affect Churn Behavior

The average monthly charges were:

* Customers who stayed: **$61.27**
* Customers who churned: **$74.44**

### Key Finding

Customers who churned paid approximately **$13 more per month** than customers who remained.

### Business Recommendation

* Review pricing structures.
* Introduce personalized discount plans.
* Provide additional value-added services for premium customers.

---

## 5. Correlation Analysis Findings

Correlation analysis identified the following relationships with churn:

| Feature         | Correlation with Churn |
| --------------- | ---------------------- |
| MonthlyCharges  | +0.193                 |
| AvgMonthlySpend | +0.192                 |
| TotalCharges    | -0.199                 |
| Tenure          | -0.352                 |

### Key Findings

* **Tenure has the strongest negative correlation with churn.**
* **MonthlyCharges have the strongest positive correlation with churn.**
* Customers with longer relationships are less likely to churn.
* Higher monthly bills increase churn risk.

### Business Interpretation

Customer loyalty increases over time, while higher recurring costs create dissatisfaction and increase the likelihood of customer attrition.

---

## 6. Data Quality and Preprocessing Insights

Several preprocessing challenges were successfully addressed:

* Missing values in TotalCharges were handled.
* Infinite values generated during AvgMonthlySpend calculation were corrected.
* Skewness analysis confirmed no severe skewness after cleaning.
* Feature scaling was applied for Logistic Regression.
* The dataset contained no missing or infinite values before modeling.

### Key Outcome

The dataset was transformed into a clean, consistent, and model-ready format suitable for machine learning analysis.

---

## 7. Logistic Regression Model Insights

### Model Performance

* Training Accuracy: **81.08%**
* Testing Accuracy: **79.70%**

### Important Predictors Identified

* InternetService_Fiber optic
* StreamingTV
* StreamingMovies
* PaperlessBilling
* Electronic Check Payment Method

### Interpretation

Customers using fiber optic services, streaming services, paperless billing, and electronic payment methods showed increased churn tendencies.

---

## 8. Random Forest Model Insights

### Model Performance

* Training Accuracy: **84.03%**
* Testing Accuracy: **80.55%**

Random Forest achieved the highest predictive performance among the evaluated models.

### Top Feature Importance Rankings

1. Tenure
2. TotalCharges
3. AvgMonthlySpend

### Interpretation

Customer longevity and spending-related characteristics are the most influential factors in predicting churn behavior.

### Business Value

Random Forest effectively captures complex relationships between customer characteristics and churn risk, making it suitable for deployment in customer retention systems.

---

# Comparative Model Analysis

| Metric            | Logistic Regression | Random Forest |
| ----------------- | ------------------- | ------------- |
| Training Accuracy | 81.08%              | 84.03%        |
| Testing Accuracy  | 79.70%              | 80.55%        |

### Observation

Random Forest slightly outperformed Logistic Regression and demonstrated stronger capability in capturing non-linear customer behavior patterns.

Therefore, Random Forest was selected as the final predictive model.

---

# Final Conclusion

The Customer Churn Prediction project successfully developed a machine learning framework capable of identifying customers at risk of leaving telecom services. Through comprehensive exploratory data analysis and predictive modeling, several critical churn drivers were identified.

The analysis revealed that contract type, tenure, monthly charges, and customer spending behavior are the most influential factors affecting churn. Customers with month-to-month contracts, shorter tenure, and higher monthly charges were found to be significantly more likely to discontinue services.

Among the machine learning models evaluated, Random Forest achieved the best performance with a testing accuracy of approximately 80.55%, making it the preferred model for churn prediction. Feature importance analysis further confirmed that customer tenure and spending-related attributes are the strongest indicators of future churn behavior.

The developed system can help organizations proactively identify high-risk customers and implement targeted retention strategies such as loyalty programs, personalized pricing plans, contract upgrades, and customer engagement initiatives. By leveraging predictive analytics, businesses can reduce customer attrition, improve customer satisfaction, and enhance long-term profitability.

Overall, this project demonstrates the practical application of data science and machine learning techniques in solving real-world customer retention challenges and supporting data-driven business decision-making.
