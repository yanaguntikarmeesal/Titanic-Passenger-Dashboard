import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ------------------------------------------------------------------
# Page configuration
# ------------------------------------------------------------------
st.set_page_config(
    page_title="Titanic Dashboard",
    page_icon="🚢",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------------------------------------------------
# Custom CSS for a polished look
# ------------------------------------------------------------------
st.markdown("""
<style>
    .main {
        background-color: #f4f7fc;
    }
    .metric-card {
        background: white;
        border-radius: 1rem;
        padding: 1.2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        border: 1px solid #e9eef4;
        text-align: center;
        transition: transform 0.2s;
    }
    .metric-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    }
    .metric-label {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-weight: 600;
        color: #64748b;
        margin-bottom: 0.3rem;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #0f172a;
    }
    .metric-sub {
        font-size: 0.8rem;
        color: #64748b;
    }
    h1, h2, h3 {
        color: #1e293b;
    }
    .block-container {
        padding-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------
# Load data
# ------------------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("titanic.csv")
    # Clean / derive fields
    df["Survived_Label"] = df["Survived"].map({0: "Died", 1: "Survived"})
    df["Pclass_Label"] = df["Pclass"].map({1: "1st Class", 2: "2nd Class", 3: "3rd Class"})
    df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
    df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")
    df["Embarked"] = df["Embarked"].fillna("Unknown")
    return df

df = load_data()

# ------------------------------------------------------------------
# Sidebar filters
# ------------------------------------------------------------------
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/f/fd/RMS_Titanic_3.jpg",
                 use_container_width=True)
st.sidebar.title("🔍 Filters")

# Survival filter
survival_filter = st.sidebar.multiselect(
    "Survival Status",
    options=["Survived", "Died"],
    default=["Survived", "Died"],
)

# Class filter
class_filter = st.sidebar.multiselect(
    "Passenger Class",
    options=["1st Class", "2nd Class", "3rd Class"],
    default=["1st Class", "2nd Class", "3rd Class"],
)

# Sex filter
sex_filter = st.sidebar.multiselect(
    "Sex",
    options=["male", "female"],
    default=["male", "female"],
)

# Age range slider
age_min = int(df["Age"].min()) if not df["Age"].isna().all() else 0
age_max = int(df["Age"].max()) if not df["Age"].isna().all() else 80
age_range = st.sidebar.slider(
    "Age Range",
    min_value=age_min,
    max_value=age_max,
    value=(age_min, age_max),
)

# Fare range slider
fare_min = float(df["Fare"].min())
fare_max = float(df["Fare"].max())
fare_range = st.sidebar.slider(
    "Fare Range",
    min_value=fare_min,
    max_value=fare_max,
    value=(fare_min, fare_max),
)

# Apply filters
filtered_df = df[
    (df["Survived_Label"].isin(survival_filter)) &
    (df["Pclass_Label"].isin(class_filter)) &
    (df["Sex"].isin(sex_filter)) &
    (df["Age"].fillna(-1).between(age_range[0], age_range[1])) &
    (df["Fare"].between(fare_range[0], fare_range[1]))
]

# ------------------------------------------------------------------
# Header
# ------------------------------------------------------------------
st.title("🚢 Titanic Passenger Dashboard")
st.markdown(
    f"**Exploratory overview** · Showing **{len(filtered_df):,}** of **{len(df):,}** passengers "
    f"based on current filters"
)
st.markdown("---")

# ------------------------------------------------------------------
# KPI Metrics
# ------------------------------------------------------------------
total = len(filtered_df)
survived = filtered_df["Survived"].sum()
died = total - survived
survival_rate = (survived / total * 100) if total > 0 else 0
avg_age = filtered_df["Age"].mean()
avg_fare = filtered_df["Fare"].mean()
female_count = (filtered_df["Sex"] == "female").sum()
male_count = (filtered_df["Sex"] == "male").sum()

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Total Passengers</div>
        <div class="metric-value">{total:,}</div>
        <div class="metric-sub">filtered</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Survivors</div>
        <div class="metric-value" style="color:#16a34a;">{survived:,}</div>
        <div class="metric-sub">{survival_rate:.1f}% survival rate</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Deaths</div>
        <div class="metric-value" style="color:#dc2626;">{died:,}</div>
        <div class="metric-sub">{100 - survival_rate:.1f}% mortality</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Average Age</div>
        <div class="metric-value">{avg_age:.1f}</div>
        <div class="metric-sub">years</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Average Fare</div>
        <div class="metric-value">£{avg_fare:.2f}</div>
        <div class="metric-sub">per passenger</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ------------------------------------------------------------------
# Row 1 — Survival by Sex, Class, and Age Distribution
# ------------------------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("👫 Survival by Sex")
    sex_survival = filtered_df.groupby(["Sex", "Survived_Label"]).size().reset_index(name="Count")
    fig_sex = px.bar(
        sex_survival,
        x="Sex",
        y="Count",
        color="Survived_Label",
        barmode="group",
        color_discrete_map={"Survived": "#22c55e", "Died": "#ef4444"},
        text="Count",
    )
    fig_sex.update_layout(
        height=320,
        margin=dict(l=10, r=10, t=10, b=10),
        legend_title="",
        xaxis_title="",
        yaxis_title="Passengers",
        plot_bgcolor="white",
    )
    fig_sex.update_traces(textposition="outside")
    st.plotly_chart(fig_sex, use_container_width=True)

with col2:
    st.subheader("🎟️ Survival by Class")
    class_survival = filtered_df.groupby(["Pclass_Label", "Survived_Label"]).size().reset_index(name="Count")
    fig_class = px.bar(
        class_survival,
        x="Pclass_Label",
        y="Count",
        color="Survived_Label",
        barmode="group",
        color_discrete_map={"Survived": "#22c55e", "Died": "#ef4444"},
        text="Count",
    )
    fig_class.update_layout(
        height=320,
        margin=dict(l=10, r=10, t=10, b=10),
        legend_title="",
        xaxis_title="",
        yaxis_title="Passengers",
        plot_bgcolor="white",
    )
    fig_class.update_traces(textposition="outside")
    st.plotly_chart(fig_class, use_container_width=True)

with col3:
    st.subheader("📊 Age Distribution")
    fig_age = px.histogram(
        filtered_df.dropna(subset=["Age"]),
        x="Age",
        nbins=25,
        color="Survived_Label",
        color_discrete_map={"Survived": "#22c55e", "Died": "#ef4444"},
        barmode="overlay",
        opacity=0.7,
    )
    fig_age.update_layout(
        height=320,
        margin=dict(l=10, r=10, t=10, b=10),
        legend_title="",
        xaxis_title="Age (years)",
        yaxis_title="Count",
        plot_bgcolor="white",
    )
    st.plotly_chart(fig_age, use_container_width=True)

# ------------------------------------------------------------------
# Row 2 — Fare Distribution & Embarkation Survival
# ------------------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("💰 Fare Distribution by Survival")
    fig_fare = px.box(
        filtered_df.dropna(subset=["Fare"]),
        x="Survived_Label",
        y="Fare",
        color="Survived_Label",
        color_discrete_map={"Survived": "#22c55e", "Died": "#ef4444"},
        points="outliers",
    )
    fig_fare.update_layout(
        height=350,
        margin=dict(l=10, r=10, t=10, b=10),
        legend_title="",
        xaxis_title="",
        yaxis_title="Fare (£)",
        plot_bgcolor="white",
        showlegend=False,
    )
    st.plotly_chart(fig_fare, use_container_width=True)

with col2:
    st.subheader("📍 Survival by Embarkation Port")
    embark_survival = filtered_df.groupby(["Embarked", "Survived_Label"]).size().reset_index(name="Count")
    fig_embark = px.bar(
        embark_survival,
        x="Embarked",
        y="Count",
        color="Survived_Label",
        barmode="group",
        color_discrete_map={"Survived": "#22c55e", "Died": "#ef4444"},
        text="Count",
    )
    fig_embark.update_layout(
        height=350,
        margin=dict(l=10, r=10, t=10, b=10),
        legend_title="",
        xaxis_title="Port (C = Cherbourg, Q = Queenstown, S = Southampton)",
        yaxis_title="Passengers",
        plot_bgcolor="white",
    )
    fig_embark.update_traces(textposition="outside")
    st.plotly_chart(fig_embark, use_container_width=True)

# ------------------------------------------------------------------
# Row 3 — Survival Heatmap + Rate Table
# ------------------------------------------------------------------
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🔥 Survival Rate Heatmap (Sex × Class)")
    pivot = filtered_df.pivot_table(
        index="Sex",
        columns="Pclass_Label",
        values="Survived",
        aggfunc="mean",
    )
    # Reorder columns
    ordered_cols = [c for c in ["1st Class", "2nd Class", "3rd Class"] if c in pivot.columns]
    pivot = pivot[ordered_cols]

    fig_heat = px.imshow(
        pivot,
        text_auto=".1%",
        color_continuous_scale="RdYlGn",
        zmin=0,
        zmax=1,
        aspect="auto",
    )
    fig_heat.update_layout(
        height=320,
        margin=dict(l=10, r=10, t=10, b=10),
        xaxis_title="",
        yaxis_title="",
        coloraxis_colorbar=dict(title="Survival Rate"),
    )
    st.plotly_chart(fig_heat, use_container_width=True)

with col2:
    st.subheader("📋 Survival Rate by Sex & Class")
    rate_table = filtered_df.groupby(["Sex", "Pclass_Label"]).agg(
        Survived=("Survived", "sum"),
        Total=("Survived", "count"),
    ).reset_index()
    rate_table["Rate"] = (rate_table["Survived"] / rate_table["Total"] * 100).round(1)
    rate_table["Rate"] = rate_table["Rate"].astype(str) + "%"
    rate_table.columns = ["Sex", "Class", "Survived", "Total", "Rate"]
    st.dataframe(
        rate_table,
        use_container_width=True,
        hide_index=True,
        height=320,
    )

# ------------------------------------------------------------------
# Row 4 — Sample Passengers Table
# ------------------------------------------------------------------
st.subheader("🧾 Sample Passengers")
sample = filtered_df[
    ["PassengerId", "Name", "Sex", "Age", "Pclass_Label", "Fare", "Embarked", "Survived_Label"]
].head(20).copy()
sample.columns = ["ID", "Name", "Sex", "Age", "Class", "Fare (£)", "Embarked", "Survival"]
sample["Fare (£)"] = sample["Fare (£)"].round(2)
st.dataframe(
    sample,
    use_container_width=True,
    hide_index=True,
    height=400,
)

# ------------------------------------------------------------------
# Footer
# ------------------------------------------------------------------
st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:#94a3b8; font-size:0.85rem;'>"
    "🚢 Titanic Dashboard · Built with Streamlit & Plotly · Data from titanic.csv"
    "</div>",
    unsafe_allow_html=True,
)

