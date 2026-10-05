"""Poll public ISS and sun-time APIs for a nearby nighttime pass."""

import requests
from datetime import datetime, timezone
import time
import smtplib
import os
from email.mime.text import MIMEText

# 'Naruto runner battalions' once tried to take this hill. . .
A51_LAT = 37.235000
A51_LONG = -115.811111


def get_sun_times():
    parameters = {
        "lat": A51_LAT,
        "lng": A51_LONG,
        "formatted": 0,
        "date": datetime.now(timezone.utc).date().isoformat(),
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, timeout=(5, 15))
    response.raise_for_status()
    data = response.json()
    sunrise = datetime.fromisoformat(data["results"]["sunrise"]).astimezone(timezone.utc).time()
    sunset = datetime.fromisoformat(data["results"]["sunset"]).astimezone(timezone.utc).time()
    return sunrise, sunset


def is_over_area_51():
    response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=(5, 15))
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return A51_LAT-5 <= iss_latitude <= A51_LAT+5 and A51_LONG-5 <= iss_longitude <= A51_LONG+5

def is_night(sunrise, sunset):
    now = datetime.now(timezone.utc).time()
    if sunrise <= sunset:
        daylight = sunrise <= now <= sunset
    else:
        # Western locations can have a sunset after midnight in UTC.
        daylight = now >= sunrise or now <= sunset
    return not daylight


def send_alert():
    sender = "you@gmail.com"  # Local sender address.
    recipient = "you@gmail.com"  # Local recipient address.

    msg = MIMEText("The ISS is currently over Area 51!")
    msg["Subject"] = "ISS Alert"
    msg["From"] = sender
    msg["To"] = recipient

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        # Set app password as an env var in terminal prior to running this code
        server.login(sender, os.environ["GMAIL_APP_PASSWORD"])
        server.sendmail(sender, recipient, msg.as_string())


def main():
    sun_times = None
    last_fetched = None
    alerted = False

    while True:
        try:
            # Refresh sunrise/sunset once a day instead of every loop to avoid hammering the API
            today = datetime.now(timezone.utc).date()
            if today != last_fetched:
                sun_times = get_sun_times()
                last_fetched = today

            if is_over_area_51() and is_night(*sun_times):
                if not alerted:
                    print("The ISS is currently over Area 51.")
                    # send_alert()  # Enable after configuring local email settings.
                    alerted = True
            else:
                print("The ISS is currently NOT over Area 51.")
                alerted = False  # Reset so the next pass triggers a new alert

        except (requests.RequestException, ValueError, KeyError) as e:
            print(f"Network error, retrying next cycle: {e}")

        time.sleep(60)

# Only start polling when this file is run directly.
if __name__ == "__main__":
    main()
