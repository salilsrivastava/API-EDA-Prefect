import pandas as pd
import numpy as np
import re
import io
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import os
from prefect import task

# Define colors for visualizations
colors = ['#F93822','#FDD20E']

@task(log_prints=True)
def catgegoricalViz(data, categorical_features):
    # Create subplots for categorical feature distributions
    fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(10, 15))
    for i in range(len(categorical_features) - 1):
        plt.subplot(3, 2, i+1)
        sns.distplot(data[categorical_features[i]], kde_kws={'bw': 1}, color=colors[0])
        title = 'Distribution : ' + categorical_features[i]
        plt.title(title)
        # plt.show()  # Uncomment if you want to show the plot
        save_plot(plt, title)
    
    # Plot the last categorical feature
    plt.figure(figsize=(4.75, 4.55))
    sns.distplot(data[categorical_features[len(categorical_features) - 1]], kde_kws={'bw': 1}, color=colors[0])
    title = 'Distribution : ' + categorical_features[len(categorical_features) - 1]
    plt.title(title)
    # plt.show()  # Uncomment if you want to show the plot
    save_plot(plt, title)

# All the categorical features are near about Normally Distributed.

@task(log_prints=True)
def numericalViz(data, numerical_features):
    # Distribution of Numerical Features
    fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 9.75))
    for i in range(len(numerical_features) - 1):
        plt.subplot(2, 2, i+1)
        sns.distplot(data[numerical_features[i]], color=colors[0])
        title = 'Distribution : ' + numerical_features[i]
        plt.title(title)
        # plt.show()  # Uncomment if you want to show the plot
        save_plot(plt, title)
    
    # Plot the last numerical feature
    plt.figure(figsize=(4.75, 4.55))
    sns.distplot(data[numerical_features[len(numerical_features) - 1]], kde_kws={'bw': 1}, color=colors[0])
    title = 'Distribution : ' + numerical_features[len(numerical_features) - 1]
    plt.title(title)
    # plt.show()  # Uncomment if you want to show the plot
    save_plot(plt, title)

# Oldpeak's data distribution is rightly skewed.
# Cholesterol has a bimodal data distribution.

@task(log_prints=True)
def catFeaturesVsTargetVar(data, categorical_features):
    # Create subplots for categorical features vs. target variable
    fig, ax = plt.subplots(nrows=3, ncols=2, figsize=(10, 12))  # Reduced figure size to make individual graphs smaller
    for i in range(len(categorical_features) - 1):
        plt.subplot(3, 2, i + 1)
        ax = sns.countplot(x=categorical_features[i], data=data, hue="HeartDisease", palette=colors, edgecolor='black')
        for rect in ax.patches:
            ax.text(rect.get_x() + rect.get_width() / 2, rect.get_height() + 2, rect.get_height(),
                    horizontalalignment='center', fontsize=9)
        title = categorical_features[i] + ' vs HeartDisease'
        plt.legend(['No Heart Disease', 'Heart Disease'], fontsize=8, loc='upper right')
        plt.title(title, fontsize=10)
    
    # Adjust spaces between subplots
    plt.subplots_adjust(hspace=0.5, wspace=0.4)  # Increase hspace and wspace for more spacing between plots
    # plt.show()  # Uncomment if you want to show the plot
    save_plot(plt, title)

# Male population has more heart disease patients than no heart disease patients. 
# In the case of Female population, heart disease patients are less than no heart disease patients.
# ASY type of chest pain boldly points towards major chances of heart disease.
# Fasting Blood Sugar is tricky! Patients diagnosed with Fasting Blood Sugar and no Fasting Blood Sugar have significant heart disease patients.
# RestingECG does not present with a clear cut category that highlights heart disease patients. 
# All the 3 values consist of high number of heart disease patients.
# Exercise Induced Angina definitely bumps the probability of being diagnosed with heart diseases.
# With the ST_Slope values, flat slope displays a very high probability of being diagnosed with heart disease. 
# Down also shows the same output but in very few data points.

def save_plot(plt, image_name):
    # Sanitize the image name to remove special characters and spaces
    sanitized_image_name = sanitize_filename(image_name)
    # Ensure the output directory exists
    output_dir = "../../output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # Save the plot to a buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    # Encode the image in base64 and log it
    # img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    full_path = os.path.join(os.path.dirname(__file__), output_dir, sanitized_image_name)
    plt.savefig(full_path)
    print(f"Plot saved at: {os.path.abspath(full_path)}")
    # Close the buffer
    buf.close()
    # plt.close()

def sanitize_filename(filename):
    # Remove special characters and spaces
    sanitized = re.sub(r'[^A-Za-z0-9_\-\.]', '', filename.replace(" ", ""))
    return sanitized
