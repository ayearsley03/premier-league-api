# =============================================================================
# Live Premier League Data for Premier League 2025/2026 Season
# =============================================================================


import requests
import pandas as pd
from datetime import datetime

# =============================================================================
# CONFIGURATION
# =============================================================================

API_KEY = "Insert Your API Key Here"
BASE_URL = "https://api.football-data.org/v4"
OUTPUT_PATH = r"C:\Users\Alfie.Yearsley\Downloads\Python\premier-league-api\Current_Season\premier_league_data.xlsx"

headers = {
    "X-Auth-Token": API_KEY
}

# =============================================================================
# HELPER FUNCTION
# =============================================================================

def make_request(endpoint):
    """Make API request and return JSON data"""
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# =============================================================================
# GET PREMIER LEAGUE STANDINGS
# =============================================================================

def get_standings():
    """Extract current Premier League table"""
    data = make_request("/competitions/PL/standings")
    
    if data:
        table = data['standings'][0]['table']
        
        df = pd.DataFrame([{
            'position': team['position'],
            'team': team['team']['name'],
            'played': team['playedGames'],
            'won': team['won'],
            'drawn': team['draw'],
            'lost': team['lost'],
            'goals_for': team['goalsFor'],
            'goals_against': team['goalsAgainst'],
            'goal_difference': team['goalDifference'],
            'points': team['points'],
            'form': team.get('form', 'N/A')
        } for team in table])
        
        return df
    return None

# =============================================================================
# GET FIXTURES/MATCHES
# =============================================================================

def get_matches(status=None, matchday=None, date_from=None, date_to=None):
    """
    Extract Premier League fixtures
    
    Parameters:
        status: SCHEDULED, LIVE, IN_PLAY, PAUSED, FINISHED, POSTPONED, CANCELLED
        matchday: Specific matchday number (1-38)
        date_from: Start date (YYYY-MM-DD)
        date_to: End date (YYYY-MM-DD)
    """
    endpoint = "/competitions/PL/matches"
    params = []
    
    if status:
        params.append(f"status={status}")
    if matchday:
        params.append(f"matchday={matchday}")
    if date_from:
        params.append(f"dateFrom={date_from}")
    if date_to:
        params.append(f"dateTo={date_to}")
    
    if params:
        endpoint += "?" + "&".join(params)
    
    data = make_request(endpoint)
    
    if data:
        matches = data['matches']
        
        df = pd.DataFrame([{
            'matchday': match['matchday'],
            'date': match['utcDate'][:10],
            'time': match['utcDate'][11:16],
            'home_team': match['homeTeam']['name'],
            'away_team': match['awayTeam']['name'],
            'home_score': match['score']['fullTime']['home'],
            'away_score': match['score']['fullTime']['away'],
            'status': match['status'],
            'venue': match.get('venue', 'N/A')
        } for match in matches])
        
        return df
    return None

# =============================================================================
# GET TOP SCORERS
# =============================================================================

def get_top_scorers(limit=20):
    """Extract Premier League top scorers"""
    data = make_request(f"/competitions/PL/scorers?limit={limit}")
    
    if data:
        scorers = data['scorers']
        
        df = pd.DataFrame([{
            'player': scorer['player']['name'],
            'team': scorer['team']['name'],
            'goals': scorer['goals'],
            'assists': scorer.get('assists', 0),
            'penalties': scorer.get('penalties', 0),
            'matches_played': scorer['playedMatches']
        } for scorer in scorers])
        
        df['goals_per_game'] = round(df['goals'] / df['matches_played'], 2)
        
        return df
    return None

# =============================================================================
# GET TOP ASSISTS
# =============================================================================

def get_top_assists(limit=20):
    """Extract Premier League top assist providers"""
    data = make_request(f"/competitions/PL/scorers?limit={limit}")
    
    if data:
        scorers = data['scorers']
        
        df = pd.DataFrame([{
            'player': scorer['player']['name'],
            'team': scorer['team']['name'],
            'assists': scorer.get('assists', 0),
            'goals': scorer['goals'],
            'matches_played': scorer['playedMatches']
        } for scorer in scorers])
        
        # Sort by assists descending
        df = df.sort_values('assists', ascending=False).reset_index(drop=True)
        df['assists_per_game'] = round(df['assists'] / df['matches_played'], 2)
        
        return df
    return None

# =============================================================================
# EXPORT TO EXCEL
# =============================================================================

def export_to_excel():
    """Export all data to Excel file with separate sheets"""
    
    print("Fetching Premier League data...")
    print("-" * 40)
    
    # Fetch all data
    print("Getting standings...")
    standings = get_standings()
    
    print("Getting top scorers...")
    scorers = get_top_scorers(limit=20)
    
    print("Getting top assists...")
    assists = get_top_assists(limit=20)
    
    print("Getting upcoming fixtures...")
    fixtures = get_matches(status="SCHEDULED")
    
    print("-" * 40)
    
    # Write to Excel with multiple sheets
    with pd.ExcelWriter(OUTPUT_PATH, engine='openpyxl') as writer:
        
        if standings is not None:
            standings.to_excel(writer, sheet_name='Standings', index=False)
            print(f"✓ Standings: {len(standings)} teams")
        
        if scorers is not None:
            scorers.to_excel(writer, sheet_name='Top Scorers', index=False)
            print(f"✓ Top Scorers: {len(scorers)} players")
        
        if assists is not None:
            assists.to_excel(writer, sheet_name='Top Assists', index=False)
            print(f"✓ Top Assists: {len(assists)} players")
        
        if fixtures is not None:
            fixtures.to_excel(writer, sheet_name='Upcoming Fixtures', index=False)
            print(f"✓ Upcoming Fixtures: {len(fixtures)} matches")
        
        # Add metadata sheet
        metadata = pd.DataFrame({
            'Info': ['Last Updated', 'Data Source', 'Season'],
            'Value': [datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                     'football-data.org API', 
                     '2024/2025']
        })
        metadata.to_excel(writer, sheet_name='Metadata', index=False)
    
    print("-" * 40)
    print(f"✓ Data exported to: {OUTPUT_PATH}")

# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    export_to_excel()