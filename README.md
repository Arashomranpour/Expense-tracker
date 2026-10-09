<div align="center">

# 💸 Income & Expense Tracker

**A Streamlit app to record monthly income and expenses and visualize where the money goes with a Sankey diagram.**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white)

</div>

---

## ✨ Features

- 📝 **Data Entry** - choose a month and year, enter income (Salary, Hustle, Other Income) and expenses (Rent, Utilities, Groceries, Car, Other Expenses, Saving), add an optional comment and save.
- 📊 **Data Visualization** - pick a saved period and see income flowing into expense categories as a **Sankey chart**, with totals.
- 🗄️ Reports are stored per period (`monthly_reports`) in a Deta Base database.
- 🧭 Clean navigation with `streamlit-option-menu`.

## 🚀 Getting Started

```bash
git clone https://github.com/Arashomranpour/Expense-tracker.git
cd Expense-tracker
pip install streamlit plotly streamlit-option-menu deta
```

Set your own Deta project key in `database.py` (ideally read from an environment variable or Streamlit secrets), then:

```bash
streamlit run app.py
```

> ℹ️ Deta Base (the original Deta Space service) has been wound down. To keep using the app, swap `database.py` for another store (SQLite, Firebase, ...); only four small functions are involved.

## 📁 Project Structure

```
.
├── app.py          # Streamlit UI: data entry + Sankey visualization
└── database.py     # Storage layer (insert / fetch periods)
```

## 🛠️ Tech Stack

`Streamlit` · `Plotly` · `streamlit-option-menu` · `Deta Base`
