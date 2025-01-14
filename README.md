
# Weather Forecasting App Using LLM

This is a Streamlit-based web application that provides real-time weather information and a 5-day weather forecast for any city. The app uses OpenWeatherMap API to fetch weather data and OpenAI's GPT model to generate natural language descriptions of the weather. It also includes interactive temperature trend visualizations powered by Plotly.

---

## Features

1. **Real-Time Weather Data**  
   - Provides information such as temperature, humidity, pressure, and wind speed for a given city.

2. **5-Day Weather Forecast**  
   - Displays a detailed forecast with temperature, weather conditions, and more.

3. **Natural Language Weather Description**  
   - Leverages OpenAI's GPT model to generate user-friendly weather summaries.

4. **Interactive Visualizations**  
   - Visualizes temperature trends over the next five days using Plotly.

---

## Project Structure

### Files and Their Purpose

#### 1. `app.py`  
The main script that contains:
   - Functions to fetch weather and forecast data using OpenWeatherMap API.
   - Integration with OpenAI's GPT for weather descriptions.
   - Streamlit code to create a user-friendly interface.

#### 2. `.gitignore`  
Lists files and directories to exclude from version control:
```plaintext
# Exclude sensitive files
.env

# Python-related exclusions
__pycache__/
*.py[cod]

# Virtual environment
venv/
```

#### 3. `.env`  
A local configuration file to store sensitive API keys:
```plaintext
OPENAI_API_KEY=your_openai_api_key
WEATHER_API_KEY=your_weather_api_key
```

> **Note**: `.env` is for local use only. For deployment on Streamlit Cloud, use Streamlit's secret management.

#### 4. `requirements.txt`  
Specifies the Python dependencies required for the project:
```plaintext
streamlit
openai
requests
python-dotenv
plotly
```

---

## Setup and Installation

### Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/weather-app-llm.git
   cd weather-app-llm
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:  
   Create a `.env` file in the project root and add:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   WEATHER_API_KEY=your_weather_api_key
   ```

5. **Run the app locally**:
   ```bash
   streamlit run app.py
   ```

6. **Access the app**:  
   Open your browser and navigate to `http://localhost:8501`.

---

## How to Use the App

1. **Enter a city name** in the input field on the sidebar.
2. **Click "Get Weather"** to fetch the data.
3. View:
   - Current weather conditions.
   - A 5-day weather forecast.
   - Natural language weather description.
   - Interactive temperature trend visualizations.

---

## Screenshots

![Screenshot 2025-01-14 171135](https://github.com/user-attachments/assets/7b53c18d-a889-4ebf-8fc7-bcc17d047bdc)


---

## Notes

- Ensure that your API keys are valid and have sufficient usage limits.
- Manage sensitive data securely using `.env` locally and Streamlit's secret management in production.

---

## Acknowledgments

- **Streamlit**: For the web application framework.
- **OpenWeatherMap API**: For real-time weather data and forecasts.
- **OpenAI**: For GPT-powered weather descriptions.
- **Plotly**: For creating interactive visualizations.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Commit your changes and push the branch.
4. Open a pull request.

---

## Contact

For queries or issues, feel free to reach out at:  
**Email**: your-email@example.com  
**GitHub**: [your-username](https://github.com/your-username)
```

### Customization Notes
1. Replace placeholders like `your_openai_api_key`, `your-weather_api_key`, and `your-username` with actual values.
2. Add screenshots under the "Screenshots" section for better visualization.
3. Provide a link to your deployed app under the "Contact" or "Usage" section.
