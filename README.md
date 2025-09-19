# 📊 CORD-19 Data Explorer

This is a beginner project to explore the **CORD-19 metadata dataset**.  
It uses **pandas** for data handling, **matplotlib** for charts, and **Streamlit** for a simple web app.  

---

## 🚀 Steps I Did
1. Loaded the dataset (`metadata.csv`)  
2. Cleaned the data (fixed missing values, extracted year)  
3. Made two visualizations:  
   - Publications by Year  
   - Top Journals  
4. Built a Streamlit app with a slider for selecting year range  

---

## 📂 Files
- `analysis.ipynb` → Jupyter notebook with exploration and charts  
- `app.py` → Streamlit web app  
- `README.md` → Documentation  

---

## ⚙️ How to Run
Install required packages:
```bash
pip install pandas matplotlib seaborn streamlit
```

---

Run the Streamlit app:
```bash
streamlit run app.py
```

---

📝 Reflection

It was a bit challenging to handle missing values, but dropping them worked.

I learned how to use pandas.to_datetime() to extract years.

Streamlit was fun because I could add a slider and make the app interactive.


---






