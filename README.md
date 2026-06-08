# E-Commerce Customer Value & Behavior Analytics (RFM, LTV & Hypothesis Testing)

Language / Язык: [English](#english-version) | [Русский](#russian-version)

---

## English Version

### Project Overview
This project focuses on comprehensive Exploratory Data Analysis (EDA) and cohort analysis of transactional data from a major e-commerce retailer. It features an automated data preprocessing pipeline (ETL), customer base segmentation using the RFM (Recency, Frequency, Monetary) methodology, statistical hypothesis testing, and an interactive Streamlit-based dashboard for monitoring key business metrics.

### Repository Structure
* `data/raw` — initial transactional dataset (Online Retail Dataset from Kaggle).
* `data/processed` — cleaned and prepared data ready for analysis.
* `src/pipeline.py` — object-oriented automated data cleaning script (ETL).
* `notebooks/1_rfm_segmentation.ipynb` — Jupyter notebook containing RFM calculations and statistical testing.
* `dashboard/app.py` — interactive analytical dashboard powered by Streamlit.
* `requirements.txt` — project dependencies.

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
* **Champions** — loyal customers with high purchase frequency and maximum spend.
* **Loyal Customers** — stable buyers with medium-to-high order values.
* **New Customers** — recent users with a low frequency score but recent activity.
* **At Risk** — historically high-value and frequent buyers who haven't made a purchase recently.
* **Hibernating** — dormant or lost users.

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
```
   pip install -r requirements.txt

```

3. Run the data processing pipeline:

```
   python src/pipeline.py

```

4. Launch the interactive dashboard:

```
   streamlit run dashboard/app.py

```

---

## Russian Version

## Описание проекта
Данный проект посвящен комплексному разведочному и когортному анализу коммерческих данных (EDА) крупного e-commerce ритейлера. В рамках работы реализован автоматизированный пайплайн предобработки сырых транзакций, проведена сегментация клиентской базы по методологии RFM (Recency, Frequency, Monetary), осуществлена проверка статистических гипотез и разработан интерактивный дашборд для мониторинга бизнес-метрик на базе Streamlit.

## Структура репозитория
* `data/raw` — исходный транзакционный датасет (Online Retail Dataset с Kaggle).
* `data/processed` — очищенные и подготовленные к анализу данные.
* `src/pipeline.py` — объектно-ориентированный скрипт автоматической очистки данных (ETL).
* `notebooks/1_rfm_segmentation.ipynb` — Jupyter-ноутбук с расчетом RFM-метрик и статистическим тестированием.
* `dashboard/app.py` — интерактивная аналитическая панель на Streamlit.
* `requirements.txt` — список зависимостей проекта.

## Технологический стек
* Python (Pandas, NumPy, SciPy) — обработка данных и математическая статистика.
* Matplotlib, Seaborn — построение аналитических графиков.
* Streamlit — развертывание веб-интерфейса.

## Реализованный функционал и этапы работы

### 1. Предобработка данных (ETL-пайплайн)
В ходе первичного анализа сырых данных (`src/pipeline.py`) были успешно устранены критические аномалии:
* Исключено более 135 000 записей с отсутствующими идентификаторами клиентов (CustomerID), не подлежащих профилированию.
* Идентифицированы и вынесены в отдельный признак транзакции возврата (коды счетов, начинающиеся с "C").
* Удалено 5 225 полных дубликатов строк, способных исказить показатели выручки.
* Автоматически рассчитана целевая метрика общей стоимости транзакции (TotalPrice).

### 2. Когортный RFM-анализ
Все клиенты были оценены по шкале от 1 до 5 на основе квантилей распределения и разделены на 5 ключевых бизнес-сегментов:
* **Champions** — постоянные клиенты с высокой частотой покупок и максимальным чеком.
* **Loyal Customers** — стабильно покупающие клиенты со средним и высоким чеком.
* **New Customers** — новые пользователи с недавней датой первой покупки.
* **At Risk** — клиенты, совершавшие крупные и частые покупки в прошлом, но прекратившие активность.
* **Hibernating** — спящие или безвозвратно ушедшие пользователи.

### 3. Проверка статистических гипотез
Для валидации бизнес-выводов было проведено статистическое тестирование с использованием двухвыборочного Т-критерия Уэлча (SciPy).
* Проверялась гипотеза о равенстве средних затрат (Monetary) между группами `Loyal Customers` и `At Risk`.
* Полученное значение p-value ($3.4475 \times 10^{-6}$) значительно ниже критического уровня значимости ($\alpha = 0.05$), что позволило уверенно отвергнуть нулевую гипотезу. Разница в средних чеках статистически значима и обусловлена поведенческими факторами, а не случайными колебаниями данных.

### 4. Интерактивный Дашборд
Разработанная панель управления в `dashboard/app.py` позволяет:
* Фильтровать метрики в режиме реального времени по конкретным когортам.
* Динамически отслеживать KPI: общее количество клиентов в выборке, средний чек, частоту транзакций и среднюю давность визита.
* Анализировать многомерные зависимости на интерактивных диаграммах рассеяния (Monetary vs Frequency).

## Инструкция по локальному запуску

1. Склонируйте репозиторий и перейдите в корневую папку проекта.
2. Установите необходимые библиотеки:
```bash
   pip install -r requirements.txt
Запустите пайплайн обработки данных:

Bash
   python src/pipeline.py
Запустите интерактивный дашборд:

Bash
   streamlit run dashboard/app.py

```

```
