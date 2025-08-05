import pandas as pd
from generate_race_plots import generate_all_plots
import os

races = [
    ("MonacoGrandPrix", "Monaco"),
    ("EmiliaRomagnaGrandPrix", "Imola"),
    ("JapaneseGrandPrix", "Suzuka"),
    ("BelgianGrandPrix", "Spa"),
    ("BritishGrandPrix", "Silverstone")
]

teams = ["Ferrari", "McLaren", "Mercedes"]

for team in teams:
    for folder_name, short_name in races:
        try:
            file_path = f"data/{team}/{folder_name}/{team}_{folder_name}_Laps.csv"
            if os.path.exists(file_path):
                df = pd.read_csv(file_path)
                print(f"Generating plots for {team} – {short_name}")
                generate_all_plots(df, race_name=short_name, team_name=team)
            else:
                print(f" Missing data: {file_path}")
        except Exception as e:
            print(f"Error for {team} – {short_name}: {e}")
