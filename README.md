# WeatherNow - Real-Time Weather Forecast Application

![WeatherNow Hero](https://via.placeholder.com/1200x600?text=WeatherNow+Premium+Weather+App)

## 📌 Project Overview
WeatherNow is a professional, full-stack weather application built with Python Flask and the OpenWeatherMap API. It allows users to search for any city worldwide and get real-time weather data, a 5-day forecast, and interactive features like favorite cities and search history. 

Designed with modern UI/UX principles, WeatherNow features a stunning Glassmorphism design, dark mode support, and full responsiveness across all devices.

**Repository Name:** `synent-task6-weatherapp-krushillukhi`

## ✨ Features
- **Real-Time Weather Data:** Current temperature, feels like, humidity, wind speed, pressure, visibility, and cloud percentage.
- **5-Day Forecast:** Detailed 5-day outlook with daily high/low temperatures and weather conditions.
- **Interactive Search:** Quickly search for any city worldwide.
- **Search History:** Automatically saves your last 10 searches for quick access, with the ability to clear history.
- **Favorite Cities:** Add and remove cities to your favorites list for one-click access.
- **Premium UI/UX:** 
  - Glassmorphism design elements
  - Smooth micro-animations and transitions
  - Fully responsive on mobile, tablet, and desktop
  - Dark mode support
- **Robust Error Handling:** Professional 404 and 500 error pages, along with graceful API error handling.

## 📸 Screenshots (Descriptions)
1. **Home Page:** A sleek landing page featuring a large search bar, a dynamic weather illustration, and the main features of the application.
2. **Weather Search Page (Dashboard):** Displays the current weather details (temperature, humidity, wind, etc.) in a large glassmorphic card, with the 5-day forecast cards below it.
3. **Forecast Page:** Detailed cards showing the 5-day forecast with daily icons and temperatures.
4. **Favorites Page:** A grid of saved cities with options to quickly view their weather or remove them.
5. **History Page:** A clean table listing recent searches with timestamps and "Search Again" buttons.
6. **About Page:** Project overview, technology stack details, and developer information.

## 🛠️ Technology Stack
- **Backend:** Python 3.11+, Flask, Flask-SQLAlchemy, Requests, python-dotenv
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript (Vanilla)
- **Database:** SQLite
- **API:** OpenWeatherMap API
- **Design System:** Custom CSS with Glassmorphism and CSS Variables

## 🚀 Installation Guide

### Prerequisites
- Python 3.11 or higher
- Git

### Step-by-Step Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/synent-task6-weatherapp-krushillukhi.git
   cd synent-task6-weatherapp-krushillukhi
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration Guide & API Setup
1. **Get an OpenWeatherMap API Key**
   - Go to [OpenWeatherMap](https://openweathermap.org/api) and sign up for a free account.
   - Navigate to your profile and generate an API key.

2. **Environment Variables**
   - Copy the example environment file:
     ```bash
     cp .env.example .env
     ```
   - Open `.env` and add your API key and a secret key:
     ```env
     OPENWEATHER_API_KEY=your_actual_api_key_here
     SECRET_KEY=your_random_secret_string
     ```

## 📂 Folder Structure
```
weathernow/
│
├── app.py                  # Main Flask application entry point
├── config.py               # Configuration settings
├── database.py             # SQLAlchemy db initialization
├── models.py               # Database models (SearchHistory, FavoriteCities)
├── weather_service.py      # OpenWeatherMap API integration service
├── requirements.txt        # Python dependencies
├── .env.example            # Example environment variables
├── README.md               # Project documentation
│
├── static/                 # Static assets
│   ├── css/
│   │   └── style.css       # Custom Glassmorphism styles
│   └── js/
│       └── script.js       # Frontend interactions (Dark mode, validation)
│
└── templates/              # HTML Templates (Jinja2)
    ├── base.html           # Main layout wrapper
    ├── index.html          # Home page
    ├── weather.html        # Current weather dashboard
    ├── forecast.html       # 5-day forecast include
    ├── history.html        # Recent searches page
    ├── favorites.html      # Favorite cities page
    ├── about.html          # About page
    ├── error.html          # Generic 500 error page
    └── 404.html            # Not Found page
```

## 🧪 Testing Instructions
1. **Run the Application Locally**
   ```bash
   python app.py
   ```
2. **Access the App**
   Open your browser and navigate to `http://127.0.0.1:5000`
3. **Manual Testing Checklist:**
   - [ ] Search for a valid city (e.g., London) and verify data loads.
   - [ ] Search for an invalid city and verify the error message appears.
   - [ ] Add a city to favorites and check the Favorites page.
   - [ ] Check the History page to ensure the search was logged.
   - [ ] Toggle dark mode and ensure styles apply correctly.

## 👨‍💻 Author Information
**Developed for Synent Technologies Internship Task 6**
- **Developer:** Krushil Lukhi 
- **GitHub:** [Your GitHub Profile]
- **LinkedIn:** [Your LinkedIn Profile]

---
*This project is built as a portfolio piece and showcase for modern full-stack Python development.*
