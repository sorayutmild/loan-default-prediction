# loan-default-prediction
Loan default prediction with Berka Dataset using XGboost model.
<!-- ![banker cat](img/loan_cat.gif "banker cat") -->

<p align="center">
  <img src="https://github.com/sorayutmild/loan-default-prediction/blob/main/img/loan_cat.gif?raw=true" alt="banker cat"/>
</p>

## Goal
To provides mechanisms in determining which consumers should receive loans and to benefit banks in increasing profits.

## Dataset
We use [Berka dataset](https://relational.fit.cvut.cz/dataset/Financial) also known as PKDD'99 Financial dataset which contains 606 successful and 76 not successful loans along with their personal and transaction information.
The data relationship is depicted in the diagram below.
<!-- ![ER diagram of dataset](img/Data_description.png "ER diagram of dataset") -->
<p align="center">
  <img src="https://github.com/sorayutmild/loan-default-prediction/blob/main/img/Data_description.png?raw=true" alt="ER diagram of dataset"/>
</p>

## Challenges
* Imbalanced data (606 negative class, 76 possitive class)
* Feature engineering (Creation, Extraction, Transformation)

## Experiments
* We only used before loan information (because our Goal is to make decision to issue the loan)
* We tried several models, including LGBM, RandomForest, and XGboost (we used auto ML and discovered that these models are the best), and in the end, we used XGboost with feature selection (using feature important) and Grid-search to tune hyperparameters because it gives the best results.
* Profit is calculated using the formula profit = revenue - cost, where revenue is money earned by the bank from interest and cost is defaulted money. the more information is in `profit_analysis.ipynb`

## How to run
* First, preprocess the raw data run `data_manipulation.ipynb`. The results will be saved in `transformed_data/final_transformed_data.csv`
* second, train model using `model.ipynb`. The results will be in `report/report_xgb.csv` which contains true label and probability of prediction in each account
* then, we run `profit_analysis.ipynb` to create `report/ori_profit.csv` which is the original profit, and the final result `report/report_xgb_threshold_profit.csv` which is the profit after using this model in each threshold and each interest rate


## Results
### performance results 
* inital model performance 

| model | Acc | F1 | ROC_AUC |
 ---                   | --- |--- |--- |
LGBMClassifier         | 0.925 | 0.553 | 0.743 
RandomForestClassifier | 0.924 | 0.544 | 0.764  
XGBClassifier          | 0.923 | 0.596 | 0.738  

* Performance after using best params & best feature

| model                  | Acc   | F1    | ROC_AUC |
 ---                   | --- |--- |--- |
LGBMClassifier         | 0.919 | 0.572 | 0.731  
RandomForestClassifier | 0.912 | 0.616 | 0.791  
XGBClassifier          | 0.927 | 0.645 | 0.784  

### Power BI Visualization
we use Power BI to create a interactive dashboard to visualize the profit we've made
<!-- ![Dashboard](img/dashboard.gif "Dashboard") -->
<p align="center">
  <img src="https://github.com/sorayutmild/loan-default-prediction/blob/main/img/dashboard.gif?raw=true" alt="Dashboard"/>
</p>

# Links
[Power BI dashboard](https://app.powerbi.com/view?r=eyJrIjoiZjAzNzBiODItMjFiMC00N2RhLWJlNzQtOTRhNTUzZDliNDkzIiwidCI6IjZmNDQzMmRjLTIwZDItNDQxZC1iMWRiLWFjMzM4MGJhNjMzZCIsImMiOjEwfQ%3D%3D&pageName=ReportSectionf57bff23ee235c96e001) \
[Slide presentation](https://www.canva.com/design/DAFA2LPDvU0/Ic6zbqoEjrfDSmRpghyBgw/view?utm_content=DAFA2LPDvU0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)