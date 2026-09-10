# Statistics and Statistical Inference

## Overview
Statistical inference allows an analyst to draw defensible conclusions about broader populations from finite, observed data. The analyst's goal is not merely to compute test statistics or seek arbitrary thresholds like $p < 0.05$, but to quantify uncertainty, evaluate effect magnitudes, and assess practical business significance.

## The Core Inferential Reasoning Chain
Whenever an observed difference or shift appears in data, reason through this five-step sequence:
```text
Observed Difference
     ↓
How uncertain is it? (Standard error, confidence interval)
     ↓
Could random noise reasonably explain it? (p-value, hypothesis test)
     ↓
How large is the effect? (Effect size: Cohen's d, relative lift)
     ↓
Does the effect matter to the business? (Practical & economic significance)
```

## Foundations: Samples, Populations, and Distributions

### Population vs. Sample
- **Population**: The complete set of entities under consideration (e.g., all current and future visitors to an e-commerce website).
- **Sample**: An observed subset drawn from the population.
- **Parameter vs. Statistic**: A parameter (e.g., population mean $\mu$) is fixed but unobservable; a statistic (e.g., sample mean $\bar{x}$) is calculated from sample data to estimate the parameter.
- **Representativeness**: Representativeness depends on the sampling design (randomized, unbiased selection), NOT merely sample size. A massive biased sample (e.g., voluntary opt-in) remains unrepresentative.

### Central Tendency and Dispersion
- **Mean vs. Median**: Use the median rather than the mean when data is substantially skewed or contains valid extreme values and the goal is to represent the typical observation.
- **Variance and Standard Deviation**: Standard deviation ($\sigma$ or $s$) describes the scale of variation around the mean and is the square root of the average squared deviation under the relevant variance definition (expressed in the variable's original physical units).
- **Quantiles and Interquartile Range (IQR)**: The difference between the 75th percentile ($Q_3$) and 25th percentile ($Q_1$), providing a dispersion metric robust against extreme values.
- **Skewness**: Right-skewed (tail extends right, mean $>$ median); Left-skewed (tail extends left, mean $<$ median).

### Sampling Distributions, CLT, and Standard Error
- **Central Limit Theorem (CLT)**: The sampling distribution of the sample mean approaches a normal distribution as sample size increases, regardless of the underlying population shape (provided variance is finite).
- **Sample Size Nuance**: There is no universal, magical sample-size cutoff at $N = 30$. The sample size required for reliable estimation depends on population skewness, variance, effect size, and analytical objectives. Mildly skewed distributions need modest samples; heavy-tailed or sparse binary events require much larger samples. Small samples should be interpreted with appropriate uncertainty.
- **Standard Error (SE)**: Measures the variability of the sample statistic across repeated samples:
  $$\text{SE}_{\bar{x}} = \frac{s}{\sqrt{n}}$$

## Confidence Intervals vs. Hypothesis Testing

### Confidence Intervals (Estimation with Uncertainty)
- A 95% Confidence Interval (CI) indicates that across repeated independent samplings from the population, approximately 95% of computed intervals would contain the true parameter.
  $$\text{CI} = \text{estimate} \pm \text{critical value} \times \text{standard error}$$
- **Critical Value Nuance**: The critical value depends on the estimator, sampling distribution, sample size, and modeling assumptions. For example, for estimating a sample mean with unknown variance, a Student's $t$-distribution critical value ($t^*$) is standard; for proportions with large samples, standard normal critical values ($z^*$) are common.
- **Interpretation Rule**: Confidence intervals communicate both the magnitude of the effect and the precision of the estimate. Always prefer reporting confidence intervals alongside point estimates.

### Hypothesis Testing Framework
- **Null Hypothesis ($H_0$)**: Baseline proposition of no effect, no difference, or status quo.
- **Alternative Hypothesis ($H_1$)**: Proposition that an effect, difference, or relationship exists.
- **Significance Level ($\alpha$)**: Pre-specified threshold for rejecting $H_0$ (conventionally $0.05$).
- **p-value**: The probability of observing a test statistic as extreme as, or more extreme than, the observed value, assuming $H_0$ is true.
- **Critical Principle**: Under the null model and stated assumptions, a small $p$-value indicates that the observed data would be relatively unusual. A $p$-value is NOT the probability that $H_0$ is true, nor does $p < 0.05$ guarantee an intervention was commercially successful. Never treat $p < 0.05$ as an automatic green light.

### Decision Errors and Statistical Power
- **Type I Error ($\alpha$)**: Rejecting $H_0$ when it is actually true (a false positive decision in hypothesis testing; distinct from a classification prediction error).
- **Type II Error ($\beta$)**: Failing to reject $H_0$ when an actual effect exists (a false negative decision in hypothesis testing).
- **Statistical Power ($1 - \beta$)**: Probability of detecting a true effect of a specified magnitude (typically targeted at $80\%$ or $90\%$).

## Statistical Significance vs. Practical Significance
- **Statistical Significance**: Indicates that under the null hypothesis and model assumptions, the observed data would be unlikely by chance alone. Crucially, statistical significance does NOT establish: (1) causality, (2) practical or commercial importance, (3) data quality, or (4) model correctness.
- **Effect Size**: Quantifies the magnitude of the phenomenon:
  - Standardized difference (Cohen's $d = \frac{\bar{x}_1 - \bar{x}_2}{s_{\text{pooled}}}$).
  - Relative lift ($\frac{\text{Treatment} - \text{Control}}{\text{Control}} \times 100\%$).
- **Practical (Business) Significance**: Determines whether the observed magnitude is large enough to justify the financial, technical, or operational costs of taking action. With massive samples ($N = 10{,}000{,}000$), a $0.01\%$ lift in click rate may be statistically significant ($p < 0.001$) but economically meaningless.

## Common Hypothesis Tests for Analysts

| Analytical Scenario | Recommended Test | Key Assumptions | Non-Parametric / Small-Sample Alternatives |
|---|---|---|---|
| Compare sample mean to benchmark | One-Sample t-Test | Independent observations, approximate normality of sample mean. | Wilcoxon Signed-Rank Test |
| Compare means of 2 independent groups | Independent Two-Sample t-Test (Welch's t-test preferred) | Independent samples; Welch's test relaxes equal variance assumption. | Mann–Whitney U Test |
| Compare means before and after on same subjects | Paired t-Test | Paired observations, normally distributed differences. | Wilcoxon Signed-Rank Test |
| Compare means across 3+ independent groups | One-Way ANOVA | Independent groups, approximate normality, homogeneity of variance. | Kruskal–Wallis Test |
| Compare categorical frequencies / proportions | Chi-Square ($\chi^2$) Test of Independence | Independent observations. Rule of thumb heuristic: expected frequencies $\ge 5$ in most cells. | Fisher's Exact Test (small $2\times 2$ tables), Monte Carlo / exact tests, or category consolidation |
| Linear association between continuous variables | Pearson Correlation ($r$) | Linear relationship, continuous variables, bivariate normality. | Spearman Rank Correlation ($\rho$) |

## Multiple Comparisons and Family-Wise Error Rate
When testing multiple hypotheses or segmenting results across many sub-cohorts simultaneously, the probability of at least one false positive inflates rapidly:
$$\alpha_{\text{family}} = 1 - (1 - \alpha)^k$$
For 20 simultaneous tests at $\alpha = 0.05$, the chance of a false positive is $1 - (0.95)^{20} \approx 64\%$.
- **Correction Techniques**:
  - **Bonferroni Correction**: Adjusts significance threshold to $\alpha / k$ (conservative).
  - **Benjamini-Hochberg (FDR)**: Controls the False Discovery Rate, balancing discovery with error control.
  - **Pre-Registration**: Formulate primary hypotheses in advance rather than searching post-hoc across dozens of sub-cohorts.

## Resampling and Bootstrap Fundamentals
When data violates parametric distribution assumptions or when estimating complex statistics (e.g., medians, percentiles, ratios of sums):
- **Bootstrapping**: Repeatedly resample the observed dataset with replacement (typically 1,000 to 10,000 iterations), compute the statistic on each replicate, and derive empirical confidence intervals from the resulting distribution percentiles (e.g., 2.5th and 97.5th percentiles for a 95% CI).
- Highly effective for non-standard metrics where analytical standard error formulas do not exist.

## Cross-References
- For designing randomized experiments and power sizing: [Experimentation and A/B Testing](./experimentation.md)
- For evaluating causal assumptions vs. observational associations: [Causal Reasoning](./causal-reasoning.md)
- For exploratory distribution and correlation analysis: [Exploratory Data Analysis (EDA)](./eda.md)
- For defining business metrics and calculating ratios correctly: [Metrics and KPIs](./metrics-and-kpis.md)
