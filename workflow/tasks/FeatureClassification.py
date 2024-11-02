from prefect import task

# Task to classify features into categorical and numerical
@task(log_prints=True)
def featureClassification(df):
    # Get a list of column names
    col = list(df.columns)
    
    # Initialize lists for categorical and numerical features
    categorical_features = []
    numerical_features = []
    
    # Iterate over columns to classify features
    for i in col:
        if len(df[i].unique()) > 6:
            numerical_features.append(i)  # Add to numerical features if unique values > 6
        else:
            categorical_features.append(i)  # Add to categorical features otherwise
    
    # Print the classified features
    print('Categorical Features :', *categorical_features)
    print('Numerical Features :', *numerical_features)
    
    # Return the lists of categorical and numerical features
    return categorical_features, numerical_features