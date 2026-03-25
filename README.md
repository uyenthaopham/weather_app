🌦️ Weather Expert App
A professional, lightweight Weather Dashboard built with Python Flask and OpenWeather API. This project demonstrates core Software Engineering principles including API Integration, Caching, and Robust Error Handling.

🚀 Key Features
Real-time Weather Data: Fetches current temperature, humidity, and weather conditions.

Smart Caching: Implemented an in-memory caching system (10-minute TTL) to reduce API calls and improve performance.

Robust Error Handling: Gracefully handles invalid city names, network timeouts, and API errors.

Security Focused: Sensitive API keys are managed via environment variables (.env).

Clean Architecture: Separated business logic (weather.py) from routing logic (app.py).

<img width="1901" height="895" alt="image" src="https://github.com/user-attachments/assets/ac79b643-ce64-4b18-aa33-c1d67831d285" />

<img width="1900" height="897" alt="image" src="https://github.com/user-attachments/assets/71b5302d-4ad0-430a-b9ea-6c5215c7ebcb" />

<img width="1903" height="894" alt="image" src="https://github.com/user-attachments/assets/48dddfee-1c13-423d-9d37-02fffa9c3143" />


🛠️ Tech Stack
Backend: Python, Flask
API: OpenWeatherMap API
Environment Management: python-dotenv
Styling: HTML5, CSS3



📦 Installation & Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/weather_app.git
    cd weather_app
    ```

2.  **Create a Virtual Environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables**:
    Create a `.env` file in the root directory and add your API Key:
    ```text
    WEATHER_API_KEY=your_actual_api_key_here
    ```

5.  **Run the Application**:
    ```bash
    python app.py
    ```
