from twilio.rest import Client
from twilio_config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, PHONE_NUMBER, API_KEY_WAPI

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

import pandas as pd
import requests



def get_weather_response(query, api_key):
    
    url_clima =  "http://api.weatherapi.com/v1/forecast.json?key="+api_key+"&q="+query+"&days=1&aqi=no&alerts=no"
    response = requests.get(url_clima).json()
    
    return response


def extract_forecast(response, i):
    
    date = response['forecast']['forecastday'][0]['hour'][i]['time'].split()[0] #Fecha
    hour = int(response['forecast']['forecastday'][0]['hour'][i]['time'].split()[1].split(":")[0])
    condition = response['forecast']['forecastday'][0]['hour'][i]['condition']['text']
    temp = response['forecast']['forecastday'][0]['hour'][i]['temp_c']
    rain = response['forecast']['forecastday'][0]['hour'][i]['will_it_rain']
    prob_rain = response['forecast']['forecastday'][0]['hour'][i]['chance_of_rain']
    
    return date, hour, condition, temp, rain, prob_rain


def get_weather_df(response, extract_forecast):
    
    weather_data = []
    for i in range(len(response['forecast']['forecastday'][0]['hour'])):
    
        weather_data.append(extract_forecast(response, i)) 
    
    col = ['Date', 'Hour', 'Condition', 'Temp', 'Rain', '"%" of Rain']
    weather_df = pd.DataFrame(weather_data, columns=col)
    
    return weather_df


def get_rain_df(weather_df):
    
    rain_df = weather_df[(weather_df["Rain"]==1) & (weather_df["Hour"]<22) & (weather_df["Hour"]>5)]
    rain_df = rain_df[['Hour','Condition']]
    rain_df.set_index('Hour', inplace=True)
    
    return rain_df
    

def get_weather_message(weather_df,rain_df):
    
    weather_message = f'\n Hellow! \n\n\n The weather forecast for {weather_df["Date"][1]} in Medellín: \n\n\n {rain_df}'
    
    return weather_message


def send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,PHONE_NUMBER,weather_message):
    
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
             body=weather_message,
             from_=PHONE_NUMBER,
            to='+573145103005'
        )

    return print('Mensaje enviado', message.sid)
    
    
    

if __name__ == "__main__" :
    
    response = get_weather_response("Medellín", API_KEY_WAPI)
    forecast_10 = extract_forecast(response, 10)
    weather_df = get_weather_df(response, extract_forecast)
    rain_df = get_rain_df(weather_df)
    message = get_weather_message(weather_df,rain_df)
    send_message(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN,PHONE_NUMBER,message)
    

     
        

         
