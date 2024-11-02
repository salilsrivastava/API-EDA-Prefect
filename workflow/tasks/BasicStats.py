from prefect import task

# Task to perform basic statistical analysis on the DataFrame
@task(log_prints=True)
def basicStats(df):
    # Print the first few rows of the DataFrame
    print(f"DataFrame head:\n{df.head()}")
    
    # Summary statistics
    print("\nSummary Statistics:")
    print(df.describe(include='all'))
    
    # Checking for missing values
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # Data type information
    print("\nData Types:")
    print(df.dtypes)
