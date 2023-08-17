from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

owner_teams = {
    "Arsenal": "Casey",
    "Aston Villa": "Casey",
    "Bournemouth": "Jason",
    "Brentford": "CB",
    "Brighton": "Megan",
    "Burnley": "Neo",
    "Chelsea": "CB",
    "Crystal Palace": "Jason",
    "Everton": "Megan",
    "Fulham": "CB",
    "Liverpool": "Neo",
    "Luton Town": "CB",
    "Manchester City": "Jason",
    "Manchester United": "Megan",
    "Newcastle Utd": "Neo",
    "Nott'ham Forest": "Neo",
    "Sheffield Utd": "Casey",
    "Tottenham": "Jason",
    "West Ham": "Casey",
    "Wolves": "Megan",
}

owner_team_data = {
    "Squad": [key for key in owner_teams.keys()],
    "Owner": [val for val in owner_teams.values()]
}

owner_table = pd.DataFrame(data=owner_team_data)

table_df = pd.read_html("https://fbref.com/en/comps/9/Premier-League-Stats")[0]
merged_table = pd.merge(table_df, owner_table, on="Squad")
final_table = merged_table.drop(
    columns=[
        "Last 5", "Attendance", "Top Team Scorer", "Goalkeeper", "Notes"
    ]
)

owner_table = final_table.groupby(["Owner"]).Pts.sum().sort_values(ascending=False).reset_index()

@app.route('/', methods = ("POST", "GET"))
def html_table():
   return render_template(
           'index.html',
            tables=[
                final_table.to_html(
                    classes="table",
                    index=False,
                    header="true"
                ),
                owner_table.to_html(
                    classes="table",
                    index=False,
                    header="true"
                ),
            ]
        )
