from sklearn.preprocessing import MinMaxScaler, StandardScaler
from prefect import task

# Task to normalize and standardize features in the DataFrame
@task(log_prints=True)
def normalization(df1):
    # Initialize MinMaxScaler for normalization
    mms = MinMaxScaler()  # Normalization
    
    # Initialize StandardScaler for standardization
    ss = StandardScaler()  # Standardization
    
    # Normalize 'Oldpeak' feature (right skewed data distribution)
    df1['Oldpeak'] = mms.fit_transform(df1[['Oldpeak']])
    
    # Standardize normally distributed features
    df1['Age'] = ss.fit_transform(df1[['Age']])
    df1['RestingBP'] = ss.fit_transform(df1[['RestingBP']])
    df1['Cholesterol'] = ss.fit_transform(df1[['Cholesterol']])
    df1['MaxHR'] = ss.fit_transform(df1[['MaxHR']])
    
    # Return the modified DataFrame
    return df1

# Normalization: Oldpeak feature is normalized as it had displayed a right-skewed data distribution.
# Standardization: Age, RestingBP, Cholesterol, and MaxHR features are scaled down because these features are normally distributed.
