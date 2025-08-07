# 🏠 House Price Predictor

A machine learning project that predicts house prices based on user-provided features like location, Residential Type, Assessed Value and more. 
Built using Python, scikit-learn, XGBRegressor, and deployed with Streamlit. This app demonstrates a full end-to-end data science workflow 
from data preprocessing to model evaluation and interactive web app deployment.

---

## 📊 Project Overview

The goal of this project is to build a highly accurate regression model to estimate house prices using structured data. This project includes:

- 🔍 Exploratory Data Analysis (EDA)
- 🧹 Data Cleaning & Feature Engineering
- ⚙️ Model Selection & Hyperparameter Tuning
- ✅ Model Evaluation using MAE, RMSE, and R²
- 📈 Walk-Forward Validation for time-sensitive data
- 🖥️ Interactive Web Application using Streamlit
- 🚀 Deployment on Streamlit Cloud
- 📁 Version Control with Git & GitHub

---

## 🚀 Tech Stack

| Tool/Library       | Role                                |
|--------------------|-------------------------------------|
| Python             | Programming Language                |
| Pandas, NumPy      | Data Manipulation                   |
| Matplotlib, Seaborn| Data Visualization                  |
| Scikit-learn       | ML Pipelines & Metrics              |
| XGBRegressor       | Gradient Boosting Regressor         |
| Optuna             | Hyperparameter Optimization         |
| Streamlit          | App Development & Deployment        |
| Git, GitHub        | Version Control & Hosting           |

---

## 📁 File Structure
- House-price-app/
- │
- ├── data [Data.gov (U.S. Government Open Data ] (https://catalog.data.gov/dataset/real-estate-sales-2001-2018) 
- ├── models (XGBRegressor,LightGBM, Optuna)
- ├── images/ 
- ├── House_Price_Predictor.ipynb # Main Jupyter Notebook
- ├── streamlit_app.py # Streamlit application
- ├── requirements.txt # Python dependencies
- └── README.md # This file


---

## 📈 Model Performance

| Metric        | Value          |
|---------------|----------------|
| MAE (avg)     | ~52,975        |
| RMSE          | ~76,437        |
| R² Score      | 0.7494         |

Model: **XGBRegressor**, tuned with **Optuna**  
Validation: **Walk-forward cross-validation**

---

## 🧪 Features & Inputs

The model considers the following features:

- Assessed Value
- Residential Type
- Town
- Location (longitude & latitude)
- ... and more depending on the dataset

Users can interactively enter values into the web app to get real-time predictions.
(https://house-price-predictor-rucszqk499dmsxzyykk4bk.streamlit.app/)
---

## 🖥️ How to Run the App

### 🔧 Installation

```bash
git clone https://github.com/YourUsername/House-Price-Predictor.git
cd House-Price-Predictor
pip install -r requirements.txt
```
---
### ▶️ Run the App Locally
```bash
streamlit run streamlit_app.py
```
The app will open in your browser automatically.

---

### 🌐 Deployment
- The app is deployed and accessible here:
- 🔗 [Live Streamlit App] (https://house-price-predictor-rucszqk499dmsxzyykk4bk.streamlit.app/)

---

### ✨ Key Highlights
- ✅ Real-world ML pipeline with deployment
- 📦 Clean, modular code with sklearn Pipelines
- 📈 Custom evaluation with time-aware validation
- 🎯 Business impact: Practical for real estate agents, buyers, and sellers

---
### 🙋‍♂️ About Me
I'm a data enthusiast passionate about turning messy data into valuable insights and tools. 
This project showcases my ability to take a problem from data collection to deployment.

## 🔗 Connect with Me

- <img width="35" height="35" alt="image" src="https://github.com/user-attachments/assets/d41e481f-a8bd-4fd5-888f-9b4b1b519eae" />[LinkedIn](www.linkedin.com/in/obed-adonle-a72298376)
- <img width="30" height="30" alt="image" src="https://github.com/user-attachments/assets/a0c4a449-fb3c-4657-a6d5-7e0559dbe801" />[Portfolio & Dashboards(https://public.tableau.com/app/profile/obed.adonle/vizzes)
- <img width="35" height="35" alt="image" src="https://github.com/user-attachments/assets/49761877-99f2-423c-9e22-7ded6b648ccd" />[Mail Me @] (kwameasomu2032@gmail.com)
- <img width="35" height="35" alt="image" src="https://github.com/user-attachments/assets/787a3e42-6599-48db-9728-49184585d89f" />[WhatsApp] (+91 8891206376)



📄 License
This project is open-source and available under the MIT License.


---

### ✅ What to Do Next:

1. **Replace** placeholders like:
   - `YourUsername`
   - Your Streamlit app link
   - LinkedIn and Portfolio URLs

2. **Add an image** (optional):
   - Take a screenshot of your app
   - Save it as `house-price-app-screenshot.png` in an `images/` folder.

3. **Save this as** `README.md` in your project root.

4. Then run:
   ```bash
   git add README.md
   git commit -m "Add detailed project README"
   git push


