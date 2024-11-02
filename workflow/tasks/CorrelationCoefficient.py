# CorrelationCoefficient.py

import matplotlib.pyplot as plt
import seaborn as sns
from prefect import task
from tasks.Visualization import save_plot

# Define colors for the heatmap
colors = ['#F93822', '#FDD20E']

# Task to calculate and plot the correlation matrix
@task(log_prints=True)
def correlationCoff(data):
    # Calculate correlation matrix
    correlation_matrix = data.corr()
    # Plot correlation matrix
    plt.figure(figsize=(20, 5))
    sns.heatmap(correlation_matrix, cmap=colors, annot=True)
    save_plot(plt, 'Correlation Matrix')

# Note: It is a huge matrix with too many features.
# We will check the correlation only with respect to HeartDisease.
@task(log_prints=True)
def correlationCoffWithHearDisease(data):
    # Calculate correlations with respect to HeartDisease
    corr = data.corrwith(data['HeartDisease']).sort_values(ascending=False).to_frame()
    corr.columns = ['Correlations']
    # Plot the correlations with HeartDisease
    plt.subplots(figsize=(5, 5))
    sns.heatmap(corr, annot=True, cmap=colors, linewidths=0.4, linecolor='black')
    plt.title('Correlation w.r.t HeartDisease')
    save_plot(plt, 'CorrelationWithHeartDisease')

# Except for RestingBP and RestingECG, everyone displays a positive or negative relationship with HeartDisease.
