from flask import Flask, jsonify, render_template
import requests
import os

# Initialize the Flask application
app = Flask(__name__)

# The URL for the free Premier League API
API_URL = "https://premier-league-api.vercel.app/standings"
@app.route('/')
def home():
    """
    This function serves the main index.html page.
    """
    # The render_template function looks for files in a 'templates' folder.
    # Make sure your index.html is inside a folder named 'templates'.
    return render_template('index.html')

@app.route('/api/scores')
def get_scores():
    """
    This is the API endpoint that fetches live data and returns it as JSON.
    Your frontend JavaScript will call this URL.
    """
    try:
        # Make the request to the external football API
        response = requests.get(API_URL, timeout=10)
        # Raise an exception if the request was not successful (e.g., 404, 500)
        response.raise_for_status()
        
        # Parse the JSON response from the API
        api_data = response.json()

       

        formatted_data = {
            "live": [], # Placeholder - you could add another API for this later
            "upcoming": [], # Placeholder
            "table": api_data 
        }

        return jsonify(formatted_data)

    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error fetching data from API: {e}")
        # Return an error response in JSON format
        return jsonify({"error": "Could not fetch data from the football API."}), 500

if __name__ == '__main__':
    # This runs the app on http://0.0.0.0:5000
    # 0.0.0.0 makes it accessible from outside the Docker container.
    app.run(host='0.0.0.0', port=5000, debug=True)