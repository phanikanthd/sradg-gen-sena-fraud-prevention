# 🚀 Smarter Reconciliation and Anomaly Detection using Gen AI

## 📌 Table of Contents
- [Introduction](#-introduction)
- [Demo](#-demo)
- [Inspiration](#-inspiration)
- [What It Does](#-what-it-does)
- [How We Built It](#-how-we-built-it)
- [Challenges We Faced](#-challenges-we-faced)
- [How to Run](#-how-to-run)
- [Tech Stack](#-tech-stack)
- [Team](#-team)

---

## 🎯 Introduction
Reconciliation often involves comparing large datasets from different sources (e.g., financial transactions, inventory records) to identify mismatches or discrepancies. 
Traditional methods rely on rule-based algorithms or manual checks, which can be time-consuming and error-prone. 
Similarly, anomaly detection for fraud, errors, or deviations requires sophisticated pattern recognition and adaptive learning.

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
a genuine inspiration from our hackathon 2025 initiative, to produce some good solutions uisng latest gen AI.

## ⚙️ What It Does
-Automate the reconciliation process.

-Enhance accuracy in identifying mismatches and anomalies.

-Reduce manual intervention.

-Provide actionable insights for faster resolution.

## 🛠️ How We Built It
Generative AI-Powered Framework 
A. Data Preprocessing
Data Ingestion: We have used existing historical sample csv files for testing.
Data Cleaning & Normalization: Deploy AI models to handle missing values, standardize formats, and merge data from disparate systems.

B. Anomaly Detection
AI Models: Leverage pre-trained transformer models (Open AI - ChatGPT) to learn patterns in historical data.
Multi-Channel Inputs: Incorporate features such as timestamps, geolocation, and user behavior to enrich the detection process.
Real-Time Analysis: Use streaming services to flag anomalies as they occur.

C. Smart Reconciliation
Data Comparison: Use NLP-powered models to interpret and match textual or semi-structured data (e.g., invoice descriptions, payment memos).
Pattern Recognition: Train the AI to detect recurring reconciliation patterns, such as partial matches or compensating errors.
Confidence Scores: Provide probabilities for matching records to help prioritize manual reviews.

D. Generative Insights
Use Gen AI to generate summaries or explanations for flagged anomalies (e.g., "This transaction appears anomalous due to an outlier in payment frequency").
Generate suggestions for resolving discrepancies (e.g., "Consider verifying transaction XYZ from source A").

## 🚧 Challenges We Faced
How to present the agent using visualisations.

# 🏃 How to Run
1. Clone the repository  
   
2. Install dependencies  
   pip install streamlit pandas numpy scikit-learn matplotlib seaborn
   
4. Run the project  
   We need do the tunneling to run the application using streamlit.
   Ex: wget -q -O - ipv4.icanhazip.com   -->to get the password to access the application IP Address
     streamlit run app.py & npx localtunnel --port 8501
     you can use the goold colab to run the above steps to get our application.
     https://colab.research.google.com/
   ```

# 🏗️ Tech Stack
- 🔹 Frontend: Streamlit, seaborn and matplotlib for plotting and visualisation.
- 🔹 Models: Pandas and numpy for data preprocessing, kmeans for clusting and isolation forest for anomolies detection.

# 👥 Team
- Phani Kanth Daliparthi
- Tarun Kumar Kollipara
- Sruthi Malladi
- Ammanna babu Kagitha
