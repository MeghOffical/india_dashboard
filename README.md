````md
# 🇮🇳 Demographix: Indian District Intelligence Dashboard

[![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-orange)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 🔍 Overview

**Demographix** is an interactive, district-level data visualization platform built using **Streamlit**. It empowers users to explore and compare key **socio-economic**, **health**, **crime**, and **budget** indicators across India’s 28 states, 8 union territories, and 600+ districts — all powered by open government datasets like **Census 2011**, **NFHS-5**, and **OpenBudgetsIndia**.

<p align="center">
  <img src="screenshots/homepage.png" alt="Demographix Home" width="700"/>
</p>

---

## 🚀 Features

- ✅ Full-screen, responsive UI with modern glassmorphism cards  
- 🧭 Modular layout:
  - 📊 **Census & Demographics**
  - 🛡️ **Crime Data**
  - 💉 **Health & Nutrition**
  - 💰 **Budget & Spending**
- 🌐 Interactive Mapbox geospatial charts
- 📈 Top-5 ranked tables by selected indicators
- ⚙️ Customizable filters for State, Year, and Parameters
- 🧹 Clean landing page with summary, sources, and instructions

---

## 🗂️ Data Sources

| Module               | Source                                                                                      |
|----------------------|---------------------------------------------------------------------------------------------|
| Census & Demographics | [Census 2011 - Kaggle](https://www.kaggle.com/datasets/rohanrao/indian-census)             |
| Crime Data           | NCRB District-wise Crime Statistics (Govt. of India - Open Data)                           |
| Health & Nutrition   | NFHS-5 (National Family Health Survey) - India District Factsheets                        |
| Budget & Spending    | [OpenBudgetsIndia](https://openbudgetsindia.org/) - State-level GVA, Expenditure, and more |

📁 Place your CSV files (`india_data.csv`, `crime_data.csv`, `health_data.csv`, `budget_data.csv`) in the project root or update the paths in `app.py`.

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **Streamlit** – frontend web app
- **Pandas, NumPy** – data processing
- **Plotly Express + Mapbox** – for interactive maps & graphs
- **HTML & CSS (inline)** – for layout styling and enhancements

---

## 📥 Installation & Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/MeghOffical/india_dashboard.git
   cd india_dashboard
````

2. **Create a virtual environment** (optional but recommended)

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # For Linux/Mac
   .venv\Scripts\activate         # For Windows
   ```

3. **Install the dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

5. Open your browser and go to `http://localhost:8501`

---

## 📖 How to Use

1. **Landing Page**

   * Overview, purpose, modules, and dataset summaries.

2. **Explore Any Module**

   * Choose a module from sidebar (Census, Crime, Health, Budget).
   * Use filters like *State*, *Year*, *Primary Parameter*, *Secondary Parameter*.
   * Click **Plot Graph** to visualize.

3. **Interactivity**

   * Hover over map charts to see details.
   * Zoom, pan, or export graphs using Plotly toolbar.

---

## 🤝 Contributing

Want to contribute? Great! Follow these steps:

1. **Fork** this repo.
2. **Create a feature branch**

   ```bash
   git checkout -b feature/my-new-feature
   ```
3. **Commit your changes**

   ```bash
   git commit -m "Add my feature"
   ```
4. **Push to GitHub**

   ```bash
   git push origin feature/my-new-feature
   ```
5. **Open a Pull Request** – We'll review and merge!

Please follow the existing coding style and update the README or documentation if necessary.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Megh Bavarva**
📧 [megh@example.com](mailto:megh@example.com)
🔗 GitHub: [@MeghOffical](https://github.com/MeghOffical)

<p align="center"><b>✨ Happy Exploring – Data speaks louder than words! ✨</b></p>
```

---
