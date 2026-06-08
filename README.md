# E-Commerce Customer Value & Behavior Analytics (RFM, LTV & Hypothesis Testing)

Language / Язык: English | Русский

---

## English Version

### Project Overview
This project focuses on comprehensive Exploratory Data Analysis (EDA) and cohort analysis of transactional data from a major e-commerce retailer. It includes an automated ETL pipeline, customer segmentation using the RFM (Recency, Frequency, Monetary) method, statistical hypothesis testing, and an interactive Streamlit dashboard for business analytics.

---

### Repository Structure
- data/raw — raw transactional dataset (Kaggle Online Retail Dataset)
- data/processed — cleaned dataset ready for analysis
- src/pipeline.py — ETL data preprocessing script
- notebooks/1_rfm_segmentation.ipynb — RFM analysis and statistical testing
- dashboard/app.py — Streamlit interactive dashboard
- requirements.txt — project dependencies

---

### Tech Stack
- Python (Pandas, NumPy, SciPy) — data processing and statistics
- Matplotlib, Seaborn — data visualization
- Streamlit — interactive dashboard

---

### Features & Workflow

#### 1. Data Preprocessing (ETL Pipeline)
- Removed 135,000+ records with missing CustomerID
- Identified return transactions (InvoiceNo starting with "C")
- Removed 5,225 duplicate rows
- Created TotalPrice feature for revenue analysis

---

#### 2. RFM Customer Segmentation
Customers were grouped into:

- Champions — most valuable and active customers
- Loyal Customers — consistent and high-value buyers
- New Customers — recently acquired customers
- At Risk — declining activity users
- Hibernating — inactive customers

---

#### 3. Statistical Hypothesis Testing
- Method: Welch’s t-test (SciPy)
- Comparison: Loyal Customers vs At Risk
- Result: p-value = 3.4475e-06
- Conclusion: statistically significant difference in spending behavior

---

#### 4. Interactive Dashboard
- Real-time segment filtering
- KPI metrics (customers, frequency, recency, monetary value)
- Visual analysis (Monetary vs Frequency relationships)

---

### Local Setup

pip install -r requirements.txt

python src/pipeline.py

streamlit run dashboard/app.py

---

## Russian Version

### Описание проекта
Проект посвящён анализу данных e-commerce, включая EDA, RFM-сегментацию, статистические тесты и интерактивный дашборд на Streamlit.

---

### Структура проекта
- data/raw — исходные данные Kaggle
- data/processed — очищенные данные
- src/pipeline.py — ETL-пайплайн
- notebooks/1_rfm_segmentation.ipynb — анализ и статистика
- dashboard/app.py — дашборд
- requirements.txt — зависимости

---

### Технологии
- Python (Pandas, NumPy, SciPy)
- Matplotlib, Seaborn
- Streamlit

---

### Этапы работы

#### 1. Предобработка данных
- удалены записи без CustomerID
- обработаны возвраты
- удалены дубликаты
- создан TotalPrice

---

#### 2. RFM-сегментация
- Champions — лучшие клиенты
- Loyal Customers — стабильные клиенты
- New Customers — новые пользователи
- At Risk — теряющие активность
- Hibernating — неактивные

---

#### 3. Проверка гипотез
- тест: Welch t-test
- группы: Loyal vs At Risk
- p-value: 3.4475e-06
- вывод: различие значимо

---

#### 4. Дашборд
- фильтрация сегментов
- KPI метрики
- графики и визуализация

---

### Запуск проекта

pip install -r requirements.txt

python src/pipeline.py

streamlit run dashboard/app.py
