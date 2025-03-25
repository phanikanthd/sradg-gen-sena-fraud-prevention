import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title('Anomaly Detection using Gen AI')

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Load CSV data into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display first few rows of the dataframe
    st.write("Data preview:")
    st.write(df.head())

    # Select numeric columns for anomaly detection and clustering
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    if len(numeric_columns) == 0:
        st.write("No numeric columns found for anomaly detection and clustering.")
    else:
        # Option to choose which columns to use for anomaly detection and clustering
        selected_columns = st.multiselect(
            "Select numeric columns for analysis", 
            options=numeric_columns, 
            default=numeric_columns
        )
        
        if len(selected_columns) > 0:
            # Perform anomaly detection using Isolation Forest
            st.subheader("Anomaly Detection using Isolation Forest")

            model_if = IsolationForest(contamination=0.05, random_state=42)
            df['Anomaly'] = model_if.fit_predict(df[selected_columns])
            df['Anomaly'] = df['Anomaly'].map({1: 'Normal', -1: 'Anomaly'})  # Mapping -1 to 'Anomaly' and 1 to 'Normal'

            # Display the rows that are detected as anomalies
            st.write("Anomalies detected:")
            anomalies_df = df[df['Anomaly'] == 'Anomaly']
            st.write(anomalies_df)

            # Visualizing anomalies with clustering
            st.subheader("Clustering using K-Means")

            # Perform KMeans clustering
            n_clusters = st.slider('Select number of clusters for K-Means', 2, 10, 3)
            model_kmeans = KMeans(n_clusters=n_clusters, random_state=42)
            df['Cluster'] = model_kmeans.fit_predict(df[selected_columns])

            # Display the cluster centers
            st.write("Cluster Centers:")
            st.write(model_kmeans.cluster_centers_)

            # Visualize the clustering results
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.scatterplot(x=df[selected_columns[0]], y=df[selected_columns[1]], hue=df['Cluster'], palette="Set1", ax=ax)
            ax.set_title("K-Means Clustering")
            st.pyplot(fig)

            # Visualize anomalies with clustering
            fig2, ax2 = plt.subplots(figsize=(8, 6))
            anomalies = df[df['Anomaly'] == 'Anomaly']
            sns.scatterplot(x=df[selected_columns[0]], y=df[selected_columns[1]], hue=df['Cluster'], palette="Set1", ax=ax2, legend=None)
            sns.scatterplot(x=anomalies[selected_columns[0]], y=anomalies[selected_columns[1]], color='red', label='Anomalies', ax=ax2)
            ax2.set_title("Anomalies with Clustering")
            ax2.legend()
            st.pyplot(fig2)

        else:
            st.write("Please select numeric columns for analysis.")
