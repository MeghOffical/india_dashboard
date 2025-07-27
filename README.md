---

````markdown
# 🇮🇳 Demographix: Indian District Intelligence Dashboard

[![Made with Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange?style=for-the-badge&logo=streamlit)](https://streamlit.io)
[![GitHub Repo](https://img.shields.io/badge/Source-GitHub-black?style=for-the-badge&logo=github)](https://github.com/MeghOffical/india_dashboard)
[![Live Demo](https://img.shields.io/badge/Live_App-Click_Here-brightgreen?style=for-the-badge&logo=google-chrome)](https://indiadashboard-pefccic4eudc3vkrne5rvz.streamlit.app/)

> A data-rich, interactive dashboard visualizing district-level Indian statistics—covering Census 2011, Health (NFHS), Crime (NCRB), and Government Spending using OpenBudgetsIndia.

---

## 📊 Project Overview

**Demographix** is an open-source, multi-part dashboard project that brings together crucial datasets from various public domains to provide insights into India's development across regions.

It allows users to:
- Analyze and compare districts across literacy, sanitation, infrastructure.
- Explore health and nutrition metrics from NFHS-5.
- View government spending and budgeting at the state level.
- Identify development gaps using ranked indicators and charts.

🔗 **Live Demo**: [https://indiadashboard-pefccic4eudc3vkrne5rvz.streamlit.app](https://indiadashboard-pefccic4eudc3vkrne5rvz.streamlit.app)

---

## 🧩 Features

### ✅ Part 1: Census 2011 Analysis
- Explore literacy rates, toilet facilities, housing, and more at district level.
- Heatmaps, bar charts, and ranking tables for visual insights.

### ✅ Part 2: State & District-Level Rankings
- Compare parameters like Female Literacy, Pucca Housing, and Sanitation.
- See top/bottom ranked districts in each state.

### ✅ Part 3: Health & Nutrition (NFHS-5)
- Indicators like stunting, wasting, anemia, under-5 mortality.
- Geospatial mapping and multi-indicator correlation.

### 🔜 Part 4: Air Quality and Exposure (Coming Soon)
- Population-weighted AQI exposure metrics.
- District-level air quality analysis.

### ✅ Part 5: Budget & Spending (OpenBudgetsIndia)
- Explore government expenditure by state across categories like Health, Education, and Rural Development.

---

## 📂 Project Structure

```bash
india_dashboard/
├── pages/
│   ├── 1_Census_Analysis.py
│   ├── 2_Statewise_Rankings.py
│   ├── 3_Health_Nutrition.py
│   ├── 4_AirQuality_Exposure.py   # (coming soon)
│   └── 5_Budget_Spending.py
├── data/
│   ├── census_2011.csv
│   ├── nfhs_5_district.csv
│   ├── state_budgets.csv
│   └── district_centroids.csv
├── Home.py
├── utils.py
└── README.md
````

---

## 📌 Tech Stack

* **Frontend**: [Streamlit](https://streamlit.io)
* **Visualization**: [Plotly](https://plotly.com), [Pandas](https://pandas.pydata.org/)
* **Data Sources**:

  * [Census 2011 India](https://censusindia.gov.in)
  * [NFHS-5 (Health Survey)](http://rchiips.org/nfhs/)
  * [NCRB Crime Stats](https://ncrb.gov.in)
  * [OpenBudgetsIndia](https://openbudgetsindia.org)

---

## 🚀 Getting Started

### 🔧 Requirements

* Python 3.9+
* Install dependencies:

```bash
pip install -r requirements.txt
```

### ▶️ Run the App

```bash
streamlit run Home.py
```

---

## 📸 Dashboard Preview

| Census Insights                                                                     | Health Overview                                                                     | Budget Trends                                                                       |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| ![census](https://github.com/MeghOffical/india_dashboard/assets/preview-census.png) | ![health](https://github.com/MeghOffical/india_dashboard/assets/preview-health.png) | ![budget](https://github.com/MeghOffical/india_dashboard/assets/preview-budget.png) |

---

## 📢 Acknowledgements

* Government of India for open data sources.
* Streamlit & Plotly for free tools to build amazing dashboards.

---

## ✍️ Author

**Megh Bavarva**
💼 [GitHub](https://github.com/MeghOffical) | 🌐 [LinkedIn](https://linkedin.com/in/meghbavarva) | 📫 [meghbavarva@gmail.com](mailto:meghbavarva@gmail.com)

---

## ⭐️ Show Your Support

If you find this project useful, don't forget to give it a ⭐️ on GitHub and share it!

---

```

---

### ✅ Next Steps for You:
- Add actual image previews to the GitHub repo (`assets/preview-census.png`, etc.) or remove that preview section.
- Update the `requirements.txt` if not already included.
- Push this `README.md` to the root of your GitHub repository.

Would you like me to **create and upload preview images** or help format cards/tabs on the front page too?
```
