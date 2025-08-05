import pandas as pd
import os
from glob import glob

base_dir = "data"
races = ["Monaco", "Silverstone", "Spa", "Imola", "Suzuka"]

# Create Summary directory
summary_dir = "summaries"
os.makedirs(summary_dir, exist_ok=True)

def generate_metadata(df):
    metadata = pd.DataFrame({
        "Column": df.columns,
        "Data Type": [df[col].dtype for col in df.columns],
        "Non-Null Count": [df[col].count() for col in df.columns],
        "Unique Values": [df[col].nunique() for col in df.columns]
    })
    return metadata

# Analyze each race
for race in races:
    print(f"Analyzing {race} 2025...")
    
    race_file = os.path.join(base_dir, race, f"Ferrari_{race}_Laps.csv")
    if not os.path.exists(race_file):
        print(f"Data for {race} not found. Skipping.")
        continue
    
    # Load race data
    df = pd.read_csv(race_file)
    
    # Metadata
    metadata = generate_metadata(df)
    metadata.to_csv(os.path.join(summary_dir, f"{race}_Metadata.csv"), index=False)
    
    # Descriptive statistics 
    numeric_cols = df.select_dtypes(include=['float64', 'int64'])
    descriptive_stats = numeric_cols.describe().transpose()
    descriptive_stats.to_csv(os.path.join(summary_dir, f"{race}_DescriptiveStats.csv"))
    
    print(f"Metadata & stats saved for {race}.")

print("All metadata and descriptive statistics generated.")
