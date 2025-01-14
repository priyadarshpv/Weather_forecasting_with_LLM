import streamlit as st
import requests
import openai
from dotenv import load_dotenv,dotenv_values
import os
import plotly.express as px


# Function to fetch current weather data
def get_weather_data(city, weather_api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + weather_api_key + "&q=" + city
    response = requests.get(complete_url)
    return response.json()


# Function to fetch 5-day weather forecast data
def get_forecast_data(city, weather_api_key):
    base_url = "http://api.openweathermap.org/data/2.5/forecast?"
    complete_url = base_url + "appid=" + weather_api_key + "&q=" + city
    response = requests.get(complete_url)
    return response.json()


# Function to generate a weather description using OpenAI's GPT model
def generate_weather_description(data, openai_api_key):
    openai.api_key = openai_api_key
    try:
        # Convert temperature from Kelvin to Celsius
        temperature = data['main']['temp'] - 273.15
        description = data['weather'][0]['description']
        prompt = (
            f"The current weather in your city is {description} with a temperature of {temperature:.1f}°C. "
            f"Explain this in a simple way for a general audience."
        )

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=60
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return str(e)


# Function to plot temperature trends
def plot_temperature_trends(forecast_data):
    # Extract data for plotting
    dates = [entry['dt_txt'] for entry in forecast_data['list']]
    temperatures = [entry['main']['temp'] - 273.15 for entry in forecast_data['list']]

    # Create a Plotly line chart
    fig = px.line(
        x=dates, y=temperatures,
        labels={"x": "Date & Time", "y": "Temperature (°C)"},
        title="Temperature Trend for the Next 5 Days"
    )
    fig.update_layout(xaxis=dict(showgrid=False), yaxis=dict(showgrid=False))
    st.plotly_chart(fig)


# Main function to run the Streamlit app
def main():
    # Sidebar configuration
    st.sidebar.title("Weather Forecasting with LLM")
    city = st.sidebar.text_input("Enter city name", "London")



    # Load environment variables from .env file
    load_dotenv()


    openai_api_key = os.getenv("OPENAI_API_KEY")
    weather_api_key = os.getenv("WEATHER_API_KEY")

    # Button to fetch and display weather data
    submit = st.sidebar.button("Get Weather")

    if submit:
        st.title("Weather Updates for " + city)
        with st.spinner('Fetching weather data....'):
            # Fetch current weather data
            weather_data = get_weather_data(city, weather_api_key)
            if weather_data.get("cod") != 404:
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Temperature", f"{weather_data['main']['temp'] - 273.15:.2f}°C")
                    st.metric("Humidity", f"{weather_data['main']['humidity']}%")
                with col2:
                    st.metric("Pressure", f"{weather_data['main']['pressure']} hPa")
                    st.metric("Wind Speed", f"{weather_data['wind']['speed']} m/s")

                # Generate and display a friendly weather description
                weather_description = generate_weather_description(weather_data, openai_api_key)
                st.write(weather_description)

                # Fetch and display 5-day forecast data
                st.subheader("5-Day Weather Forecast")
                forecast_data = get_forecast_data(city, weather_api_key)
                if forecast_data.get("cod") == "200":
                    plot_temperature_trends(forecast_data)

                    # Display tabular forecast data
                    st.subheader("Detailed Forecast")
                    for forecast in forecast_data['list'][:10]:  # Show the next 10 entries
                        dt = forecast['dt_txt']
                        temp = forecast['main']['temp'] - 273.15
                        desc = forecast['weather'][0]['description']
                        st.write(f"{dt}: {temp:.2f}°C, {desc.capitalize()}")
                else:
                    st.error("Could not fetch forecast data. Please try again later.")
            else:
                # Display an error message if the city is not found
                st.error("City not found or an error occurred!")


if __name__ == "__main__":
    main()
