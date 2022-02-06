import requests
from datetime import datetime
import smtplib

MY_LATITUDE = 21.176395
MY_LONGITUDE = 79.647968


def iss_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    iss_longitude = float(response.json()["iss_position"]["longitude"])
    iss_latitude = float(response.json()["iss_position"]["latitude"])

    if iss_longitude - 2 < MY_LONGITUDE < iss_longitude + 2 and iss_latitude - 2 < MY_LONGITUDE < iss_latitude + 2:
        return True


#
# iss_coordinates = (latitude, longitude)
# print(iss_coordinates)

def is_night():
    parameters = {
        "lat": MY_LATITUDE,
        "lng": MY_LONGITUDE,
        "formatted": 0,
    }

    sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()
    rise_set = sun_response.json()

    sunrise = int(rise_set["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(rise_set["results"]["sunset"].split("T")[1].split(":")[0])
    now_time = int(datetime.utcnow().hour)
    if now_time < sunrise or now_time > sunset:
        return True


# print(sunrise)
# print(sunset)

# rise_time = int(sunrise.split("T")[1].split(":")[0])
# set_time = int(sunset.split("T")[1].split(":")[0])


# now_time = datetime.now()
# print(now_time.hour)
if iss_above() and is_night():
    mail = "pythoncodetrial@gmail.com"
    with smtplib.SMTP("smtp.google.com") as connection:
        connection.starttls()
        connection.login(user=mail, password="trial_password30")
        connection.sendmail(from_addr=mail, to_addrs=mail, msg="Subject:Look up\n\nISS is above you")
