# File Name : visual.py
# Student Name: Uruz B, Shantele K, Nogaye G
# email:  bidiwaur@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:  3/27/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Created code for logoPackage and visualPackage to run the graph and picture

# Brief Description of what this module does.Added a chart and logo
# Citations: ChatGPT and Youtube

# Anything else that's relevant:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def load_data(filepath):
    """Loads the car price dataset from a CSV file."""
    return pd.read_csv(filepath)

def preprocess_data(df, features):
    """Preprocesses the dataset by selecting features and scaling them."""
    df = df.dropna()  # Remove missing values
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[features])
    return scaled_data

def perform_kmeans_clustering(data, n_clusters=3):
    """Performs K-Means clustering and returns the cluster labels."""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(data)
    return clusters, kmeans

def visualize_clusters(df, features, clusters):
    """Plots the clustered data."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df[features[0]], y=df[features[1]], hue=clusters, palette='viridis')
    plt.xlabel(features[0])
    plt.ylabel(features[1])
    plt.title('Car Price Clustering')
    plt.legend(title='Cluster')
    plt.show()
