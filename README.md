# E-Commerce Customer Value & Behavior Analytics (RFM, LTV & Hypothesis Testing)

## Project Overview
This project focuses on comprehensive Exploratory Data Analysis (EDA) and cohort analysis of transactional data from a major e-commerce retailer. It includes an automated ETL pipeline, customer segmentation using the RFM (Recency, Frequency, Monetary) method, statistical hypothesis testing, and an interactive Streamlit dashboard for business analytics.

---

## Repository Structure
- `data/raw` — raw transactional dataset (Kaggle Online Retail Dataset)
- `data/processed` — cleaned dataset ready for analysis
- `src/pipeline.py` — ETL data preprocessing script
- `notebooks/1_rfm_segmentation.ipynb` — RFM analysis and statistical testing
- `dashboard/app.py` — Streamlit interactive dashboard
- `requirements.txt` — project dependencies

---

## Tech Stack
- **Python** (`Pandas`, `NumPy`, `SciPy`) — data processing and statistics
- **Matplotlib**, **Seaborn** — data visualization
- **Streamlit** — interactive dashboard

---

## Features & Workflow

### 1. Data Preprocessing (ETL Pipeline)
- Removed 135,000+ records with missing `CustomerID`
- Identified return transactions (`InvoiceNo` starting with "C")
- Removed 5,225 duplicate rows
- Created `TotalPrice` feature for revenue analysis

---

### 2. RFM Customer Segmentation
Customers were grouped into:
- **Champions** — most valuable and active customers
- **Loyal Customers** — consistent and high-value buyers
- **New Customers** — recently acquired customers
- **At Risk** — declining activity users
- **Hibernating** — inactive customers

---

### 3. Statistical Hypothesis Testing
- **Method:** Welch’s t-test (`SciPy`)
- **Comparison:** `Loyal Customers` vs `At Risk`
- **Result:** p-value = $3.4475 \times 10^{-6}$
- **Conclusion:** statistically significant difference in spending behavior

---

### 4. Interactive Dashboard
- Real-time segment filtering
- KPI metrics (total customers, frequency, recency, monetary value)
- Visual analysis (Monetary vs Frequency relationships)

---

## Local Setup

To run the project locally, execute the following commands in your terminal:

```bash
pip install -r requirements.txt
python src/pipeline.py
streamlit run dashboard/app.py
```

### (Russian Version)


# E-Commerce Customer Value & Behavior Analytics (RFM, LTV & Hypothesis Testing)

## Описание проекта
Проект посвящён анализу данных e-commerce, включая комплексный EDA, автоматический пайплайн предобработки сырых транзакций, RFM-сегментацию клиентов, проверку статистических гипотез и развёртывание интерактивного дашборда на Streamlit для мониторинга бизнес-метрик.

---

## Структура проекта
- `data/raw` — исходные транзакционные данные Kaggle
- `data/processed` — очищенные и готовые к анализу данные
- `src/pipeline.py` — скрипт автоматической очистки данных (ETL)
- `notebooks/1_rfm_segmentation.ipynb` — расчет RFM-метрик и статистика
- `dashboard/app.py` — аналитический дашборд
- `requirements.txt` — зависимости проекта

---

## Технологии
- **Python** (`Pandas`, `NumPy`, `SciPy`) — предобработка данных и математическая статистика
- **Matplotlib**, **Seaborn** — визуализация данных и графиков
- **Streamlit** — интерактивный веб-интерфейс

---

## Этапы работы

### 1. Предобработка данных (ETL-пайплайн)
- Удалено более 135 000 записей без идентификатора клиента (`CustomerID`)
- Корректно обработаны и вынесены в отдельный признак возвраты
- Удалено 5 225 полных дубликатов строк для предотвращения искажения выручки
- Создан целевой признак стоимости транзакции `TotalPrice`

---

### 2. RFM-сегментация
Клиенты были оценены на основе квантилей распределения и разделены на группы:
- **Champions** — лучшие клиенты с высокой частотой покупок и максимальным чеком
- **Loyal Customers** — стабильные покупатели со средним и высоким чеком
- **New Customers** — новые пользователи с недавней датой активности
- **At Risk** — клиенты, совершавшие крупные покупки, но теряющие активность
- **Hibernating** — спящие или неактивные пользователи

---

### 3. Проверка гипотез
- **Тест:** двухвыборочный Т-критерий Уэлча (`SciPy`)
- **Группы:** `Loyal Customers` vs `At Risk`
- **p-value:** $3.4475 \times 10^{-6}$ (значительно ниже $\alpha = 0.05$)
- **Вывод:** различие в средних чеках статистически значимо и обусловлено поведенческими факторами

---

### 4. Дашборд
- Фильтрация метрик по когортам в режиме реального времени
- Динамические KPI метрики (кол-во клиентов, частота, давность визита, средний чек)
- Графики и многомерная визуализация зависимостей (Monetary vs Frequency)

---

## Запуск проекта

Для локального запуска выполните следующие команды в вашем терминале:

```bash
pip install -r requirements.txt
python src/pipeline.py
streamlit run dashboard/app.py
```
pip install -r requirements.txt
python src/pipeline.py
streamlit run dashboard/app.py
