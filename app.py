from flask import Flask, render_template, request
from weather import get_weather_data 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error_message = None
    city = ""

    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if city:
           
            weather_data, error_message = get_weather_data(city)

    return render_template("index.html", 
                           weather_data=weather_data, 
                           error_message=error_message, 
                           city=city)

if __name__ == "__main__":
    app.run(debug=True)