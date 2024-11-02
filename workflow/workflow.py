from prefect import flow, task
import os
import pandas as pd
from tasks.BasicStats import basicStats
from tasks.FeatureClassification import featureClassification
from tasks.Encoding import encodingData
from tasks.Normalization import normalization
from tasks.CorrelationCoefficient import correlationCoff, correlationCoffWithHearDisease
from tasks.Visualization import catgegoricalViz, numericalViz, catFeaturesVsTargetVar
from tasks.ChiSquaredTest import chiSqauredTest
from tasks.FeatureImportanceMLalgorithm import mlAlgo

# Task to read data from CSV
@task(log_prints=True)
def read_data():
    print("Dataset loading...")
    # Load the dataset from the specified path
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), "../data", "heart.csv"))
    print("Dataset loaded successfully.")
    return df

# Define the main flow for data processing and analysis
@flow(log_prints=True)
def main_flow():
    # Read the data
    data = read_data()
    
    # Perform basic statistical analysis on the data
    basicStats(data, wait_for=[data])
    
    # Classify features into categorical and numerical
    categorical_features, numerical_features = featureClassification(data, wait_for=[data])
    
    # Encode categorical data
    data_encoded = encodingData(data, wait_for=[data])
    
    # Visualize categorical features
    catgegoricalViz(data_encoded, categorical_features, wait_for=[data_encoded])
    
    # Visualize numerical features
    numericalViz(data, numerical_features)
    
    # Visualize categorical features vs target variable
    catFeaturesVsTargetVar(data, categorical_features)
    
    # Normalize the data
    data_norm = normalization(data_encoded, wait_for=[data_encoded])
    
    # Calculate correlation coefficients
    correlationCoff(data_norm, wait_for=[data_norm])
    correlationCoffWithHearDisease(data_norm, wait_for=[data_norm])
    
    # Perform Chi-Squared Test on categorical features
    chiSqauredTest(data_norm, categorical_features, wait_for=[data_norm, categorical_features])
    
    # Apply Machine Learning algorithm to assess feature importance
    mlAlgo(data_norm, wait_for=[data_norm])

# Execute the main flow if this script is run directly
if __name__ == "__main__":
    main_flow.serve(name="Assignment1-Pt2-HeartFailure-Workflow",
                    tags=["Heart Failure Predication"],
                    parameters={},
                    interval=120)
