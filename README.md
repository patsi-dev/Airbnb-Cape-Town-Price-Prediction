# Airbnb-Cape-Town-Price-Prediction
## Business Understanding
Travelers using Airbnb in Cape Town often face difficulties finding fair and consistent prices for accommodation. The city’s tourism scene changes throughout the year, especially during peak seasons. Prices can rise sharply, while in quieter months, rates drop unpredictably. Different neighborhoods also have their own unique attractions and price ranges, which makes comparing options even more confusing.
As a result, many clients end up paying more than the true value of their stay or miss out on affordable and high-quality options. The lack of pricing transparency and consistency creates frustration for travelers trying to plan their trips and manage their budgets. This project seeks to address that problem by improving how prices are determined, ensuring that clients can access more accurate, fair, and reliable accommodation rates that reflect real market conditions in Cape Town.

**Main Objective**: To develop an accurate and interpretable machine learning system to predict optimal Airbnb listing prices in Cape Town, providing hosts with data-driven pricing recommendations and insights.
### Stakeholder Value
- **Airbnb Clients:**
Gain access to fairer and more accurate accommodation prices, helping them make better booking decisions.

- **Airbnb Hosts:**
Benefit from data-driven insights that can potentially increase revenue by 15-25% through optimized pricing strategies.

- **Platform Efficiency:**
Improved pricing stability and market transparency, reducing price volatility across listings.

- **Tourism Industry:**
Enhanced understanding of Cape Town’s accommodation trends and tourism dynamics.

- **Research Community:**
Valuable contribution to the study of the African sharing economy and its emerging market applications.
## Data Understanding
The dataset is from [Inside Airbnb Website](https://insideairbnb.com/get-the-data/), which was last updated on September 28th, 2025. Kindly scroll to Cape Town. There were a total of 7 Cape Town datasets, but we worked with listings.csv. It had all the columns and information from the other datasets. The dataset:
- 79 columns and 26,877 columns
- A lot of missing values.

Some of the columns include:

**Location & Geographic Data**

- `latitude`, `longitude`: Complete geographic coordinates
- `neighbourhood_cleansed`: Complete neighborhood data
- Multiple geographic identifiers available

**Property Characteristics**

- `property_type`, `room_type`: Complete categorical data
- `accommodates`, `bathrooms`, `bedrooms`, `beds`: Capacity metrics
- `amenities`: Text field with listing amenities

**Host Information**

- `host_since`: Host join date (complete)
- `host_is_superhost`: Superhost status (95.9% complete)
- `host_response_rate`, `host_acceptance_rate`: Response metrics
- Multiple host verification and listing count metrics

**Pricing & Revenue Data**

- `price`: Primary target variable (needs cleaning)
- `estimated_revenue_l365d`: Potential secondary target
- Availability metrics: `30/60/90/365 day availability`

**Review & Rating System**

- `review_scores_rating` and sub-scores: Multiple rating dimensions
- `number_of_reviews`: Review volume metrics
- `reviews_per_month`: Review frequency

Some Exploratory Data Analysis (EDA) was done
<p align = 'center'>Univariate Analysis</p>

![Analysis 4](https://github.com/patsi-dev/Airbnb-Cape-Town-Price-Prediction/blob/ivy/images/Screenshot%20(139).png)

<p align = 'center'>Bivariate Analysis</p>

![Analysis 5](https://github.com/patsi-dev/Airbnb-Cape-Town-Price-Prediction/blob/ivy/images/Screenshot%20(141).png)

<p align = 'center'>Linearity</p>

![Analysis 6](https://github.com/patsi-dev/Airbnb-Cape-Town-Price-Prediction/blob/ivy/images/Screenshot%20(140).png)

## Data Preparation
The dataset underwent several cleaning and transformation steps to ensure quality and reliability before modeling.

**Handling Missing Values:**
Missing values were carefully filled, and a few rows were dropped due to the small number of null entries. This helped maintain data integrity without losing valuable information.

**Duplicate and Placeholders Check:**
No duplicate records were found, confirming that each listing in the dataset was unique.

**Outlier Treatment:**
<p align = 'center'>Outliers</p>

![Analysis 2](https://github.com/patsi-dev/Airbnb-Cape-Town-Price-Prediction/blob/ivy/images/Screenshot%20(143).png)
Outliers were capped since some were genuine (reflecting real, high-value listings), while others were errors or extreme values that could distort model performance.
<p align = 'center'> Price outliers (Before Vs. After)</p>

![Analysis 3](https://github.com/patsi-dev/Airbnb-Cape-Town-Price-Prediction/blob/ivy/images/Screenshot%20(142).png)
**Feature engineering** involved creating geospatial features, including distance to major landmarks such as the V&A Waterfront, Table Mountain, and nearby beaches, host-based features, including host experience level, responsiveness, and superhost status, were included to reflect trust and reliability factors influencing price, among other features. 

## Modelling
We tested five different models to find the one that best predicts Airbnb prices in Cape Town. Each model has its own way of learning from data and making predictions.
We split the data into 3 parts: training, validation, and testing set.
### **1. Linear Regression**
This is the simplest model. It looks for straight-line relationships between the features and the price. It’s fast and easy to understand, but in this case, it didn’t work well.
- R2: -248664552725744.84. Performed worse than just guessing the average price.
- RMSE: Extremely high. Predictions were far from actual values.
- MAPE: Infinite. Caused by division errors or very small actual prices.
Conclusion: The model failed to capture the pricing patterns and gave very poor results.
### **2. Decision Tree Regressor**
This model splits the data into smaller groups by asking a series of “yes” or “no” questions based on different features. It can find non-linear relationships and is easy to visualize.
- R2: 0.665. Explained about 67% of the variation in prices.
- RMSE: 0.418. Predictions were off by about 42% on average.
- MAPE: 30.8%. Predictions were around 30% off from real prices.
Conclusion: A decent starting point. The model learned the data fairly well but was not very precise and tended to overfit.
### **3. Random Forest Regressor**
This model combines many decision trees to make better predictions. Each tree gives a small vote, and the average result becomes the final prediction. This helps improve accuracy and reduce overfitting.
- R2: 0.705. Explained about 71% of the variation.
- RMSE: 0.392. Errors were smaller, showing closer predictions.
- MAPE: 28.4%. Average error dropped, improving accuracy.
Conclusion: A strong and reliable model that handled complex data patterns well and gave consistent results.
### **4. XGBoost Regressor**
This is an advanced and powerful model that builds trees one after another, each time learning from the previous mistakes. It’s fast, efficient, and often produces very accurate results.
- R2: 0.758. Explained about 76% of the variation.
- RMSE: 0.356. Lowest error, with predictions very close to actual prices.
- MAPE: 25.9%. Predictions were about 26% off on average.
Conclusion: The best-performing model. XGBoost handled complex relationships extremely well and gave the most accurate and reliable results.
### **5. Gradient Boosting Regressor**
This model works similarly to XGBoost, building trees step by step, where each new tree fixes the errors of the previous ones.
- R2: 0.729. Explained about 73% of the variation.
- RMSE: 0.376. Moderate error, fairly close predictions.
- MAPE: 27.4%. Predictions were around 27% off on average.
Conclusion: A strong model with good performance. It was slightly less accurate than XGBoost, but with some fine-tuning, it could reach similar results.

Both the XGBoost Regressor and Gradient Boosting Regressor were tuned to improve their performance. After tuning, XGBoost achieved the best results, showing higher accuracy and lower error compared to the other models. We also experimented with a simple neural network, but the results were poor. The model struggled to learn meaningful patterns from the data and performed much worse than the tree-based models. In the end, XGBoost was chosen as the final model for predicting Airbnb prices in Cape Town due to its strong accuracy, consistency, and ability to handle complex data relationships effectively.

## Evaluation
The testing set was used here.
The tuned XGBoost Regressor, identified as the best-performing model, was evaluated on the training, validation, and test sets. The model showed strong performance and good generalization ability across all datasets.

**Performance Summary:**<br>
- Training Set: RMSE (actual) = 1006.31, R2 = 0.93, MAPE = 11.52%
- Validation Set: RMSE (actual) = 2039.22, R2 = 0.70, MAPE = 23.73%
- Test Set: RMSE (actual) = 1941.24, R2 = 0.73, MAPE = 23.12%

These results indicate that the model performs very well on the training data and maintains solid predictive accuracy on unseen data. The R2 score of 0.73 on the test set shows that about 73% of the variation in Airbnb prices can be explained by the model’s features. While the validation and test errors are higher than the training error, the difference is reasonable, suggesting the model generalizes well and avoids overfitting. The MAPE of around 23% means that, on average, the model’s predictions are within 23% of the actual Airbnb prices.
<p align = 'center'>Evaluation on the Testing set</p>

![Analysis 1](https://github.com/patsi-dev/Airbnb-Cape-Town-Price-Prediction/blob/ivy/images/Screenshot%20(144).png)

Overall, the tuned XGBoost model demonstrates reliable performance and provides meaningful insights into the factors influencing Airbnb pricing.

## Conclusion
In conclusion, the tuned XGBoost model performed well, explaining about 73% of price changes and keeping good accuracy across all datasets. With an average error of around 23%, it gives useful pricing suggestions and highlights important factors like location, property type, and amenities. Overall, it meets the project’s goal of providing smart, data-based insights to improve Airbnb pricing in Cape Town.
## Recommendations
- Retrain the model periodically as Airbnb listings and demand patterns change.
- Use feedback from host adoption to refine predictions, focusing on reducing the MAPE further below 20%.
- Include more features that capture dynamic pricing factors, e.g., local events, holidays, competitor prices, and seasonal trends
