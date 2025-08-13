# 🌍 COVID-19 Global Dashboard

A data science project that visualizes and analyzes the global impact of COVID-19 using real-time data from [Our World in Data](https://ourworldindata.org/coronavirus). The dashboard is built with Streamlit and includes interactive charts, forecasting using Prophet, and global maps with Plotly.

---

## 📌 Features

- 🗺️ Global and country-specific COVID-19 data
- 📊 Interactive plots of daily cases, deaths, and vaccinations
- 🔮 Time series forecasting using Prophet
- 🌍 Choropleth maps of global spread and vaccination rates
- 📅 Date filtering with sliders
- 💡 Built as a hands-on data science learning project

---

## 🧰 Tech Stack

- **Python**
- **Pandas** – Data cleaning and wrangling
- **Matplotlib / Seaborn** – Visualizations
- **Plotly Express** – Interactive maps
- **Prophet** – Forecasting daily cases
- **Streamlit** – Dashboard UI

---

## 📦 Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/covid-dashboard.git
cd covid-dashboard
```
(Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```
Install dependencies

```bash
pip install -r requirements.txt
Run the Streamlit app
```

```bash
streamlit run app.py
```
📁 Project Structure

covid-global-dashboard/
│
├── data/
│   ├── raw/
│   │   └── owid-covid-data.csv
│   └── processed/
│       └── preprocessed_data.csv
│
├── notebooks/
│   ├── 0_data_preprocessed.ipynb
├── 1_visualized_key_trends.ipynb
├── 2_streamlit_dashboard.py
├── 3_forecasting_prophet.ipynb
├── 4_interactive_map.ipynb
│
├── requirements.txt
└── README.md

📊 Data Source
- 📥 [OWID COVID-19 Data](https://github.com/owid/covid-19-data/tree/master/public/data)  
  - Raw: `data/raw/owid-covid-data.csv`  
  - Cleaned: `data/processed/preprocessed_data.csv`

This dataset is updated daily and includes global COVID-19 cases, deaths, testing, vaccinations, and policy responses.

📈 Learning Goals
This project was created to:

- Practice real-world data cleaning and analysis
- Build an interactive Streamlit dashboard
- Explore time series forecasting
- Learn data visualization and mapping

✍️ Author
@ThilinaGunathilaka

📃 License
This project is licensed under the MIT License.
