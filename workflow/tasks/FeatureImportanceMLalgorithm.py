from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import RepeatedStratifiedKFold
from prefect import task
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Define colors for future plots (though not used in this function)
colors = ['#F93822','#FDD20E']

# Task to train and evaluate a Machine Learning model
@task(log_prints=True)
def mlAlgo(data):
    # Select features and target variable
    features = data[data.columns.drop(['HeartDisease','RestingBP','RestingECG'])].values
    target = data['HeartDisease'].values
    
    # Split the data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.20, random_state=2)
    
    # Initialize the RandomForestClassifier
    classifier  = RandomForestClassifier(max_depth=4, random_state=0)
    
    # Fit the classifier on the training data
    classifier.fit(x_train, y_train)
    
    # Make predictions on the test data
    prediction = classifier.predict(x_test)
    
    # Calculate and print the accuracy of the model
    print("Accuracy:", '{0:.2%}'.format(accuracy_score(y_test, prediction)))

# Accuracy :  84.24%
