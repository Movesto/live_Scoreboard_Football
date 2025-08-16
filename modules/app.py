from flask import Flask, jsonify, render_template
import requests # Used to make HTTP requests to the football API

# Initialize the Flask application
app = Flask(__name__)

# This is the main page of your website
@app.route('/')
def home():
    # This tells Flask to serve your index.html file
    return render_template('index.html')

# This will be your API endpoint that the JavaScript on your page will call
@app.route('/api/scores')
def get_scores():
    # --- THIS IS WHERE YOU WILL FETCH THE LIVE DATA ---
    # For now, we are just returning the same placeholder data as your frontend
    
    # In the future, you will add your API call here:
    # try:
    #     response = requests.get('https://premier-league-standings.vercel.app/api/standings')
    #     data = response.json()
    # except Exception as e:
    #     print(f"Error fetching data: {e}")
    #     data = {} # Return empty data on error
    
    # Placeholder data for now
    placeholder_data = {
        "live": [
            { "home": "Man United", "away": "Liverpool", "score": "1 - 0", "time": "78'", "homeLogo": "https://www.thesportsdb.com/images/media/team/badge/xzqdr11517660252.png", "awayLogo": "https://www.thesportsdb.com/images/media/team/badge/e2l7o71588434511.png" },
            { "home": "Arsenal", "away": "Chelsea", "score": "2 - 2", "time": "85'", "homeLogo": "https://www.thesportsdb.com/images/media/team/badge/uyhbfe1612468012.png", "awayLogo": "https://www.thesportsdb.com/images/media/team/badge/yvwvtu1448813215.png" }
        ],
        "upcoming": [
            { "home": "Man City", "away": "Tottenham", "time": "15:00", "date": "Sat, 16 Aug", "homeLogo": "https://www.thesportsdb.com/images/media/team/badge/v0d31b1612468249.png", "awayLogo": "https://www.thesportsdb.com/images/media/team/badge/k06k8f1612467920.png" }
        ],
        "table": [
            { "pos": 1, "name": "Arsenal", "mp": 5, "gd": 8, "pts": 13, "logo": "https://www.thesportsdb.com/images/media/team/badge/uyhbfe1612468012.png" }
        ]
    }
    
    return jsonify(placeholder_data)

if __name__ == '__main__':
    # This runs the app on http://127.0.0.1:5000 when you execute "python app.py"
    app.run(debug=True)