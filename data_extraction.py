from extract_team_data import extract_team_laps

races = [
    ("Monaco Grand Prix", "Monaco"),
    ("Emilia Romagna Grand Prix", "Imola"),
    ("Japanese Grand Prix", "Suzuka"),
    ("Belgian Grand Prix", "Spa"),
    ("British Grand Prix", "Silverstone")
]

for team in ["Ferrari","McLaren", "Mercedes"]:
    for full_race, short_name in races:
        print(f"Extracting: {team} - {short_name}")
        laps = extract_team_laps(2025, full_race, team)
