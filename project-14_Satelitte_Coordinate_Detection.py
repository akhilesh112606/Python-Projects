from tkinter import Canvas
import requests
from datetime import datetime
import tkinter

MY_LATITUDE = -52.4523445
MY_LONGITUDE = -25.324234
i = 1

# FUNCTIONS -----------------------------------------------------------------------
def is_in():
    global i
    if ((MY_LONGITUDE - 5) <= longitude <= (MY_LONGITUDE + 5)) and (
            (MY_LATITUDE - 5) <= latitude <= (MY_LATITUDE + 5)) and (
            sunset <= present_time.hour <= sunrise):
        return True

    return False

def check_available():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_position = (longitude, latitude)
    print(iss_position)
    response.close()

    print(is_in())
    if is_in():
        window.config(bg="green")
        canvas.config(bg="green")
        canvas.itemconfig(text_bar, text="CAN SEE ISS", font=("Arial", 10, "bold"))


    else:
        window.config(bg="red")
        canvas.config(bg="red")
        canvas.itemconfig(text_bar, text="CANNOT SEE ISS", font=("Arial", 10, "bold"))
    window.after(1000, check_available)

# ISS MOVEMENT CODE -----------------------------------------------------------

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = response.json()
longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])
iss_position = (longitude, latitude)
print(iss_position)
response.close()

# ISS MOVEMENT END CODE -------------------------------------------------------

# SUNRISE & SUNSET CODE START -------------------------------------------------

parameters = {
    "lat" : MY_LATITUDE,
    "lng" : MY_LONGITUDE,
    "formatted" : 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split('T')[1].split(':')[0])
sunset = int(data["results"]["sunset"].split('T')[1].split(':')[0 ])
present_time = datetime.now()

# SUNRISE AND SUNSET CODE END ------------------------------------------------

# TKINTER SETUP --------------------------------------------------------------
window = tkinter.Tk()
window.title("ISS CHECKER")
window.config(height=200, width=200)
window.config(bg="green")
canvas = Canvas(height=200, width=200, bg="green")
text_bar = canvas.create_text(100,100,text="Welcome",font=("Arial", 10, "bold"), fill="white")


canvas.grid(row=0, column=0)
window.after(1000, check_available)
window.mainloop()





