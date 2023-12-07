import requests
from datetime import datetime
import smtplib

HOME_LAT = 66.28
HOME_LNG = 46.9960

my_email = "thapa.ramesh474@gmail.com"
password = "mlsg edyp mfhu rjen"
reciver = "thapa.ramesh474@outlook.com"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    print(response.status_code)

    data = response.json()
    print(data)

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_position = (iss_longitude, iss_latitude)
    print(iss_position)

    # to check iss postion within +-5 degrees
    if (
        HOME_LAT - 5 <= iss_latitude <= HOME_LAT + 5
        and HOME_LNG - 5 <= iss_longitude <= HOME_LNG + 5
    ):
        print("ISS is in your position")
        return True


def is_night():
    parameters = {"lat": HOME_LAT, "lng": HOME_LNG, "formatted": 0}

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


if is_iss_overhead():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=reciver,
        msg="Subject:Look Up\n\nThe ISS is above you in the sky,,,,,,,,,,,,,,",
    )
    print("Email sent")
    connection.close()
