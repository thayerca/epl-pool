import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

owner_teams = {
    "Arsenal": "Casey",
    "Aston Villa": "Casey",
    "Bournemouth": "Jason ⭐️",
    "Brentford": "CB",
    "Brighton": "Megan ⭐️",
    "Burnley": "Neo ⭐️⭐️",
    "Chelsea": "CB",
    "Crystal Palace": "Jason ⭐️",
    "Everton": "Megan ⭐️",
    "Fulham": "CB",
    "Liverpool": "Neo ⭐️⭐️",
    "Luton Town": "CB",
    "Manchester City": "Jason ⭐️",
    "Manchester Utd": "Megan ⭐️",
    "Newcastle Utd": "Neo ⭐️⭐️",
    "Nott'ham Forest": "Neo ⭐️⭐️",
    "Sheffield Utd": "Casey",
    "Tottenham": "Jason ⭐️",
    "West Ham": "Casey",
    "Wolves": "Megan ⭐️",
}

owner_team_data = {
    "Squad": [key for key in owner_teams.keys()],
    "Owner": [val for val in owner_teams.values()]
}

@app.route('/', methods = ("POST", "GET"))
def html_table():
    owner_table = pd.DataFrame(data=owner_team_data)
    table_df = pd.read_html("https://fbref.com/en/comps/9/Premier-League-Stats")[0]
    merged_table = pd.merge(table_df, owner_table, on="Squad")
    extra_columns = [
        "Last 5", "Attendance", "Top Team Scorer", "Goalkeeper", "Notes"
    ]
    columns_to_drop = [col for col in extra_columns if col in merged_table.columns]
    final_table = merged_table.drop(
        columns=columns_to_drop
    )
    owner_table = final_table.groupby(["Owner"]).Pts.sum().sort_values(ascending=False).reset_index()
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
