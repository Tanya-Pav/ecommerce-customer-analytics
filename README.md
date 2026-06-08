# E-Commerce Customer Value & Behavior Analytics (RFM, LTV & Hypothesis Testing)

Language / Язык: [English](#english-version) | [Русский](#russian-version)

---

## English Version

### Project Overview
This project focuses on comprehensive Exploratory Data Analysis (EDA) and cohort analysis of transactional data from a major e-commerce retailer. It features an automated data preprocessing pipeline (ETL), customer base segmentation using the RFM (Recency, Frequency, Monetary) methodology, statistical hypothesis testing, and an interactive Streamlit-based dashboard for monitoring key business metrics.

### Repository Structure
* data/raw — initial transactional dataset (Online Retail Dataset from Kaggle).
* data/processed — cleaned and prepared data ready for analysis.
* src/pipeline.py — object-oriented automated data cleaning script (ETL).
* notebooks/1_rfm_segmentation.ipynb — Jupyter notebook containing RFM calculations and statistical testing.
* dashboard/app.py — interactive analytical dashboard powered by Streamlit.
* requirements.txt — project dependencies.

### Tech Stack
* Python (Pandas, NumPy, SciPy) — data processing and mathematical statistics.
* Matplotlib, Seaborn — analytical data visualization.
* Streamlit — web interface deployment.

### Features & Implementation Steps

#### 1. Data Preprocessing (ETL Pipeline)
During the initial analysis of the raw data (`src/pipeline.py`), critical anomalies were successfully resolved:
* Excluded over 135,000 records with missing customer identifiers (CustomerID) that could not be profiled.
* Identified and isolated return transactions (invoice codes starting with "C") into a separate feature.
* Removed 5,225 duplicate rows to prevent distortion of total revenue metrics.
* Automatically calculated the target metric for total transaction value (TotalPrice).

#### 2. Cohort RFM Analysis
Customers were scored from 1 to 5 based on distribution quantiles and divided into 5 core business segments:
* Champions — loyal customers with high purchase frequency and maximum spend.
* Loyal Customers — stable buyers with medium-to-high order values.
* New Customers — recent users with a low frequency score but recent activity.
* At Risk — historically high-value and frequent buyers who haven't made a purchase recently.
* Hibernating — dormant or lost users.

#### 3. Statistical Hypothesis Testing
To validate business insights, statistical testing was conducted using a two-sample Welch's T-test (SciPy).
* The hypothesis evaluated whether the average spend (Monetary) of `Loyal Customers` was equal to that of the `At Risk` group.
* The resulting p-value ($3.4475 \times 10^{-6}$) was significantly lower than the critical significance level ($\alpha = 0.05$), allowing us to confidently reject the null hypothesis. The difference in average order value is statistically significant and driven by behavioral factors rather than random data fluctuations.

#### 4. Interactive Dashboard
The control panel developed in `dashboard/app.py` enables users to:
* Filter metrics in real-time by specific customer cohorts.
* Dynamically track KPIs: total customer count in the selection, average order value, transaction frequency, and average recency.
* Analyze multidimensional relationships using interactive scatter plots (Monetary vs Frequency).

### Local Deployment Instructions

1. Clone the repository and navigate to the project's root folder.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
