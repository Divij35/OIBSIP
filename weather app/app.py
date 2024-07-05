import ttkbootstrap as ttk
from tkinter import messagebox, PhotoImage
from PIL import Image, ImageTk
from dotenv import load_dotenv
from io import BytesIO
import requests
import os
load_dotenv()

def weather_app(api_key, city, temperature_selection):
    try:
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "q=" + city + "&appid=" + api_key
        response = requests.get(complete_url)
        response.raise_for_status()
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            weather_description = data['weather'][0]['description']
            icon_image = data['weather'][0]['icon']
            temperature_kelvin = main['temp']
            if temperature_selection == "fahrenheit":
                temperature = (temperature_kelvin - 273.15) * 9/5 + 32
                temperature_unit = "°F"
            elif temperature_selection == "kelvin":
                temperature = temperature_kelvin
                temperature_unit = "K"
            else:
                temperature = temperature_kelvin - 273.15
                temperature_unit = "°C"             
            return (f"The temperature in {city} is {temperature:.2f}{temperature_unit} with {weather_description}.",weather_description, icon_image)
    except ValueError as e:
        messagebox.showwarning("WARNING", e)
    except KeyError:
        messagebox.showerror("ERROR","Invalid response from weather API.")
    
api = os.getenv("WEATHER_KEY")

def weather_details():
    try:
        city_name = entry_city.get()
        if not city_name:
            messagebox.showerror("Input Error", "Please enter a city name.")
        temperature = temperature_type.get().lower()
        weather, description ,icon_image = weather_app(api, city_name, temperature)
        label_weather.config(text=weather)
        if weather:
            try:
                icon_url = f"http://openweathermap.org/img/wn/{icon_image}@2x.png"
                icon_response = requests.get(icon_url)
                icon_response.raise_for_status()
                icon_data = icon_response.content
                image = Image.open(BytesIO(icon_data))
                weather_icon = ImageTk.PhotoImage(image)
                label_icon.config(image=weather_icon)
                label_icon.image = weather_icon
            except Exception as e:
                label_weather.config(text=f"Error loading icon: {e}")
    except ValueError as err:
        label_weather.config(text=err)

root = ttk.Window(themename="solar")
root.title("Weather app")
root.geometry("600x400")

ttk.Label(root, text="Enter the name of the city to the weather").pack(pady=2)

entry_city = ttk.Entry(root)
entry_city.pack(pady=4)

temperature_type = ttk.StringVar()
entry_selection = ttk.OptionMenu(root, temperature_type,"fahrenheit", "fahrenheit", "celsius", "kelvin")
entry_selection.pack(pady=4)

ttk.Button(root, text="search", command=weather_details).pack()
label_weather = ttk.Label(root)
label_weather.pack()

label_icon = ttk.Label(root)
label_icon.pack()

root.mainloop()