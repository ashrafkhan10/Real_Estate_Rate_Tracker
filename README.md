# Real Estate Rate Tracker

## Project Overview
The Real Estate Rate Tracker project aims to predict property prices in Mumbai using machine learning algorithms. The project involves web scraping, data cleaning, exploratory data analysis (EDA), feature engineering, model building, and deployment using a Streamlit web application.

## Objective and Scope
- **Objective**: Develop a model that accurately predicts property prices based on various features.
- **Scope**: Includes data collection, preprocessing, analysis, model training, evaluation, and deployment.

## Dataset Description
The dataset, sourced from www.99acres.com, contains the following attributes:
- **Property_Name**: Title or name of the property listing.
- **Location**: Specific location within Mumbai.
- **Region**: Locality within Mumbai.
- **Property_Age**: Age of the property in years.
- **Availability**: Status of the property (e.g., ready to move, under construction).
- **Area_Type**: Type of area (e.g., built-up area, carpet area).
- **Area_SqFt**: Size of the property in square feet.
- **Rate_SqFt**: Price per square foot of the property.
- **Floor_No**: Floor number of the property.
- **Bedroom**: Number of bedrooms.
- **Bathroom**: Number of bathrooms.
- **Price_Lakh**: Price of the property in lakhs (Indian Rupees).

## Methodology

### Web Scraping
- **Tools Used**: `requests`, `BeautifulSoup`
- **Techniques Applied**: Iteratively scraped property details from multiple pages of the website.

### Data Cleaning
- **Handling Missing Values**: Imputed missing values using appropriate strategies.
- **Handling Duplicates**: Removed duplicate entries.
- **Handling Outliers**: Detected and addressed outliers using statistical methods.
- **Removing Unwanted Symbols and Text**: Cleaned specific text patterns and symbols.
- **Data Export**: Exported the cleaned data to `Mumbai_Property.csv`.

### Exploratory Data Analysis (EDA)
- **Summary Statistics**: Calculated descriptive statistics.
- **Visualizations**: Created histograms, box plots, scatter plots, etc., to gain insights.

### Feature Engineering
- **Polynomial Features**: Generated polynomial features to capture non-linear relationships.

### Model Building
- **Algorithms Used**:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
  - Polynomial Features with Linear Regression
- **Evaluation Metrics**: MAE, RMSE, R-squared
- **Model Comparison**: Polynomial Features with Linear Regression model achieved the highest accuracy.

### Deployment
- **Streamlit Web Application**:
  - Features: User input for property details, prediction of property price.
  - Deployment: Hosted on Streamlit.io.

## Final Model Evaluation
- **Function**: `evaluate` to assess model performance.
- **Results**:
  - Training Accuracy: 98.33%
  - Test Accuracy: 98.74%
  - Average Error: 8.7685 lakhs

## Results and Discussion
- **Key Findings**: Polynomial features significantly improved model performance.
- **Interpretation**: High accuracy indicates the model effectively captures property price determinants.
- **Limitations**: Model may overfit; further tuning and validation needed.
- **Future Enhancements**: Incorporate more features, use advanced algorithms, and improve web scraping efficiency.

## Conclusion
- **Recap**: Achieved a highly accurate model for predicting Mumbai property prices.
- **Lessons Learned**: Importance of feature engineering and thorough data cleaning.
- **Recommendations**: Future work should focus on expanding features and refining the model for better generalization.

## References
- www.99acres.com for dataset
- Scikit-learn documentation
- Streamlit documentation

## Appendices
- **Glossary**: Explanation of terms used in the project.
- **Supplementary Visualizations**: Additional plots and tables for detailed insights.

