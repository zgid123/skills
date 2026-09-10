# Time-Series Analysis

## Overview
Time-series analysis evaluates sequential data points indexed in temporal order. Unlike cross-sectional data where observations are assumed independent, time-series data exhibits temporal dependency, autocorrelation, and structural patterns. The analyst must isolate underlying trends from recurring seasonal patterns and random noise to evaluate performance accurately and produce reliable baseline forecasts.

## Components of a Time Series
A classical time series $Y_t$ is decomposed into four fundamental components:
- **Trend ($T_t$)**: The long-term directional trajectory of the metric over months or years (growth, decline, stagnation).
- **Seasonality ($S_t$)**: Periodic, predictable fluctuations occurring at fixed intervals (e.g., day-of-week dips on weekends, fourth-quarter retail surges).
- **Cyclical Variations ($C_t$)**: Macroeconomic or multi-year business fluctuations without fixed calendar periodicity.
- **Noise / Residual ($R_t$)**: Irregular, unpredictable random variation remaining after removing systematic components.

### Decomposition Models
- **Additive Decomposition**: $Y_t = T_t + S_t + C_t + R_t$ (or $Y_t = T_t + S_t + R_t$ where longer-term cyclical movements are absorbed into the trend component). Appropriate when seasonal fluctuations remain roughly constant in absolute magnitude regardless of the series level.
- **Multiplicative Decomposition**: $Y_t = T_t \times S_t \times C_t \times R_t$ (or $Y_t = T_t \times S_t \times R_t$). Appropriate when seasonal variations scale proportionally with the overall trend level (e.g., holiday sales surge by $30\%$ of current base volume).

## Temporal Metric Calculations

### 1. Growth Rates and Period-Over-Period Changes
- **Month-over-Month (MoM)**: Compares current month directly to the immediate preceding month:
  $$\text{MoM Growth} = \frac{Y_t - Y_{t-1}}{Y_{t-1}} \times 100\%$$
- **Year-over-Year (YoY)**: Compares current period to the exact same calendar period in the prior year, neutralizing annual seasonality:
  $$\text{YoY Growth} = \frac{Y_t - Y_{t-12}}{Y_{t-12}} \times 100\%$$
- **Quarter-over-Quarter (QoQ)**: Compares quarterly performance:
  $$\text{QoQ Growth} = \frac{Y_t - Y_{t-1}}{Y_{t-1}} \times 100\%$$

### 2. Rolling Metrics and Moving Averages
- **Simple Moving Average (SMA)**: Unweighted mean of the last $k$ periods. Smooths high-frequency noise and calendar fluctuations (e.g., a 7-day rolling window is a common heuristic for daily consumer traffic with day-of-week seasonality, but the smoothing window should always align with the data frequency and known periodicity).
- **Exponential Moving Average (EMA)**: Applies exponentially decreasing weights to older observations, responding faster to recent structural trend breaks.
- **Trailing vs. Centered Windows**:
  - *Trailing Window* ($t-k$ to $t$): Used for real-time operational monitoring and forecasting (avoids lookahead leakage).
  - *Centered Window* ($t - k/2$ to $t + k/2$): Used for retrospective trend decomposition and historical smoothing.

### 3. Lags, Leads, and Autocorrelation
- **Lag Operator ($Y_{t-k}$)**: The value of the series $k$ time steps prior.
- **Autocorrelation Function (ACF)**: Quantifies the linear correlation between a series and its own historical lags.
- **Frequency-Dependent Lag Interpretation**: Lags must always be interpreted relative to data cadence:
  - *Daily Data*: Lag 7 represents one week; lag 1 represents prior day.
  - *Monthly Data*: Lag 12 represents one year; lag 1 represents prior month.
  - *Hourly Data*: Lag 24 represents one full day.

## Stationarity and Transformation
- **Stationarity**: A stationary series exhibits constant mean, constant variance, and autocovariance independent of time. Most statistical forecasting models assume stationarity.
- **Differencing ($Y_t - Y_{t-1}$)**: Removes linear trends to stabilize the series mean. Seasonal differencing ($Y_t - Y_{t-s}$) removes periodic seasonal patterns.
- **Log Transformation**: Stabilizes exponential growth and heteroscedastic variance (increasing spread over time).

## Analyst-Level Baseline Forecasting Methods

Always establish simple, defensible baseline models before considering complex statistical techniques:

| Method | Formulation | When to Use |
|---|---|---|
| **Naive Baseline** | $\hat{Y}_{t+h} = Y_t$ | Fast random-walk benchmark; projects latest observed value forward. |
| **Seasonal Naive** | $\hat{Y}_{t+h} = Y_{t+h-m}$ | Projects the value from the exact same season last cycle (e.g., this Monday equals last Monday). Strong baseline for highly seasonal data. |
| **Moving Average Forecast** | $\hat{Y}_{t+h} = \frac{1}{k}\sum_{i=0}^{k-1} Y_{t-i}$ | Appropriate for stable series with zero trend and zero seasonality. |
| **Holt-Winters Exponential Smoothing** | Level + Trend + Seasonal smoothing equations | Captures both trending trajectories and multiplicative/additive seasonal patterns with low computational overhead. |
| **ARIMA / SARIMA** | Autoregressive Integrated Moving Average | Rigorous statistical modeling incorporating autoregression, differencing, and moving average residuals across non-seasonal and seasonal lags. |

## Temporal Validation and Lookahead Bias

### The Lookahead Leakage Trap
- **Never Use Random Train/Test Splits for Time Series**: Shuffling time-series observations randomly leaks future information into past training instances, producing unrealistically inflated model accuracy that collapses in production.
- **Rolling / Expanding Window Validation**: Always train on past historical periods and evaluate strictly on chronologically subsequent holdout periods:
  ```text
  Fold 1: [ Train: Month 1-6 ] → [ Test: Month 7 ]
  Fold 2: [ Train: Month 1-7 ] → [ Test: Month 8 ]
  Fold 3: [ Train: Month 1-8 ] → [ Test: Month 9 ]
  ```

### Prediction Intervals and Uncertainty
- Forecast uncertainty generally tends to increase as the forecast horizon $h$ extends into the future because more future shocks accumulate, though the exact pattern depends on the underlying process and model.
- Always communicate prediction intervals (e.g., $80\%$ and $95\%$ bounds) to reflect uncertainty transparently and prevent stakeholders from planning against an illusory single point estimate.

## Common Time-Series Analytical Pitfalls
- **The Incomplete Window Trap**: Comparing an ongoing partial month (e.g., 14 days of data) to a completed prior month without daily run-rate normalization.
- **Calendar Alignment Artifacts**: Comparing February (28 days) directly to January (31 days), or ignoring the shift in the number of weekend shopping days between calendar months.
- **Spurious Correlation in Non-Stationary Series**: Two independent series that both happen to trend upward over time (e.g., cloud hosting costs and global temperature) show near-perfect correlation ($r > 0.95$) despite having zero causal connection.

## Cross-References
- For SQL period-over-period and window function implementations: [SQL for Analysis](./sql-for-analysis.md)
- For exploratory distribution and trend profiling: [Exploratory Data Analysis (EDA)](./eda.md)
- For general predictive modeling and regression evaluation: [Predictive Analysis](./predictive-analysis.md)
- For visualizing time-series trends and intervals: [Visualization and Storytelling](./visualization-and-storytelling.md)
