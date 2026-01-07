Premier League Data Analytics Dashboard

Project Overview
This project extracts Premier League football data using the API-Football API and transforms it into a Power BI dashboard with interactive drill-down and drill-through capabilities.

Data Source

API: API-Football (https://www.api-football.com)
Documentation: https://www.api-football.com/documentation-v3
Base URL: https://v3.football.api-sports.io


Data Extracted

Dataset              Description
Standings            Current Premier League table with points, wins, draws, losses, goal difference
Top Scorers          Top 20 goalscorers with goals, assists, penalties, minutes played
Top Assists          Top 20 assist providers with appearances and minutesResultsAll 
completed fixtures   with scores and venuesUpcoming 
FixturesScheduled    matches for the season
Teams                Team information including stadium and capacity


Tools Used

Python — Data extraction and transformation
Pandas — Data manipulation and CSV export
API-Football — Premier League statistics API
Power BI — Dashboard visualisation with drill-down and drill-through functionality

Power BI Dashboard Features

League standings with conditional formatting
Top scorers and assists bar charts
Results breakdown by team and matchday
Drill-down from league level → team level → player level
Drill-through pages for detailed team and player analysis
Slicers for filtering by team, date range, and matchday

How to Use

Clone the repository
Set your API key as an environment variable: FOOTBALL_API_KEY
Run the Python script to extract data to CSV files
Import CSVs into Power BI
Build relationships between tables using team name columns

Future Improvements

Add player ratings by team, by adding more players
Include historical season comparisons
