import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

tab1, tab2, tab3 = st.tabs(["📊 Overview", "🔮 Forecast", "🗺️ Map"])

with tab1:
    # Load the OWID dataset
    @st.cache_data
    def load_data():
        url = "data/processed/preprocessed_data.csv"
        df = pd.read_csv(url, parse_dates=['date'])
        df = df[df['continent'].notna()]  # Filter out aggregate rows
        return df

    df = load_data()
    st.title("🌍 COVID-19 Global Dashboard")

    # Sidebar: country selection
    countries = sorted(df['location'].unique())
    selected_country = st.sidebar.selectbox("Select a Country", countries)

    # Filter data
    country_df = df[df['location'] == selected_country]

    # Show KPIs
    latest = country_df.sort_values('date').iloc[-1]
    st.metric("Total Cases", f"{int(latest['total_cases']):,}")
    st.metric("Total Deaths", f"{int(latest['total_deaths']):,}")
    st.metric("People Fully Vaccinated", f"{int(latest['people_fully_vaccinated']):,}")


    # Plot daily new cases
    st.subheader("📈 Daily New Cases")
    fig, ax = plt.subplots()
    ax.plot(country_df['date'], country_df['new_cases'], label="New Cases")
    ax.set_xlabel("Date")
    ax.set_ylabel("New Cases")
    ax.legend()
    st.pyplot(fig)


### Add Forecasting (Prophet)

from prophet import Prophet

# Prepare data
forecast_df = country_df[['date', 'new_cases']].rename(columns={'date': 'ds', 'new_cases': 'y'})
forecast_df = forecast_df.dropna()

# Train model
m = Prophet()
m.fit(forecast_df)

# Future dates
future = m.make_future_dataframe(periods=30)
forecast = m.predict(future)

with tab2:
    # Plot
    st.subheader("🔮 Forecast: Daily New Cases (Next 30 Days)")
    fig2 = m.plot(forecast)
    st.pyplot(fig2)

### Add Interactive Maps (Plotly or Folium)

import plotly.express as px

latest_date = '2022-08-14'

# Get latest data per country
latest_date = df['date'].max()
latest_df = df[df['date'] == latest_date].copy()
latest_df['cases_per_million'] = latest_df['total_cases'] / latest_df['population'] * 1e6

with tab3:
    st.subheader("🗺️ Total COVID-19 Cases per Million (Map)")

    fig_map = px.choropleth(
        latest_df,
        locations="location",
        locationmode="country names",
        color="cases_per_million",
        hover_name="location",
        color_continuous_scale="OrRd",
        title="Cases per Million"
    )
    st.plotly_chart(fig_map)