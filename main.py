# API Application proramming interface

# API je skup komandi, funkcija, protokola i objekata koje programeri koriste da naprave ili imaju interakciju sa
# eksternim sistemom
# API je barijera ili granica izmedju tvog programa i eksternog sistema, dakle koriste se pravila
# koja je API postavio da bi se napravio zahtev za ulazak dela date u eksterni sistem.
# Odgovor sistema je da ti da datu koju trazis ili da odbije.

# Bitniji aspekt API-ja je API Endpoint, primer je ako zelite novac iz banke morate da znate njenu adresu tj gde se nalazi,
# API zahtev tj request je na primer izvlacenje novca iz trezora, zato postoji bankar koji pomaze i da te spreci da udjes u trezor
# tj API koji se nalazi izmedju tvog programa i eksternog sistema.

import requests
from datetime import datetime
import smtplib
import time
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # API Endpoint dakle data koju koristimo sa ovog APIJA je dole
# response.raise_for_status()
# # response raise for status nam govori da li imamo pristup dati sa ovog APIja, code 200 znaci da, code 404 nepostojeci, code 401 da nismo ovlasceni da vidimo te podatke
# data = response.json()
# # ovo koristimo da ispisemo odgovor eksternog sistema u konzoli u json formatu
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# # ovako smo napravili posebne promenljive kojima smo dodelili vrednosti iz dictionary-a sa APIja, preko
# # key:value sistema
#
# iss_position = (longitude, latitude)
# # Ovde smo te vrednosti dodelili u tuple i ispisali ih kasnije u konzoli
# print(iss_position)
# if response.status_code != 404:
# # odgovor sistema npr 404 file not found, 200 je uspesno itd
#     raise Exception ("That response does not exist")
# elif response.status_code == 401:
#     raise Exception ("You are not authorised to acces this data")

# API parametri
# Mozemo dobiti odredjeni podatak unosenjen drugog podatka
# Npr latituda i longituda mogu da se zovu lat i lng i tipa su float, date, fromatted i callback


MY_LAT = 44.720680
MY_LNG = 19.663090
MY_EMAIL = "nemanjagajic39@gmail.com"
MY_PASSWORD = "abcdefg123"


parameters = {
    "lat":MY_LAT,
    "lng":MY_LNG,
    "formatted":0,
}

def is_iss_overhead():

    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG -5 <= iss_longitude <= MY_LNG + 5:
        return True

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])


    time_now = datetime.now().hour

    if time_now > sunset or time_now < sunrise:
        return False

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP_SSL("smtp.gmail.com")
        connection.login(MY_PASSWORD, MY_EMAIL)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="nemanjagajic73@gmail.com",
            msg="Subject:Look up \n\n ISS is above you right now"
        )

# split() metoda, splituje string pomocu separatora i stavlja ih u listu

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



