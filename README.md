# New-Wine-Quality-Prediction

Wine-Quality-Prediction
🔍 Overview This project predicts wine quality from physicochemical attributes and presents the results in a Power BI dashboard built on the scaled feature set (StandardScaler). It covers data cleaning, preprocessing, model selection, tuning, and interactive visualisation.

📌 Objective Classify wine samples into quality tiers (Low, Medium, High) so producers can automate routine quality checks.

📁 Dataset Source: UCI Wine Quality (red & white combined)

Features: 11 physicochemical inputs → scaled to μ = 0, σ = 1 before modelling and before exporting to Power BI.

Label: Quality score (0–10)

⚙️ Techniques & Algorithms Used Data Preprocessing:

1). Handling missing values

2). Label encoding

3). Scaling with StandardScaler

4). Outlier detection using IQR method

Exploratory Data Analysis (EDA):

1). Correlation heatmaps

2). Boxplots & pairplots

3). Histograms for feature distribution

Algorithms Tried:

1). Logistic Regression

2). Decision Tree Classifier

3). Random Forest Classifier

Evaluation Metrics:

1). Accuracy, Precision, Recall, F1-Score

2). Confusion Matrix

3). Mean Absolute Error (MAE), RMSE (for regression attempts)

🧪 Challenges Faced Imbalanced Quality Labels:

Most wines had quality ratings between 5 and 6, making it difficult for classifiers to detect minority classes.

Overfitting with Complex Models:

Some models like Random Forest or XGBoost were prone to overfitting on training data.

Metric Selection:

Initially used accuracy, but it wasn’t reliable due to class imbalance.

✅ Solutions Implemented Class Balancing:

Grouped wine qualities into categories: Low (3–4), Medium (5–6), High (7–8)

Cross-validation:

Used Stratified K-Fold to ensure balanced splits across classes

Hyperparameter Tuning:

Used GridSearchCV and RandomizedSearchCV for model optimization

Evaluation Shift:

Switched to F1-Score and Confusion Matrix for better insights

📊 Power BI Dashboard (from wine_scaled.csv) Card KPIs: Precision, Recall, F1 by class

Clustered bar: Alcohol (scaled) vs Predicted Quality

Stacked column: Actual vs Predicted counts

Density scatter: Volatile Acidity (scaled) vs Quality

Curved cards & custom dark canvas background for aesthetics

📦 Requirements Python 3

pandas, numpy, scikit-learn, matplotlib, seaborn

Jupyter Notebook / VS Code

Power BI (for dashboard)
