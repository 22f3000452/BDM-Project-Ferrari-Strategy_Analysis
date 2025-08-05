import os
import pandas as pd
import matplotlib.pyplot as plt

summary_dir = "summaries"
base_dir = "data/Ferrari"

races = [
    ("BelgianGrandPrix", "Belgian Grand Prix"),
    ("BritishGrandPrix", "Silverstone"),
    ("EmiliaRomagnaGrandPrix", "Imola"),
    ("JapaneseGrandPrix", "Suzuka"),
    ("MonacoGrandPrix", "Monaco")
]
racers = ["HAM", "LEC"]

os.makedirs(summary_dir, exist_ok=True)

for folder_name, race_full in races:
    for racer in racers:
        telemetry_file = f"{base_dir}/{folder_name}/{racer}_{race_full}_Telemetry.csv"
        if os.path.exists(telemetry_file):
            df = pd.read_csv(telemetry_file)
            plt.figure(figsize=(12, 6))
            plt.plot(df['Distance'], df['Speed'], label='Speed (km/h)')
            plt.xlabel('Distance (m)')
            plt.ylabel('Speed (km/h)')
            plt.title(f'{racer} Speed Trace - {race_full}')
            plt.legend()
            plt.tight_layout()
            save_path = os.path.join(summary_dir, f"{race_full}_{racer}_SpeedTrace.png")
            plt.savefig(save_path)
            plt.close()
            print(f"Saved {save_path}")
        else:
            print(f"File not found: {telemetry_file}")
