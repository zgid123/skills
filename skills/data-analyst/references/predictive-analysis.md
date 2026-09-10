# Predictive Analysis

## Overview
Predictive analysis uses historical data to estimate the likelihood of future outcomes or quantify unobserved continuous quantities. Within the Data Analyst scope, predictive analysis focuses on defining clear prediction problems, establishing transparent baseline models, detecting data leakage, evaluating performance using business-aligned metrics, and interpreting model drivers. Deep learning, complex neural architectures, extensive hyperparameter optimization, and production MLOps deployment are explicitly out of scope.

## The Prediction Problem Formulation
Every predictive inquiry must be translated into a structured formulation:
- **Target Variable ($Y$)**: What specific business quantity or event are we predicting? (e.g., continuous revenue next quarter, or binary customer churn within 30 days).
- **Features ($X$)**: Measurable attributes, historical behaviors, and contextual signals available at the time prediction is made.
- **Unit of Observation**: What entity does a single row represent? (e.g., one customer account at the end of month $m$).
- **Prediction Horizon / Cutoff Date**: Predictions must use features available strictly prior to the observation cutoff timestamp.

## Data Splitting and Validation Strategy

### Train, Validation, and Test Partitions
- **Split Strategy is Context-Dependent**: Fixed split proportions (e.g., $70/15/15$ or $60/20/20$) are illustrative starting examples, not universal rules. The appropriate validation partitioning depends on:
  - Total dataset volume (massive datasets can use smaller percentage holdouts, e.g., $95/2.5/2.5$);
  - Temporal ordering (time-dependent data requires chronological rolling splits rather than random partitions);
  - Event rarity / class imbalance (stratified splits may be required);
  - Resampling strategy (cross-validation vs. single train/validation split);
  - Availability of external holdout datasets.
- **Partition Roles**:
  - *Training Set*: Used to estimate model parameters (coefficients, decision boundaries).
  - *Validation Set*: Used to evaluate competing model specifications, tune decision thresholds, and compare features.
  - *Test / Holdout Set*: Kept sealed until final model selection to provide an unbiased estimate of generalization error.

### Data Leakage (The Cardinal Sin of Predictive Analysis)
Data leakage occurs when information from outside the training dataset or from the future is inadvertently introduced into the model training pipeline:
- **Target Leakage**: Features that include artifacts or consequences of the target variable (e.g., using `refund_processed_timestamp` to predict whether an order will be returned).
- **Temporal Leakage**: Using future observations to predict past outcomes (e.g., standardizing data using the global mean of the entire dataset rather than computing mean strictly on historical training folds).
- **Train/Test Contamination**: Performing data imputation, scaling, or feature selection on the combined dataset prior to splitting.

### Overfitting vs. Underfitting
- **Underfitting**: Model is too simple to capture real underlying relationships (high bias; poor performance on both train and validation sets).
- **Overfitting**: Model memorizes noise and idiosyncratic quirks of the training sample (high variance; excellent training performance but poor generalization on validation/test holdouts).

## Regression Analysis (Predicting Continuous Outcomes)

### Baseline Model
Always compare against the simplest heuristic benchmark: predicting the training set mean or median ($\hat{Y} = \bar{Y}_{\text{train}}$). Any predictive model must beat the baseline to justify adoption.

### Representative Method: Ordinary Least Squares (OLS) Linear Regression
$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_p X_p + \epsilon$$
- **Interpretability**: Each coefficient $\beta_j$ represents the estimated change in outcome $Y$ associated with a one-unit increase in predictor $X_j$, holding all other predictors constant.
- **Coefficients vs. Feature Importance Nuance**: Do not automatically equate standardized regression coefficient magnitudes with "feature importance." Coefficient size and stability depend heavily on collinearity among predictors, model specification, feature scaling, interaction terms, categorical dummy coding, and regularization. A coefficient reflects partial association conditional on the other included variables, not an objective, global ranking of business importance.

### Regression Evaluation Metrics
- **Mean Absolute Error (MAE)**: Average magnitude of errors in original physical units:
  $$\text{MAE} = \frac{1}{n} \sum |Y_i - \hat{Y}_i|$$
- **Root Mean Squared Error (RMSE)**: Penalizes large outlier errors more heavily than MAE:
  $$\text{RMSE} = \sqrt{\frac{1}{n} \sum (Y_i - \hat{Y}_i)^2}$$
- **Coefficient of Determination ($R^2$)**: Proportion of variance in the target variable explained by the model relative to the simple mean baseline:
  $$R^2 = 1 - \frac{\sum (Y_i - \hat{Y}_i)^2}{\sum (Y_i - \bar{Y})^2}$$

## Classification Analysis (Predicting Discrete Categories)

### Baseline Model
Always compare against the majority class baseline (e.g., in a churn dataset where $92\%$ stay and $8\%$ churn, a naive model predicting "stays" for all accounts achieves $92\%$ accuracy while being operationally useless).

### Representative Method: Logistic Regression
Models the log-odds of a binary outcome:
$$\ln\left(\frac{p}{1-p}\right) = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p$$
- **Estimated Probabilities and Calibration**: Logistic regression produces estimated probabilities between $0.0$ and $1.0$, but **calibration is not guaranteed**. If predicted probabilities directly drive business decisions (e.g., pricing risk or expected value thresholds), evaluate calibration using calibration plots / reliability curves or the Brier score, and apply recalibration (such as isotonic regression or Platt scaling) when necessary.
- **Threshold Setting**: The analyst should adjust the decision threshold (default $0.5$) based on the asymmetric commercial costs of false positives vs. false negatives.

### The Confusion Matrix

| | Predicted Negative ($\hat{Y}=0$) | Predicted Positive ($\hat{Y}=1$) |
|---|---|---|
| **Actual Negative ($Y=0$)** | True Negative (TN) | False Positive (FP) |
| **Actual Positive ($Y=1$)** | False Negative (FN) | True Positive (TP) |

> **Conceptual Distinction**: False positives and false negatives are classification prediction errors. Type I and Type II errors are formal hypothesis-testing decision errors under a null hypothesis framework. While conceptually analogous in some contexts, avoid treating them as interchangeable terms.

### Classification Evaluation Metrics
- **Accuracy**: $\frac{\text{TP} + \text{TN}}{\text{Total}}$. Misleading on imbalanced datasets.
- **Precision**: $\frac{\text{TP}}{\text{TP} + \text{FP}}$. "When the model predicts positive, how often is it correct?" (Critical when false alarms carry high operational costs).
- **Recall (Sensitivity)**: $\frac{\text{TP}}{\text{TP} + \text{FN}}$. "Of all actual positive instances, what proportion did the model catch?" (Critical in churn detection or fraud flagging).
- **F1-Score**: Harmonic mean of Precision and Recall:
  $$\text{F1} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$
- **ROC-AUC (Receiver Operating Characteristic - Area Under Curve)**: Evaluates model ranking ability across all possible classification thresholds independent of class balance. A score of $0.5$ represents random guessing; $1.0$ represents perfect separation.

## Communicating Predictive Findings to Business Stakeholders
- Translate abstract statistical errors into commercial impacts (e.g., "At our chosen precision threshold, the model catches 70% of churners while requiring retention outreach to only 5% of our active customer base").
- Present predictions as calibrated risk bands or deciles rather than rigid binary assertions.
- Clearly state model limitations, training timeframe boundaries, and historical assumptions.

## Cross-References
- For temporal validation, lookahead bias prevention, and time-series forecasting: [Time-Series Analysis](./time-series-analysis.md)
- For distinguishing predictive correlation from causal interventions: [Causal Reasoning](./causal-reasoning.md)
- For feature cleaning, normalization, and dummy variable encoding: [Data Wrangling and Transformation](./data-wrangling.md)
- For evaluating baseline metrics, precision, and business costs: [Metrics and KPIs](./metrics-and-kpis.md)
