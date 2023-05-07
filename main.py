
from twilio.rest import Client
import requests

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "your account sid"
auth_token = "your auth token"
client = Client(account_sid, auth_token)



owm_enp = "OpenWeatherMap endpoint"
api_key = "your api key"

my_lat = "your latitude"
my_lng = -'your longitude'

weather_params = {
    "lat": my_lat,
    "lon": my_lng,
    "appid": api_key,
}


response = requests.get(url=owm_enp, params=weather_params)
print(response.status_code)

# message = client.messages \
#                 .create(
#                      body="test to see if the message will work",
#                      from_="+12677152919",
#                      to="+905526166679"
#                  )



message = client.messages.create(
    from_="your twilio number",
    body='message body',
    to="the receiving number",)

print(message.status)


