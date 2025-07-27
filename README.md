```# 🇮🇳 Demographix: Indian District Intelligence Dashboard

[![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-orange)](https://streamlit.io/) [![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/) [![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 🔍 Overview

**Demographix** is an interactive, district‑level data visualization platform built with Streamlit. It empowers users to explore and compare key socio‑economic, health, crime, and budget indicators across India’s 28 states, 8 union territories, and 600+ districts—leveraging Census 2011 and other public datasets.

<p align="center">
  <img src="screenshots/homepage.png" alt="Demographix Home" width="700"/>
</p>

---

## 🚀 Features

- **Full‑screen, responsive UI** with modern glassmorphism cards  
- **Four modules**:  
  - 📊 Census & Demographics  
  - 🛡️ Crime Data  
  - 💉 Health & Nutrition  
  - 💰 Budget & Spending  
- **Interactive Mapbox charts** powered by Plotly Express  
- **Top‑5 ranking tables** for quick insights  
- **Customizable parameters**: state, year (crime), primary & secondary metrics  
- **Clean landing page** summarizing purpose, data sources, and usage  

---

## 🗂️ Data Sources

| Module                  | Source                                                                                                             |
|-------------------------|--------------------------------------------------------------------------------------------------------------------|
| Census & Demographics   | [Census 2011 (Kaggle)](https://www.kaggle.com/datasets/rohanrao/indian-census)                                     |
| Crime Data              | NCRB district‑wise crime statistics (public domain releases)                                                       |
| Health & Nutrition      | NFHS‑5 district‑level indicators (Government of India datasets)                                                    |
| Budget & Spending       | OpenBudgetsIndia state‑level allocations & GVA data                                                                |

Place your CSV files (`india_data.csv`, `crime_data.csv`, `health_data.csv`, `budget_data.csv`) in the project root or update paths in `app.py`.

---

## 🛠️ Tech Stack

- **Python 3.8+**  
- **Streamlit** for the web UI  
- **Pandas & NumPy** for data processing  
- **Plotly Express + Mapbox** for interactive geospatial charts  
- **Embedded HTML/CSS** for custom styling  

---

## 📥 Installation & Quick Start

1. **Clone the repository**  
   ```bash
   git clone https://github.com/MeghOffical/india_dashboard.git
   cd india_dashboard ```

2. **Create a virtual environment** (optional)

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Run the app**

   ```bash
   streamlit run app.py
   ```

5. **Open** the URL shown in terminal (usually `http://localhost:8501`)

---

## 📖 Usage

1. **Landing Page**

   * Overview, data sources, and how to use instructions.

2. **Explore Modules**

   * Use the sidebar to select Census, Crime, Health or Budget.
   * Choose filters: State, Year (for crime), and metrics.
   * Click **Plot Graph** to view interactive maps and tables.

3. **Interactivity**

   * Pan/zoom on maps, hover for tooltips, and export charts via Plotly’s toolbar.

---

## 🤝 Contributing

1. **Fork** this repository
2. **Create** a feature branch:

   ```bash
   git checkout -b feature/my-new-feature
   ```
3. **Commit** your changes:

   ```bash
   git commit -m "Add awesome feature"
   ```
4. **Push** to your branch:

   ```bash
   git push origin feature/my-new-feature
   ```
5. **Open** a Pull Request

Please follow existing code style and update this README as needed.

---

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## 👨‍💻 Author

**Megh Bavarva**

* GitHub: [@MeghOffical](https://github.com/MeghOffical)
* Email: [megh@example.com](mailto:megh@example.com)

<p align="center">✨ Happy Data Exploration! ✨</p>
```
