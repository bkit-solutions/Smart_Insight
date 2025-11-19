# Smart_Insight  
### Student Performance Prediction & Analytics System

Smart_Insight is a machine learning–powered web application built using **Flask**, designed to predict a student’s academic performance based on key demographic and socio‑educational factors such as gender, ethnicity, parental education, lunch type, and test preparation status.

This project also includes a detailed dataset visualization dashboard for deeper insights.

---

## 🚀 Features

### 🔹 ML-Based Score Prediction  
Predicts scores for **Maths**, **Reading**, and **Writing** using a trained regression model.

### 🔹 Interactive UI  
A clean, modern, two‑panel interface for input & results.

### 🔹 Loading Animation  
Simulates real ML processing for a better user experience.

### 🔹 Dataset Visualization  
Integrated SweetViz report for comprehensive statistical analysis.

### 🔹 Professional Layout  
Landing page, prediction page, result dashboard — all built with a consistent blue-white professional theme.

---

## 📁 Project Structure

```
Smart_Insight/
│── templates/
│   ├── landing.html
│   ├── predictor_form.html
│   ├── result_form.html
│   ├── Report.html
│
│── StudentsPerformance.csv
│── model.sav
│── app.py
│── requirements.txt
│── README.md   ← you are here
```

---

## 🛠️ Setup Instructions

### 1️⃣ Create a Virtual Environment  
It is recommended to use a virtual environment.

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 2️⃣ Install Required Dependencies

```
pip install -r requirements.txt
```

Ensure packages like Flask, pandas, SweetViz, and scikit‑learn are installed.

---

### 3️⃣ Run the Application  
Start the local server using:

```
python app.py
```

You should see:
```
Running on http://127.0.0.1:5000/
```

Open this address in your browser.

---

## 📊 Dataset  
The project uses the **Students Performance Dataset (1000 rows)** which contains:  
- Gender  
- Race/Ethnicity  
- Parental Level of Education  
- Lunch Type  
- Test Preparation Course  
- Math, Reading & Writing Scores  

The ML model is built using preprocessed one‑hot encoded features.

---

## 🧠 Machine Learning Model  
- Algorithm: **Regression (Linear/RandomForest based depending on training)**  
- Uses one‑hot encoding for categorical inputs  
- Predicts 3 output scores simultaneously  
- Model stored as: `model.sav`

---

## 📈 Visualisation  
The app includes a **SweetViz dashboard** accessible via:

👉 *“View Dataset Insights”* or  
👉 `/visualisation` route

This report shows:  
- Distributions  
- Correlations  
- Demographic impact comparisons  
- Statistical summaries  

---

## 🎨 UI/UX  
Designed with:  
- Bootstrap 5  
- Custom animations  
- Professional corporate blue‑white theme  
- Responsive layouts  
- Loading overlay animation  

---

## 🧪 Testing  
Try different combinations of gender, education, and test preparation to see how the model reacts.

---

## 🤝 Contributions  
Feel free to fork, improve the UI, retrain the model, or integrate additional ML components.

---

## 📜 License  
This project is created for **Final Year Academic Use** and can be freely modified for educational purposes.

---

## 👨‍💻 Author  
**Created By:** BKIT Solutions
*Final Year Project — Data Science Track*

---

Enjoy exploring insights with **Smart_Insight**! 🚀  
