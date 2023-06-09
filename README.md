
# Daily weather forecast message

Using weatherAPI, Twilio, Python and a AWS EC2 instance to generate a daily sms with a weather forecast report.




## API Reference

#### TWILIO

```http
  GET https://www.twilio.com/en-us
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `TWILIO_ACCOUNT_SID` | `string` | **Required** |
| `TWILIO_AUTH_TOKEN` | `string` | **Required** |

#### WEATHER API

```http
  GET https://www.weatherapi.com
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `API_KEY_WAPI`      | `string` | **Required** |



