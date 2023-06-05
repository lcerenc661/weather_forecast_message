from utils import get_weather_message, get_rain_df, get_weather_df, get_weather_response, extract_forecast, send_message
from twilio_config import TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,PHONE_NUMBER,API_KEY_WAPI



query = "Medellín"

response = get_weather_response(query, API_KEY_WAPI)
weather_df = get_weather_df(response, extract_forecast)
rain_df = get_rain_df(weather_df)
message = get_weather_message(weather_df,rain_df)
send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,PHONE_NUMBER,message)