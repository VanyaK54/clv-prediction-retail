# 🛍️ Customer Lifetime Value (CLV) Prediction – Retail & E-Commerce

Predict the long-term value a customer brings to a business using transactional and behavioral data. Built with Python, MS SQL, Power BI, Azure, and ML — this project is tailored to real-world retail needs in the Canadian market.

---

## 📌 Objective

To accurately forecast Customer Lifetime Value using:
- RFM (Recency, Frequency, Monetary) features
- Clickstream & website visit behavior
- Demographics and transactional summaries

---

## 🛠️ Tech Stack

**Languages**: Python, SQL  
**Database**: Azure SQL, MS SQL Server  
**Cloud**: Azure Blob Storage, Azure ML  
**Dashboards**: Power BI, Streamlit  
**Libraries**: Scikit-learn, XGBoost, pandas, seaborn  
**Tools**: Jupyter, pyodbc, joblib, dotenv

---

## 🗂️ Folder Structure

```bash
clv-prediction-retail/
├── data/ # Raw + processed CSVs
├── notebooks/ # EDA + training notebooks
├── src/ # Python scripts
├── dashboards/ # Power BI + Streamlit apps
├── models/ # Trained ML models
├── sql/ # Azure/MS SQL schema
├── outputs/ # Visuals + reports
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## 📊 Power BI Dashboard

- CLV distribution
- High-value vs low-value customer segmentation
- Regional & behavioral breakdowns
- Filters: age, gender, country, recency

---

## 🌐 Streamlit App (Optional)

- Upload customer CSV
- Get CLV predictions
- Download results

---

## ☁️ Azure Integration

- Azure Blob for storing CSVs
- Azure SQL for data and dashboards
- .env file holds connection strings securely

---

## 🚀 How to Run

```bash
# Clone repo
git clone https://github.com/VanyaK54/clv-prediction-retail.git

# Install requirements
pip install -r requirements.txt

# Run model training
python src/clv_model.py

# Predict CLV on new data
python src/predict.py

# Launch web app
streamlit run dashboards/streamlit_app.py
