from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "002cac3f9e02f23496458d60533b54c3"  # Replace with your OpenWeather API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error_message = None
    city = ""

    if request.method == "POST":
        city = request.form["city"]
        if city:
            try:
                url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
                response = requests.get(url)
                data = response.json()

                if data["cod"] != 200:
                    error_message = "City not found!"
                else:
                    weather_data = {
                        "temp": data["main"]["temp"],
                        "description": data["weather"][0]["description"],
                        "feels_like": data["main"]["feels_like"],
                        "humidity": data["main"]["humidity"]
                    }
            except Exception as e:
                error_message = str(e)

    return render_template("index.html", weather_data=weather_data, error_message=error_message, city=city)

if __name__ == "__main__":
    app.run(debug=True)
