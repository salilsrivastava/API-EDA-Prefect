from prefect import task
from sklearn.preprocessing import LabelEncoder

# Task to encode categorical features in the DataFrame
@task(log_prints=True)
def encodingData(df):
    # Initialize the LabelEncoder
    le = LabelEncoder()
    # Create a deep copy of the DataFrame
    df1 = df.copy(deep=True)
    
    # Encode the 'Sex' column
    df1['Sex'] = le.fit_transform(df1['Sex'])
    print(df1['Sex'])
    
    # Encode the 'ChestPainType' column
    df1['ChestPainType'] = le.fit_transform(df1['ChestPainType'])
    print(df1['ChestPainType'])
    
    # Encode the 'RestingECG' column
    df1['RestingECG'] = le.fit_transform(df1['RestingECG'])
    print(df1['RestingECG'])
    
    # Encode the 'ExerciseAngina' column
    df1['ExerciseAngina'] = le.fit_transform(df1['ExerciseAngina'])
    print(df1['ExerciseAngina'])
    
    # Encode the 'ST_Slope' column
    df1['ST_Slope'] = le.fit_transform(df1['ST_Slope'])
    print(df1['ST_Slope'])
    
    # Return the DataFrame with encoded features
    return df1

    
# Modifications in the original dataset will not be highlighted in this deep copy.
# Hence, we use this deep copy of dataset that has all the features converted into numerical values for visualization & modeling purposes.
