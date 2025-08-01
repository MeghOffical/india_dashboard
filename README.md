### 📊 Project Summary
An interactive dashboard for Indian district-level insights from Census, Health, Crime, and Budget datasets.

![Dashboard Preview](./Home_page.png)

## 📈 Dashboard Modules

Below are the four key analytical modules built into this project:

| Module | Preview | Description |
|--------|---------|-------------|
| 🧮 **Census 2011 Insights** | ![Census](./Census.png) | Analyze district-wise literacy, sanitation, housing, and infrastructure across India using Census 2011 data. |
| 🩺 **Health & Nutrition (NFHS-5)** | ![Health](./Health.png) | Visualize public health metrics like child stunting, anemia, immunization, and more from NFHS-5 survey. |
| 🕵️ **Crime Statistics (NCRB)** | ![Crime](./Crime.png) | Explore district and state-level crime rates and patterns using official NCRB reports. |
| 💰 **State Budget Spending** | ![Budget](./Budget.png) | Understand how state governments allocate and spend funds across health, education, and development. |

## 🚀 Live Demo

👉 **Streamlit App**: [https://indiadashboard-pefccic4eudc3vkrne5rvz.streamlit.app](https://indiadashboard-pefccic4eudc3vkrne5rvz.streamlit.app/)

---

## 📌 Project Overview

This dashboard helps users analyze and compare districts and states across multiple parameters such as:
- Literacy and sanitation (Census 2011)
- Health and nutrition indicators (NFHS-5)
- Crime statistics (NCRB)
- Budget and government expenditure (OpenBudgetsIndia)

It provides a comprehensive, visual understanding of regional development in India.

---

## 🧩 Features

- 📍 District-wise analysis with parameter filters
- 📊 Bar charts, maps, and correlation plots
- 🩺 Health outcomes like child stunting, anemia, and under-5 mortality
- ⚖️ State government budget visualizations by sector
- 🔒 Built with a clean Streamlit interface

---

## 🗂️ File Structure

```

india\_dashboard/
├── app.py                # Main Streamlit app
├── budget\_data.csv       # Budget and spending dataset
├── crime\_data.csv        # NCRB crime statistics
├── health\_data.csv       # NFHS-5 health and nutrition data
├── india\_data.csv        # Census 2011-based metrics
├── requirements.txt      # Python dependencies
└── README.md             # This file

````

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/MeghOffical/india_dashboard.git
cd india_dashboard
````

### 2. Install Dependencies

Make sure Python 3.9+ is installed.

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

---

## 📚 Data Sources

* 📌 [Census of India 2011](https://censusindia.gov.in)
* 🩺 [NFHS-5 Survey](http://rchiips.org/nfhs/)
* 🕵️ [NCRB Crime Statistics](https://ncrb.gov.in/)
* 💰 [OpenBudgetsIndia](https://openbudgetsindia.org)

---

## 📝 License

This project is open source feel free to contribute it.

---

## ⭐ Support

If you found this project useful or insightful, consider starring the repo and sharing it!

---

## 🙋 About the Creator

👤 **Megh Bavarva**  

I'm deeply passionate about **data science** and **data-driven storytelling**.  
This project was built as a way to apply **real-world data analysis** using IPL cricket data, and to showcase how raw CSVs can be transformed into actionable insights through APIs and dashboards.  

My primary interests are:
- **Data wrangling and feature engineering**
- **Building analytics pipelines**
- **Working with Pandas, NumPy, and ML tools**
- **Solving real-world problems using data**

Feel free to fork, star, or collaborate on data-focused projects!

🔗 GitHub: [@MeghOffical](https://github.com/MeghOffical)
