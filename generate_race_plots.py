import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import statsmodels.api as sm

sns.set(style="whitegrid")


def plot_lap_time_trend(df, race_name, team_name):
    plt.figure(figsize=(12, 6))
    for driver in df['Driver'].unique():
        driver_data = df[df['Driver'] == driver]
        plt.plot(driver_data['LapNumber'], driver_data['LapTimeSeconds'], label=driver)
    plt.title(f"Lap Time Trend – {team_name} ({race_name} 2025)")
    plt.xlabel("Lap Number")
    plt.ylabel("Lap Time (seconds)")
    plt.legend()
    plt.tight_layout()

    path = f"summaries/{race_name}_LapTimeTrend_{team_name}.png"
    plt.savefig(path)
    plt.close()

 

def plot_tire_degradation(df, race_name, team_name):
    plt.figure(figsize=(14, 5))
    for idx, driver in enumerate(df['Driver'].unique(), 1):
        plt.subplot(1, 2, idx)
        driver_data = df[df['Driver'] == driver]
        
        compounds = driver_data['Compound'].unique()
        for compound in compounds:
            subset = driver_data[driver_data['Compound'] == compound]
            # Scatter plot
            sns.scatterplot(
                data=subset,
                x="TyreLife", y="LapTimeSeconds",
                label=compound
            )
            lowess = sm.nonparametric.lowess
            smooth = lowess(subset['LapTimeSeconds'], subset['TyreLife'], frac=0.3)
            plt.plot(smooth[:, 0], smooth[:, 1], label=f"{compound} Trend")
        
        plt.title(f"Driver = {driver}")
        plt.xlabel("TyreLife")
        plt.ylabel("LapTimeSeconds")
        plt.legend()

    plt.suptitle(f"Tire Degradation – LapTime vs TyreLife ({race_name} 2025)", fontsize=14)
    plt.tight_layout(rect=[0, 0, 1, 0.95])

    path = f"summaries/{race_name}_TireDegradation_{team_name}.png"
    plt.savefig(path)
    plt.close()

def plot_pit_strategy(df, race_name, team_name):

    drivers = df['Driver'].unique()
    compounds = ["SOFT", "MEDIUM", "HARD"]
    compound_colors = {
    "SOFT": "#e74c3c",
    "MEDIUM": "#f1c40f",
    "HARD": "#2ecc71",
    "INTERMEDIATE": "#3498db",    
    "WET": "#8e44ad"        
}
    
    plt.figure(figsize=(12, 5))
    for idx, driver in enumerate(drivers):
        driver_data = df[df['Driver'] == driver]
        stint_starts = driver_data['Stint'].drop_duplicates().index
        for _, row in driver_data.iterrows():
            plt.barh(
                y=driver,
                width=1,
                left=row['LapNumber'],
                color=compound_colors.get(row['Compound'], 'gray'),
                edgecolor='black'
            )
    plt.title(f"Pit Strategy Timeline – {team_name} ({race_name} 2025)")
    plt.xlabel("Lap Number")
    plt.tight_layout()

    path = f"summaries/{race_name}_PitStrategy_{team_name}.png"
    plt.savefig(path)
    plt.close()


def generate_all_plots(df, race_name, team_name):
    df = df.copy()
 
    if 'LapTime' in df.columns:
        df['LapTimeSeconds'] = pd.to_timedelta(df['LapTime']).dt.total_seconds()

    required_cols = {'LapNumber', 'LapTimeSeconds', 'TyreLife', 'Compound', 'Driver'}
    if not required_cols.issubset(df.columns):
        print(f"⚠️ Skipping {race_name} for {team_name} due to missing required columns.")
        return

    plot_lap_time_trend(df, race_name, team_name)
    plot_tire_degradation(df, race_name, team_name)
    plot_pit_strategy(df, race_name, team_name)
