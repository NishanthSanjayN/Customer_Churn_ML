📌 Overview

Customer churn is one of the biggest challenges faced by subscription-based and service-oriented businesses. This project focuses on predicting whether a customer is likely to leave a company based on customer behavior, subscription details, and service usage patterns.

The project demonstrates a complete End-to-End Machine Learning Workflow from data preprocessing and model training to deployment using an interactive web application.

🚀 Highlights
✅ Built a complete Machine Learning pipeline for customer churn prediction
✅ Compared multiple classification algorithms for optimal performance
✅ Developed a real-time prediction system using <entity>Streamlit</entity>
✅ Performed feature engineering and exploratory data analysis
✅ Generated actionable business insights for customer retention
✅ Deployed a scalable and interactive ML application
✨ Features
⚡ Real-time customer churn prediction
🎨 Interactive and user-friendly Streamlit interface
🤖 Multiple ML models evaluated for best performance
🧹 Clean preprocessing and feature engineering pipeline
📊 Visual insights using graphs and charts
🚀 Deployable and scalable architecture
📈 Business-focused analytics and actionable insights
🎯 Problem Statement

Businesses lose significant revenue when customers stop using their services. Identifying potential churn customers beforehand helps organizations:

📉 Reduce customer attrition
💰 Increase revenue
🎯 Build targeted marketing strategies
😊 Improve customer satisfaction

This project uses Machine Learning Classification Algorithms to predict customer churn based on historical customer data.

💡 Why This Project Matters

Customer retention is critical because acquiring new customers costs significantly more than retaining existing ones. This system helps businesses proactively identify high-risk customers and improve retention strategies using data-driven insights.

🛠️ Tech Stack
Category	Technologies
Programming Language	Python
Data Analysis	Pandas, NumPy
Visualization	Matplotlib, Seaborn
Machine Learning	Scikit-learn
Deployment	Streamlit
Model Persistence	Pickle
Version Control	Git & GitHub
📊 Machine Learning Workflow
1️⃣ Data Collection
Imported telecom customer dataset
Checked null values and inconsistencies
Performed dataset understanding and validation
2️⃣ Data Preprocessing
Handled missing values
Label encoding and feature transformation
Feature scaling using StandardScaler
Cleaned and prepared data for model training
3️⃣ Exploratory Data Analysis (EDA)

Performed detailed visualization and analysis to identify customer churn patterns.

Analysis Included:
Customer churn distribution
Correlation analysis
Monthly charges comparison
Contract type analysis
Customer tenure visualization
Behavioral trend analysis
4️⃣ Model Training

Implemented and compared multiple Machine Learning models:

Model	Purpose
Logistic Regression	Baseline Classification
Decision Tree Classifier	Rule-Based Prediction
Random Forest Classifier	Ensemble Learning
5️⃣ Model Evaluation

Evaluated models using:

✅ Accuracy Score
✅ Precision
✅ Recall
✅ F1 Score
✅ Confusion Matrix
📈 Model Performance
Metric	Score
Accuracy	85%
Precision	83%
Recall	81%
F1 Score	82%

(Update these values based on your actual model performance)

6️⃣ Deployment
Built an interactive web application using <entity>Streamlit</entity>
Enabled real-time churn prediction
Deployed publicly for accessibility and testing
📈 Key Insights

🔹 Customers with higher monthly charges showed higher churn probability

🔹 Long-term customers were less likely to churn

🔹 Contract type and tenure significantly affected churn behavior

🔹 Automated payment methods improved customer retention

🖥️ Application Preview
Features Available in the Web App
📋 Customer detail input form
⚡ Instant churn prediction
📊 Probability-based prediction output
🎨 Interactive and responsive user interface
🏗️ System Architecture
Dataset → Data Preprocessing → Feature Engineering → ML Model Training → Model Evaluation → Streamlit Deployment → Real-Time Prediction
📂 Project Structure
Customer_Churn_ML/
│
├── app.py                     # Streamlit application
├── model.pkl                  # Trained ML model
├── scaler.pkl                 # Feature scaling object
├── requirements.txt           # Project dependencies
├── churn.csv                  # Dataset
├── notebooks/                 # Jupyter notebooks
├── images/                    # Screenshots & assets
└── README.md
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/NishanthSanjayN/Customer_Churn_ML.git

cd Customer_Churn_ML
2️⃣ Create Virtual Environment
python -m venv venv
3️⃣ Activate Environment
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
4️⃣ Install Dependencies
pip install -r requirements.txt
5️⃣ Run the Application
streamlit run app.py
🌐 Deployment

The project is successfully deployed using <entity>Streamlit</entity> Cloud.

🚀 Live Application

🔗 https://nishanthsanjayn-customer-churn-ml-app-u8j39t.streamlit.app/

📸 Screenshots
Add Screenshots of:
🏠 Home Page
📊 Prediction Interface
⚡ Prediction Results
📈 Graphs & Visualizations
🎯 Business Impact

This solution can help organizations:

✅ Reduce customer attrition
✅ Improve retention campaigns
✅ Increase customer lifetime value
✅ Enable data-driven decision making
🚀 Future Enhancements
🤖 Add Deep Learning models
📊 Integrate SHAP for Explainable AI
☁️ Deploy using Docker & AWS
🔐 Add authentication system
🗄️ Real-time database integration
📈 Advanced dashboard analytics
📚 Learning Outcomes

Through this project, I gained hands-on experience in:

✅ End-to-end ML pipeline development
✅ Data preprocessing and visualization
✅ Classification algorithms
✅ Model evaluation techniques
✅ Deployment using Streamlit
✅ Building production-ready ML applications
👨‍💻 Author
Nishanth Sanjay N

🎓 Final Year B.Tech Information Technology Student
🏫 MIT, Anna University

Passionate about:

Machine Learning
Full Stack Development
Scalable Systems
Software Engineering
Problem Solving
🔗 Connect With Me

📂 GitHub:
https://github.com/NishanthSanjayN

🌐 Live Project:
https://nishanthsanjayn-customer-churn-ml-app-u8j39t.streamlit.app/
