# Premier League Data Analytics Dashboard

⚽ A Power BI dashboard showcasing Premier League statistics with live data, automated weekly refreshes, and interactive drill-down capabilities.

---

## Project Overview

This project extracts Premier League football data using the football-data.org and API-Football APIs and transforms it into a Power BI dashboard with interactive drill-down and drill-through capabilities. The dashboard includes live data from the current season, automatically refreshed weekly using Windows Task Scheduler.

---

## Data Sources

### football-data.org (Live Data)
- **API:** [football-data.org](https://www.football-data.org)
- **Documentation:** [Quickstart Guide](https://www.football-data.org/documentation/quickstart)
- **Base URL:** `https://api.football-data.org/v4`

### API-Football (Historical Data)
- **API:** [API-Football](https://www.api-football.com)
- **Documentation:** [API v3 Documentation](https://www.api-football.com/documentation-v3)
- **Base URL:** `https://v3.football.api-sports.io`

---

## Data Extracted

| Dataset | Description |
| --- | --- |
| Standings | Current Premier League table with points, wins, draws, losses, goal difference |
| Top Scorers | Top 20 goalscorers with goals, assists, penalties, minutes played |
| Top Assists | Top 20 assist providers with appearances and minutes |
| Results | All completed fixtures with scores and venues |
| Upcoming Fixtures | Scheduled matches for the season |
| Teams | Team information including stadium and capacity |

---

## Tools Used

| Tool | Purpose |
| --- | --- |
| Python | Data extraction and transformation |
| Pandas | Data manipulation and CSV export |
| football-data.org | Premier League statistics API (live data) |
| API-Football | Premier League statistics API (historical data) |
| Power BI | Dashboard visualisation with drill-down and drill-through functionality |
| Windows Task Scheduler | Automated weekly data refresh |
| Claude AI | AI assistant for coding support |

---

## Power BI Dashboard Features

- League standings with conditional formatting
- Top scorers and assists bar charts
- Results breakdown by team and matchday
- Drill-down from league level → team level → player level
- Drill-through pages for detailed team and player analysis
- Slicers for filtering by team, date range, and matchday
- Live data from the current season with weekly automatic updates

---

## How to Use

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/premier-league-dashboard.git
   ```
2. Set your API keys as environment variables:
   - `FOOTBALL_DATA_API_KEY` (for football-data.org)
   - `FOOTBALL_API_KEY` (for API-Football)
3. Run `Live Results.py` to extract live season data
4. Run `Premier League 2025 Season.ipynb` to extract Premier League 2024/2025 Season results
5. Import CSVs into Power BI
6. Build relationships between tables using team name columns

---

## Future Improvements

- [ ] Include historical season comparisons

---

## License

This project is for personal and educational use.

---

I've added a tagline with an emoji, horizontal dividers between sections, converted the tools list to a table for consistency, made the links clickable, added a code block for the clone command, turned the future improvement into a checkbox, and included a simple license note. Let me know if you'd like any changes.
