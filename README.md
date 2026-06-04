# 📊 Student Performance Analyzer   

## 🚀 Overview

**Student Performance Analyzer** is a web-based application built using Python that analyzes student academic data to identify performance trends, top performers, and weak students. It also includes basic machine learning to predict pass/fail outcomes.

---

## 🎯 Features

* 📊 Calculate average marks of students
* 🏆 Identify topper
* ⚠️ Detect weak students
* 📈 Visualize performance using bar charts
* 🌐 Web interface using Flask
* 🤖 Basic Machine Learning (Pass/Fail Prediction)

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** Pandas, Matplotlib, Scikit-learn
* **Framework:** Flask
* **Frontend:** HTML, CSS
* **IDE:** VS Code

---

## 📁 Project Structure

```
student-performance-analyzer/
│
├── analyzer.py              # Core analysis script
├── app.py                   # Flask web app
├── students.csv             # Dataset
├── templates/
│     └── index.html         # Frontend UI
```

---

## 📊 Dataset

Sample dataset used:

```
Name,Maths,Science,English,Attendance
Aman,85,78,92,88
Riya,90,88,95,92
Rahul,40,45,50,60
Sneha,72,70,68,80
Arjun,30,35,40,55
Priya,88,90,85,95
```

---

## ▶️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/student-performance-analyzer.git
cd student-performance-analyzer
```

### 2️⃣ Install Dependencies

```
pip install pandas matplotlib scikit-learn flask
```

### 3️⃣ Run Application

```
python app.py
```

### 4️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 📈 How It Works

1. Loads student dataset (CSV)
2. Calculates average marks
3. Identifies topper and weak students
4. Displays results on web interface
5. (Optional) Uses ML model to predict pass/fail

---

## 🤖 Machine Learning

* Model: Logistic Regression
* Input Features: Marks + Attendance
* Output: Pass (1) / Fail (0)

---

## 🚀 Future Enhancements

* 📁 Upload CSV file feature
* 📊 Interactive charts (dashboard)
* 🗄️ Database integration
* 🌐 Deployment (Heroku / Render)
* 🤖 Advanced ML models

---

## 💼 Resume Description

Developed a web-based application using Python, Pandas, and Flask to analyze student performance data. Implemented data processing, visualization, and machine learning techniques to identify top performers and predict student outcomes.

---

## 📌 Author

**Anoop**

---

## ⭐ Contribute

Feel free to fork this repository and improve the project!

---

## 📜 License

This project is open-source and available under the MIT License.
