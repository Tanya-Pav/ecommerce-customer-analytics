import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

# 1. Настройка страницы дашборда
st.set_page_config(
    page_title="E-Commerce Customer Analytics Dashboard",
    layout="wide",
)

# 2. Динамическое определение путей к данным
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
data_path = os.path.join(
    project_root, "data", "processed", "cleaned_ecommerce_data.csv"
)


# Оптимизируем загрузку данных с помощью кэширования Streamlit
@st.cache_data
def load_dashboard_data(path):
    data = pd.read_csv(path)
    data["InvoiceDate"] = pd.to_datetime(data["InvoiceDate"])
    return data


try:
    df = load_dashboard_data(data_path)
except Exception:
    st.error(
        f"Не удалось загрузить обработанные данные. Проверьте путь: {data_path}"
    )
    st.stop()

# 3. Заголовок дашборда
st.title("E-Commerce Customer Value & Behavior Dashboard")
st.markdown(
    "Интерактивная аналитическая панель для сегментации клиентов и мониторинга ключевых бизнес-метрик."
)
st.write("---")

# 4. Расчет RFM данных внутри дашборда для фильтрации
snapshot_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)
rfm = df.groupby("CustomerID").agg(
    {
        "InvoiceDate": lambda x: (snapshot_date - x.max()).days,
        "InvoiceNo": lambda x: x.nunique(),
        "TotalPrice": "sum",
    }
)
rfm.rename(
    columns={"InvoiceDate": "Recency", "InvoiceNo": "Frequency", "TotalPrice": "Monetary"},
    inplace=True,
)
rfm = rfm[rfm["Monetary"] > 0]

# Назначение баллов и сегментов
rfm["R_Score"] = pd.qcut(rfm["Recency"], q=5, labels=[5, 4, 3, 2, 1])
rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"), q=5, labels=[1, 2, 3, 4, 5]
)
rfm["M_Score"] = pd.qcut(rfm["Monetary"], q=5, labels=[1, 2, 3, 4, 5])


def get_segment_name(row):
    r = int(row['R_Score'])
    f = int(row['F_Score'])
    if r >= 4 and f >= 4:
        return 'Champions'
    elif r >= 3 and f >= 3:
        return 'Loyal Customers'
    elif r >= 4 and f < 3:
        return 'New Customers'
    elif r < 3 and f >= 3:
        return 'At Risk'
    else:
        return 'Hibernating'


rfm["Segment"] = rfm.apply(get_segment_name, axis=1)

# 5. Боковая панель (Sidebar)
st.sidebar.header("Фильтрация данных")
selected_segments = st.sidebar.multiselect(
    "Выберите сегменты клиентов:",
    options=list(rfm["Segment"].unique()),
    default=list(rfm["Segment"].unique()),
)

# Фильтруем данные по выбору пользователя
filtered_rfm = rfm[rfm["Segment"].isin(selected_segments)]

# 6. Ключевые метрики (KPI Blocks)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Всего клиентов в выборке", f"{len(filtered_rfm)} чел.")
with col2:
    st.metric("Средний чек сегментов", f"£ {filtered_rfm['Monetary'].mean():.2f}")
with col3:
    st.metric("Средняя частота покупок", f"{filtered_rfm['Frequency'].mean():.1f} зак.")
with col4:
    st.metric("Средняя давность (дней)", f"{filtered_rfm['Recency'].mean():.1f} дн.")

st.write("---")

# 7. Графики
left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Распределение клиентов по когортам")
    seg_counts = filtered_rfm["Segment"].value_counts().reset_index()

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(
        x="count",
        y="Segment",
        data=seg_counts,
        palette="viridis",
        ax=ax,
        hue="Segment",
        legend=False,
    )
    ax.set_xlabel("Количество клиентов")
    ax.set_ylabel("")
    st.pyplot(fig)

with right_col:
    st.subheader("Взаимосвязь частоты покупок и суммы (Monetary vs Frequency)")
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.scatterplot(
        x="Frequency",
        y="Monetary",
        hue="Segment",
        data=filtered_rfm,
        palette="viridis",
        alpha=0.6,
        ax=ax,
    )
    ax.set_yscale("log")
    ax.set_xlabel("Частота (кол-во заказов)")
    ax.set_ylabel("Сумма покупок (£, лог. шкала)")
    st.pyplot(fig)


st.write("---")
st.subheader("Детальные данные отфильтрованных клиентов")

st.dataframe(
    filtered_rfm[["Recency", "Frequency", "Monetary", "Segment"]].round(2),
    width="stretch",
)