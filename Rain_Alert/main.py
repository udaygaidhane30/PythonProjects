import requests

from twilio.rest import Client

api_base_address = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "b66f4dc056d58400c7f16cc0558787e0"
account_sid = "ACb3c3796f346703ab5b90f1790f9efe0e"
auth_token = "dcd3aee850d620c57ff56a44820275e1"

parameters = {
    "lat": 21.176361,
    "lon": 79.647978,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=api_base_address, params=parameters)
response.raise_for_status()
weather_data = response.json()
# for i in range(1, 12):
#     weather_code = weather_data["hourly"][i]["weather"][0]["id"]
#     if weather_code < 700:
#         print(f"Take your umbrella at {i}")
weather_slice = weather_data["hourly"][:12]

will_rain = False

for weather_hour in weather_slice:
    condition_code = weather_hour["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True


if will_rain:
    # print("take your umbrella")

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Take your umbrella, it might RAIN ☔",
        from_="+17127944714",
        to="+917507912231"
    )
    print(message.status)
