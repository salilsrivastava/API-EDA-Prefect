from prefect import task
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from tasks.Visualization import save_plot

# Define colors for the heatmap
colors = ['#F93822','#FDD20E']

# Task to perform Chi-Squared Test for feature selection
@task(log_prints=True)
def chiSqauredTest(data, categorical_features):
    # Feature Selection for Categorical Features
    # Select all features except the last one as features
    features = data.loc[:,categorical_features[:-1]]
    # Select the last feature as target
    target = data.loc[:,categorical_features[-1]]
    
    # Apply SelectKBest with chi2 scoring function
    best_features = SelectKBest(score_func=chi2, k='all')
    fit = best_features.fit(features, target)
    
    # Create DataFrame with feature scores
    featureScores = pd.DataFrame(data=fit.scores_, index=list(features.columns), columns=['Chi Squared Score'])
    
    # Plotting the feature scores
    plt.subplots(figsize=(5,5))
    sns.heatmap(featureScores.sort_values(ascending=False, by='Chi Squared Score'), annot=True, cmap=colors, linewidths=0.4, linecolor='black', fmt='.2f')
    plt.title('Selection of Categorical Features')
    
    # Save the plot
    save_plot(plt, 'Selection of Categorical Features')
# Except RestingECG, all the remaining categorical features are pretty important for predicting heart diseases.