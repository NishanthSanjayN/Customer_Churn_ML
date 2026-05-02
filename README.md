**Customer Churn Prediction System:**
AI-Powered Customer Retention Analytics using Machine Learning

**1. Overview:**
Customer churn is one of the biggest challenges faced by subscription-based and service-oriented businesses. This project focuses on predicting whether a customer is likely to leave a company based on customer behavior and service usage patterns.

The project includes:
1.Data preprocessing & feature engineering
2.Exploratory Data Analysis (EDA)
3.Machine Learning model training & evaluation
4.Real-time prediction using a deployed Streamlit app
5.Business insights for customer retention strategies

This project demonstrates a complete ML workflow from raw data to deployment.

**2. Features**
1.Predicts customer churn in real time
2.Interactive and user-friendly Streamlit interface
3.Multiple ML models evaluated for best performance
4.Clean preprocessing and feature engineering pipeline
5.Visual insights using plots and charts
6.Deployable and scalable architecture
7.Business-focused analytics and actionable insights

**3.Problem Statement**
Businesses lose significant revenue when customers stop using their services. Identifying potential churn customers beforehand helps companies:

>Improve customer retention
>Increase revenue
>Build targeted marketing strategies
>Enhance customer satisfaction

This project uses Machine Learning to classify whether a customer will churn based on historical customer data.

**4.Tech Stack**

1.Category	Technologies
Programming Language	Python
Data Analysis	Pandas, NumPy
Visualization	Matplotlib, Seaborn
Machine Learning	Scikit-learn
Deployment	Streamlit
Model Persistence	Pickle
Version Control	Git & GitHub


**5.Machine Learning Workflow**
1️⃣ Data Collection
Imported telecom customer dataset
Checked null values and inconsistencies

2️⃣ Data Preprocessing
Handled missing values
Label encoding & feature transformation
Feature scaling using StandardScaler

3️⃣ Exploratory Data Analysis
Churn distribution analysis
Correlation analysis
Customer behavior visualization

4️⃣ Model Training
Implemented and compared multiple models:
Logistic Regression
Decision Tree Classifier
Random Forest Classifier

5️⃣ Model Evaluation
Evaluated models using:
Accuracy Score
Precision
Recall
F1 Score
Confusion Matrix

6️⃣ Deployment
Built an interactive web app using Streamlit
Enabled real-time churn prediction

**Key Insights**

🔹 Customers with higher monthly charges showed higher churn probability
🔹 Long-term customers were less likely to churn
🔹 Contract type and tenure significantly affected churn behavior
🔹 Automated payment methods improved customer retention

**6.Application Preview:**
Features Available in the Web App
Customer detail input form
Instant churn prediction
Probability-based output
Interactive UI for easy usage

📂**Project Structure**
Customer_Churn_ML/
│
├── app.py                     # Streamlit application
├── model.pkl                  # Trained ML model
├── scaler.pkl                 # Scaler object
├── requirements.txt           # Dependencies
├── churn.csv                  # Dataset
├── notebooks/                 # Jupyter notebooks
├── images/                    # Screenshots/assets
└── README.md

⚙️ **Installation & Setup**
1.Clone the Repository
git clone https://github.com/NishanthSanjayN/Customer_Churn_ML.git
cd Customer_Churn_ML

2.Create Virtual Environment
python -m venv venv

3.Activate Environment
Windows
venv\Scripts\activate
Linux / Mac
source venv/bin/activate
4.Install Dependencies
pip install -r requirements.txt

5.Run the Application
streamlit run app.py

6.Deployment
The project is deployed using <entity>Streamlit</entity> Cloud.

**Live Application:**
🔗 https://nishanthsanjayn-customer-churn-ml-app-u8j39t.streamlit.app/

**7.Business Impact**
This solution can help organizations:

1.Reduce customer attrition
2.Improve retention campaigns
3.Increase customer lifetime value
4.Enable data-driven decision making

**8.Future Enhancements**
1.Add Deep Learning models
2.Integrate SHAP for explainability
3.Deploy using Docker & AWS
4.Add authentication system
5.Real-time database integration
6.Advanced dashboard analytics

**9.Learning Outcomes**
Through this project, I gained hands-on experience in:

>End-to-end ML pipeline development
>Data preprocessing & visualization
>Classification algorithms
>Model evaluation techniques
>Deployment using Streamlit
>Building production-ready ML applications

Author
Nishanth Sanjay N

Final Year B.Tech IT Student | MIT, Anna University

🔗 GitHub:
NishanthSanjayN GitHub
