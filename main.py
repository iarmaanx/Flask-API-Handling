from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Route for the homepage
@app.route("/")
def home():
    return render_template("home.html")

# Route to fetch a random food image
@app.route("/get-food-image")
def get_food_image():
    response = requests.get("https://foodish-api.com/api/")
    data = response.json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
